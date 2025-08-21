from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name ='home'),
   path('history',views.history,name ='history'),
   path('profile',views.profile,name ='profile'),
   path('about',views.about,name ='about'),
   path('',views.home,name='home'),
    path('indigo',views.indigo,name='indigo'),
    path('airindia',views.airindia,name='airindia'),
    path('spicejet',views.spicejet,name='spicejet'),

   path('gofirst',views.gofirst,name='first'),
   path('vistara',views.vistara,name='tara'),

    path('booking/<str:airline><int:pk>',views.booking,name='booking'),
    path('booking_details',views.booking_details,name='booking_details'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('confirm_del/<int:pk>',views.confirm_del,name='confirm_del'),
    path('del/<int:pk>',views.del_,name='del'),
    path('history/', views.history, name='history'),
    # Add these paths
    path('recover/<int:pk>/', views.recover_booking, name='recover_booking'),
    path('delete_forever/<int:pk>/', views.delete_forever, name='delete_forever'),

]
