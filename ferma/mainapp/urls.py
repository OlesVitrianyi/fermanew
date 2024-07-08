from django.urls import path, include
from django.views.generic import TemplateView

from .views import *


urlpatterns = [
   path('', index, name='index'),
   path('about_us', about_us, name='about_us'),
   path('bank_details', bank_details, name='bank_details'),
   path('contact_us', contact_us, name='contact_us'),
   path('documents/rules_of_stay', rules_of_stay, name='rules_of_stay'),
   path('documents/check_in_rules/', check_in_rules, name='check_in_rules'),
   path('documents/booking_rules/', booking_rules, name='booking_rules'),
   path('documents/privacy-policy/', privacy_policy, name='privacy_policy'),
   path('post/<slug:post_slug>/', show_post, name='post'),
   path('holiday_house/1/', holiday_house_1, name='holiday_house_1'),
   path('holiday_house/2/', holiday_house_2, name='holiday_house_2'),
   path('holiday_house/3/', holiday_house_3, name='holiday_house_3'),
   path('holiday_house/4/', holiday_house_4, name='holiday_house_4'),
   path('holiday_house/5/', holiday_house_5, name='holiday_house_5'),
   path('holiday_house/6/', holiday_house_6, name='holiday_house_6'),
   path('holiday_house/7/', holiday_house_7, name='holiday_house_7'),
   path('booking/', booking, name='booking'),
   path('booking-submit', bookingSubmit, name='bookingSubmit'),
path('delete_booking/<int:id>/', delete_booking, name='delete_booking'),  # test
   path('user-panel', userPanel, name='userPanel'),
   path('user-update/<int:id>', userUpdate, name='userUpdate'),
   path('user-update-submit/<int:id>', userUpdateSubmit, name='userUpdateSubmit'),
   path('staff-panel', staffPanel, name='staffPanel'),
]



