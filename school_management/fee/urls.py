from django.urls import path
from .views import *

urlpatterns = [
    path('feecontrol_create/<int:pk>/',feecontrol_createview.as_view(),name='fee_create'),
    path('feecontrol_create/',feecontrol_createview.as_view(),name='fee_create'),


]