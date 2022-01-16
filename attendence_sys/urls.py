from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home2/', views.home2Page, name='home2'),
    path('update_student_/', views.update_student_, name='update_student_'),
    
    path('AddStudent/', views.AddStudent, name='AddStudent'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('searchattendence/', views.searchAttendence, name='searchattendence'),
    path('account/', views.facultyProfile, name='account'),

    path('updateStudentRedirect/', views.updateStudentRedirect, name='updateStudentRedirect'),
    path('updateStudent/', views.updateStudent, name='updateStudent'),
    path('attendence/', views.takeAttendence, name='attendence'),
    # path('video_feed/', views.videoFeed, name='video_feed'),
    # path('videoFeed/', views.getVideo, name='videoFeed'),
]
