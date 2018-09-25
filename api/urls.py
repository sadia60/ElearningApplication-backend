from django.urls import include, path

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Dashboard.views import CourseList,CourseDetail,VideoList,VideoDetail
#from rango import views
from django.conf.urls import include, url
from django.conf import settings

urlpatterns = [
 #
    path('users/', include('users.urls')),
    #
   path('Dashboard/', include('Dashboard.url')),
    #
    path('Quiz/', include('Quiz.url')),

    #
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))

#Dashboard
    # url(r'^course/', CourseList.as_view()),
    # url(r'^courses/(?P<pk>[0-9]+)/$', CourseDetail.as_view()),
    #
    # url(r'^video/', VideoList.as_view()),
    # url(r'^videos/(?P<pk>[0-9]+)/$', VideoDetail.as_view()),

    #  path('rest-auth/registration/', include('rest_auth.registration')),

]

urlpatterns=format_suffix_patterns(urlpatterns)