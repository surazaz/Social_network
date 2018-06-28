sufee-admin-dashboard-master
def edit_school(request):
    if request.method == 'POST':
        # form=UserChangeForm(request.POST,instance=rerequestquest.user)
        form = SchoolForm(request.POST)
        request.POST._mutable = True
        r=request.POST


        if form.is_valid:
            schoolid=r['csrfmiddlewaretoken']
            del r['csrfmiddlewaretoken']
            print(r)
            db.child("school").child(schoolid).set(request.POST)
            return redirect('school')
    else:
        # form=UserChangeForm(instance=request.user)
        form = SchoolForm()
        args = {'form': form}


    return render(request, "addschool.html", args)

# path('school/', views.school,name='school'),
# path('school/<int:id>\d+)/', views.school,name='school'),
path('school/edit/', views.edit_school,name='edit_school'),

addschool.html

<title>Profile</title>

<h2>Edit Profile</h2>
<form method="POST">
	{%csrf_token%}
	{{form.as_p}}
	<button type="submit">Submit</button>
</form>

