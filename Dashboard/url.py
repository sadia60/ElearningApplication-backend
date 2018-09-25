from django.urls import include, path
from . import views

urlpatterns = [

    path('course',views.CourseList.as_view()),
    path('video', views.VideoList.as_view()),

    #path('', views.UserListView.as_view()),

#Dashboard
    # url(r'^course/', CourseList.as_view()),
    # url(r'^courses/(?P<pk>[0-9]+)/$', CourseDetail.as_view()),
    #
    # url(r'^video/', VideoList.as_view()),
    # url(r'^videos/(?P<pk>[0-9]+)/$', VideoDetail.as_view()),

    #  path('rest-auth/registration/', include('rest_auth.registration')),



]