from django.urls import path
from mainapp import views

urlpatterns = [
    path('sign/', views.sign, name='signin'),
    path('test/', views.test),
    path('api/', views.ProfileDetail.as_view()),
    path('postsign/', views.postsign, name='admin'),
    path('allform/<str:formtype>/', views.allform,name='allform'),
    path('allform/<str:formtype>/<str:id>', views.allform,name='allform'),
    path('home/', views.home, name='home'),
    path('userform/<str:formtype>/', views.userform, name='userform'),

]
