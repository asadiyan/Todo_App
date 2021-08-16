"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/', views.add, name="add"),
    # '' empty makes the index.html page as a homepage
    path('', views.index, name="index"),
    # the reason for passing int:taskid is because we passed it in views.html
    path('delete/<int:taskid>/', views.delete, name="delete"),
    path('edit/<int:taskid>/', views.edit, name="edit"),
    # cbv = class based view
    # because TaskListView is a class so we put as_view() function to end of it
    path('cbvindex/', views.TaskListView.as_view(), name="cbvindex"),
    # we put int:pk(pk is primary key same as id we passed in before) there becouse we need it to know wich item we want to see the detail
    path('cbvdetail/<int:pk>', views.TaskDetailView.as_view(), name="cbvdetail"),
    path('cbvupdate/<int:pk>', views.TaskUpdateView.as_view(), name="cbvupdate"),
    path('cbvdelete/<int:pk>', views.TaskDeleteView.as_view(), name="cbvdelete"),
]
