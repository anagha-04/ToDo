"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user_app.views import *
from task_app.views import *
from API.views import*


urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',RegisterView.as_view(),name ="signup"),
    path('login/',LoginView.as_view(),name ="login"),
    path('logout/',LogoutView.as_view(),name = "logout"),
    path('add_task/',AddTaskView.as_view(),name="add_task"),
    path('list/',TaskList.as_view(),name="task_list"),
    path('update/<int:pk>',TaskUpdate.as_view(),name='task_update'),
    path("", BaseView.as_view(), name="home"),
    path('delete/<int:pk>',TaskDelete.as_view(),name='task_delete'),
    path('complete/<int:pk>',TaskComplete.as_view(),name ="complete"),
    path('search/',TaskSearchView.as_view(),name="search"),
    path('list/',UserRegisterView.as_view(),name="list_create"),
   
    
]
