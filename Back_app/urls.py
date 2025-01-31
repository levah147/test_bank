from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('forgot_password/',views.forgot_password, name='forgot_password'),
    path('reset_password/',views.reset_password, name='reset_password'),
    
    # ///////
    path('about/',views.about, name='about'),
    path('contact/',views.contact, name='contact'),
    path('business_backing/',views.business_backing, name='business_backing'),
    path('error_page/',views.error_page, name='error_page'),
    
    
    
    
    
    
]
