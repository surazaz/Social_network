IN Views.py

from django.shortcuts import get_object_or_404, redirect
from rest_framework import mixins, generics

from mainApp.models import  School
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.serializers import SchoolSerializer


class SchoolList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_list.html'

    def get(self, request):
        queryset = School.objects.all()
        return Response({'schools': queryset})




class SchoolDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        return redirect('school-list')
class SchoolForm(mixins.ListModelMixin,from django.shortcuts import get_object_or_404, redirect
from rest_framework import mixins, generics

from mainApp.models import  School
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.serializers import SchoolSerializer


class SchoolList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_list.html'

    def get(self, request):
        queryset = School.objects.all()
        return Response({'schools': queryset})




class SchoolDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_detail.html'

    def get(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school)
        return Response({'serializer': serializer, 'school': school})

    def post(self, request, pk):
        school = get_object_or_404(School, pk=pk)
        serializer = SchoolSerializer(school, data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer, 'school': school})
        serializer.save()
        return redirect('school-list')
class SchoolForm(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = School.objects.all()

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_form.html'
    def get(self, request):
        serializer = SchoolSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('school-list')

                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = School.objects.all()

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'school_form.html'
    def get(self, request):
        serializer = SchoolSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        serializer.save()
        return redirect('school-list')

In urls.py

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from mainApp import views

urlpatterns = [
    url(r'^schools/$', views.SchoolList.as_view(),name='school-list'),
    url(r'^schools/add$', views.SchoolForm.as_view(),name='school-add'),

    url(r'^schools/(?P<pk>[0-9]+)/$', views.SchoolDetail.as_view(),name='school-detail'),

]

Inside templates/school_detail.html
{% load rest_framework %}

<html><body>

<h1>School - {{ school.name }}</h1>

<form action="{% url 'school-detail' pk=school.pk %}" method="POST">
    {% csrf_token %}
    {% render_form serializer %}
    <input type="submit" value="Save">
</form>

</body></html>

Inside templates/school_form.html
{% load rest_framework %}

<form class="form-horizontal" action="{% url 'school-add' %}" method="post" novalidate>
    {% csrf_token %}
    {% render_form serializer %}
    <div class="form-group">
        <div class="col-sm-offset-2 col-sm-10">
            <button type="submit" class="btn btn-default">Save</button>
        </div>
    </div>
</form>

Inside templates/school_list.html
<html><body>
<h1>Schools</h1>
<ul>
    {% for school in schools %}
    <li>{{ school.name }}</li>
    {% endfor %}
</ul>
</body></html>

