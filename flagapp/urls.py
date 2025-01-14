from django.urls import path
from . import views
app_name='flagapp'

urlpatterns = [
   path('',views.home,name='home'),

]