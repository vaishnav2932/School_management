from django.urls import path
from .views import *

urlpatterns = [
    path('students/',StudentView.as_view(),name='student_detail'),
    path('students/<int:id>/',StudentView.as_view(),name='student_detail'),
    path('Library_history/<int:id>/',libraryhistory.as_view(),name='library-history'),
    path('Library_history/',libraryhistory.as_view(),name='library-history'),

]