from django.shortcuts import render, redirect
import pyrebase
from django.contrib import auth
from django import forms
from django.utils.safestring import mark_safe
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.utils import json

from.forms import *
from mainapp.models import School, Room, Building, Topic, Course, Program, CourseSchedule

# Create your views here.
from mainapp.forms import StaffForm, StudentForm, ParentForm
from mainapp.serializer import SchoolSerializer

config = {
    'apiKey': "AIzaSyCrAG2_pI8A00gIAPBniRLqv7Kym2d97f0",
    'authDomain': "fir-project-8cea6.firebaseapp.com",
    'databaseURL': "https://fir-project-8cea6.firebaseio.com",
    'projectId': "fir-project-8cea6",
    'storageBucket': "fir-project-8cea6.appspot.com",
    'messagingSenderId': "609798741798"

}

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
db = firebase.database()
storage = firebase.storage()
# ids = list(db.child('Schools').shallow().get().val())
# mykeys = list(db.child('Schools').child(ids[1]).get().val().keys())
# allvalues = db.child('Schools').get().val()




items=['Schools','Rooms','Buildings','Topics', 'Courses', 'Programs', 'CourseSchedules','Questions']


def sign(request):
    return render(request, "source/login.html")


def postsign(request):
    email = request.POST.get("email")
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
        return render(request, "source/admin.html",{'items':items})
    except:
        message = "Invalid Credentials"
        print(message)
        return render(request, "source/login.html", {"messg": message})

    # print(user['idToken'])
    # session_id = user['idToken']
    # request.session['uid'] = str(session_id)


def allform(request, formtype,id=None):
    class AllForm(MyStyleForm):
        class Meta:
            model = getform(formtype)
            fields = ('__all__')
    # for editing forms
    if id:
        forminstance=db.child(formtype).child(id).get().val()
        form = AllForm(forminstance)
    # for adding new data into forms
    else:
        form=AllForm()

    if request.method == 'POST':
        form = AllForm(request.POST)
        # print(request.POST)
        xyz=dict(request.POST)
        print(xyz.keys())
        pqr=xyz['MyUser']
        request.POST._mutable = True
        r=request.POST


        del r['csrfmiddlewaretoken']
        del r['MyUser']

        mno=r
        print(mno)
        data={'user':pqr,'details':mno}

        if form.is_valid:
            # schoolid = r['csrfmiddlewaretoken']
            # del r['csrfmiddlewaretoken']
            # me=mark_safe(json.dumps(r))
            db.child(formtype).push(data)

            return redirect('/mainapp/home/')
    args = {'form': form, 'items':items}

    return render(request, 'allforms.html', args)


def home(request):
    # print(allvalues)
    myvalues=[]
    # print(mykeys)
    # print(allvalues)
    # for i in mykeys:
    #     myvalues.append(allvalues[i])
    from django.utils.safestring import mark_safe
    import json
    x=mark_safe(json.dumps(allvalues))
    print(x)
    # print(myvalues)
    # serializer = SchoolSerializer(allvalues)
    # print(serializer)
    # return Response({'serializer': serializer, 'profile': profile})
    # genres = keys['city']
    # print(title)
    # print(genres)
    # for i in ids:
    #     for j in keys:
    #         bc=db.child('Schools').child(i).get().val()[j]
    #         print(bc)
    #     print("break")
    testing={'hello':'hy','numb':45}

    return render(request, 'home.html',{'x':x,'ids':ids})


def userform(request, formtype):
    if formtype == 'staff':
        form = StaffForm()
        category = "Staff"
    elif formtype == 'student':
        form = StudentForm()
        category = "Student"
    elif formtype == 'parent':
        form = ParentForm()
        category = "Parent"

    if request.method =='POST':
        # print(request.POST)
        request.POST._mutable = True
        r = request.POST

        if form.is_valid:
            del r['csrfmiddlewaretoken']
            print(json.dumps(r))
            db.child("Users").child(category).push(r)
            return redirect('abcyutjytg')

    args = {'form': form, 'items': items}

    return render(request, "source/form.html", args)

from rest_framework.views import APIView


class ProfileDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, requests,pk):
        ids = list(db.child('Schools').shallow().get().val())
        mykeys = list(db.child('Schools').child(ids[1]).get().val().keys())
        allvalues = db.child('Schools').child(ids[1]).get().val()
        serializer = SchoolSerializer(allvalues)
        return Response({'serializer': serializer})

    #
    # def post(self, request, pk):
    #     profile = get_object_or_404(Profile, pk=pk)
    #     serializer = ProfileSerializer(profile, data=request.data)
    #     if not serializer.is_valid():
    #         return Response({'serializer': serializer, 'profile': profile})
    #     serializer.save()
    #     return redirect('profile-list')

def test(request):
    allvalues = db.child('Schools').get().val()
    import json
    jsonobj=mark_safe(json.dumps(allvalues))
    return render(request,'test.html',{'jsonobj':jsonobj})
    # # print(allvalues)
    # print(mykeys)
    #
    # print(ids)
    # whole_data=[]
    # single_data=[]
    # for j in range(len(ids)):
    #     datas = [ids[j]]
    #     for i in range(len(mykeys)):
    #         datas.append(db.child('Schools').child(ids[j]).get().val()[mykeys[i]])
    #     whole_data.append(datas)
    #     # whole_data.append(single_data)
    # print(datas)
    # print(single_data)
    # mykeys.insert(0, "schoolid")
    # # print(whole_data)
    # comb_list=zip(mykeys,whole_data)
    # print(comb_list)
