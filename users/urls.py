from django.urls import include, path
from . import views

urlpatterns = [
    path('user/', views.UserListView.as_view()),
]