from .import views
from django.urls import path
app_name='bankapp'

urlpatterns = [
        path('', views.home, name='home'),
        path('login/', views.login, name='login'),
        path('register/', views.registerPage, name='register'),
        path('logout/', views.logOutUser, name='logout'),
        path('entry/', views.entry, name='entry'),
        path('form/', views.form, name='form'),
        path('submit/', views.submit, name='submit'),




]