# Create your urls here.

from django.urls import path
from . import views

#urlpatterns=[path('',views.yoga,name='yoga')]
#from django.urls import path
#from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),]