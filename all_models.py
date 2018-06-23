from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class School(models.Model):
	"""docstring for School"""
	name=models.CharField(max_length=200)
	principal=models.CharField(max_length=200)
	
	def __str__(self):
		return self.name
	# while creating or updating we need this function
	def get_absolute_url(self):
		return reverse("basic_app:detail",kwargs={'pk':self.pk})


class Student(models.Model):
	name=models.CharField(max_length=200)
	age=models.PositiveIntegerField()
	school=models.ForeignKey(School,related_name='Students')
	def __str__(self):
		return self.name
#related name is useful here to use in html {%for student in school_detail.Students.all%}

class Post(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now())
	published_date=models.DateTimeField(blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
	updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved. 

	def publish(self):
		self.published_date=timezone.now()
		self.save()
	def approve_comments(self):
		return self.comments.filter(approved_comment=True)
	def get_absolute_url(self):
		return reverse("post_detail",kwargs={'pk':self.pk})

	def __str__(self):
		return self.title

class Comment(models.Model):
	post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
	author=models.CharField(max_length=400)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now())
	approved_comment=models.BooleanField(default=False)

	def approve(self):
		self.approved_comment=True

class Product(models.Model):
	name = models.CharField(max_length=255,unique=True)
	slug = models.SlugField(max_length=50,unique=True,help_text='Unique value for product url,created from name')
	brand = models.CharField(max_length=255)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	old_price = models.DecimalField(max_digits=9,decimal_places=2,blank=True,default=0.00)
	image = models.ImageField(upload_to='product/%Y/%m/%d')
	is_active = models.BooleanField(default=True)
	is_bestseller = models.BooleanField(default=False)
	is_featured = models.BooleanField(default=False)
	quantity = models.IntegerField()
	description = models.TextField()
	meta_keywords = models.CharField('meta keywords',max_length=255,help_text='Comma-delimited set of SEO keywords for meta tag')
	meta_description = models.CharField('meta description',max_length=255,help_text='Content for description meta tag')
	created_at = models.DateTimeField(auto_now_add=True) #Automatically set the field to now when the object is first created.
	updated_at = models.DateTimeField(auto_now=True) #Automatically set the field to now every time the object is saved. 
	categories = models.ManyToManyField(Category) 

	class Meta:
		db_table = 'products'
		ordering = ['-created_at']

	def __str__(self):
		return self.name 
		self.save()
	def __str__(self):
		return self.text
	def get_absolute_url(self):
		return reverse("post_list")

class Cv_Info(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,primary_key=True)
    # cv_id=models.IntegerField()
    name=models.CharField(max_length=100,default='name')
    headline=models.CharField(max_length=400,default='(e.g. Front-end developer)')
    photo=models.ImageField(blank=True,default='avatar.jpg')

    def __str__(self):
        return self.name

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title  = models.CharField(max_length=500)
	genre = models.CharField(max_length=100)
	album_logo = models.FileField(max_length=1000)

	def get_absolute_url(self):
		return reverse('music:detail',kwargs={'pk':self.pk})
	def __str__(self):
		return self.album_title+"-"+self.artist


class Song(models.Model):
	album = models.ForeignKey(Album,on_delete=models.CASCADE)
	#part of album and on_delete cascade means whever we delete album song is itself deleted
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	is_fav=models.BooleanField(default=False)
	def __str__(self):
		return self.song_title
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	description=models.CharField(max_length=200,default='')
	city=models.CharField(max_length=50,default='')
	phone=models.IntegerField(default='0')
	
def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)	
#For sending email in settings.py
EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='djangosuraj@gmail.com'
EMAIL_PORT=587
EMAIL_HOST_PASSWORD='django@123'


