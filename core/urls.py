from django.urls import path
from . import views
from .views import CustomLogoutView,CustomLoginView

app_name='core'
urlpatterns = [
    path('', views.index, name='index'),
    path('signUp/', views.signUp, name='signUp'),
    path('login/',CustomLoginView.as_view(), name='login'),
    path('logout/',CustomLogoutView.as_view(), name='logout'),
  
]