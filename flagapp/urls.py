from django.urls import path
from . import views
app_name='flagapp'

urlpatterns = [
   path('',views.home,name='home'),
   path('demo/',views.demo,name='demo'),
   path('about/',views.about,name='about'),
   path('registeration/',views.registeration,name='registeration'),
   path('payment-success/',views.payment_success, name='payment_success'),
   path('success/',views.success_page, name='success_page'),
   path('levels/',views.levels,name='levels'),
   path('whyflag/',views.whyflag,name='whyflag'),
   path('germany/',views.germany,name='germany'),


]