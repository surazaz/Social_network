from django import forms
from django.db import models

from mainapp.models import User, School, Room, Building, Topic, Course, Program, CourseSchedule, Question
IMP_CHOICES = (
    ('Nepal', 'Nepal'),
    ('Bhutan', 'Bhutan'),
    ('Sweden', 'Sweden'),
)
etcfield = models.CharField(max_length=100, choices=IMP_CHOICES)


class StaffForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('dob', 'special_care_needed', 'subject_of_interest',)


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation',)


class ParentForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ('designation', 'subject_of_interest', 'special_care_needed','dob',)




def getform(formtype):
    if formtype == 'Schools':
        modelform = School
    elif formtype == 'Rooms':
        modelform = Room
    elif formtype == 'Buildings':
        modelform = Building
    elif formtype == 'Topics':
        modelform = Topic
    elif formtype == 'Courses':
        modelform = Course
    elif formtype == 'Programs':
        modelform = Program
    elif formtype == 'CourseSchedules':
        modelform = CourseSchedule
    elif formtype == 'Questions':
        modelform = Question
    return(modelform)

class MyStyleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MyStyleForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
