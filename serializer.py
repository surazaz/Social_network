from rest_framework import serializers
from mainapp.models import School, Course, Topic, Program, Room, Building
#converting model into JSON data
class SchoolSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = School
	 	fields = '__all__'
        # fields=('name','city','country')


class CourseSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Course
	 	fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Topic
	 	fields = '__all__'

class ProgramSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Program
	 	fields = '__all__'

class BuildingSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Building
	 	fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
	 class Meta:
	 	model = Room
	 	fields = '__all__'