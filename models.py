
from django.db import models
from rest_framework.fields import ListField

IMP_CHOICES = (
    ('Nepal', 'Nepal'),
    ('Bhutan', 'Bhutan'),
    ('Sweden', 'Sweden'),
)


class School(models.Model):
    name = models.CharField(max_length=200, blank=False)
    street_address = models.CharField(max_length=200, blank=False)
    postal_code = models.CharField(max_length=10, blank=False)
    city = models.CharField(max_length=200, blank=False)
    country = models.CharField(max_length=100, choices=IMP_CHOICES)
    phone = models.CharField(max_length=20, blank=True)
    website = models.URLField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Program(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=500, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    program = models.ManyToManyField(Program)
    title = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=400, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Building(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name_or_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name_or_number


class Room(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return self.room_number


class SchoolAnnouncement(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(max_length=1000, blank=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProgramAnnouncement(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(max_length=1000, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CourseAnnouncement(models.Model):
    title = models.CharField(max_length=200, blank=False)
    body = models.TextField(max_length=1000, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class CourseSchedule(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class User(models.Model):
    name = models.CharField(max_length=200)
    street_address = models.IntegerField(blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField(max_length=20, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=100)
    designation = models.CharField(max_length=200)
    dob = models.DateField(max_length=8)
    subject_of_interest = models.CharField(max_length=200, blank=True, null=True)
    special_care_needed = models.CharField(max_length=1, choices=(
        ('Y', 'Yes'),
        ('N', 'No')
    ))


class Question(models.Model):
    question=models.TextField(max_length=500)
    correct_answer=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)

