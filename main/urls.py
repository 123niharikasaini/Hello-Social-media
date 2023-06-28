from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name="hello"),
    path('signUp',views.signUp,name="signUp"),
    path('forgetPassword',views.forgetPassword,name="forgetPassword"),
    path('helloHome',views.helloHome,name="helloHome"),
    path('signOut',views.signOut,name="signOut"),
    path('settings',views.settings,name="settings"),
    path('upload',views.upload,name="upload"),

]