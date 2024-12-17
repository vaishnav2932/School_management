from django.urls import path
from .views import *

urlpatterns = [
    path('office_staffget/<int:pk>/',OfficeStaffGet.as_view(),name='office_staff_get'),
    path('office_staffget/',OfficeStaffGet.as_view(),name='office_staff_get'),
    path('librarianget/',LibrarianGet.as_view(),name='librarian_get'),
    path('librarianget/<int:pk>/',LibrarianGet.as_view(),name='librarian_get'),
    path('offisestaff_create/',ofiicestaff_creationview.as_view(),name='create_staff'),
    path('librarian_create/',librarian_createview.as_view(),name='create_librarian'),
    path('ofiicestaff_edit/<int:pk>/edit/',officestaff_updateview.as_view(),name='staff_update'),
    path('liabrarian_edit/<int:pk>/edit/',librarian_updateview.as_view(),name='update_librarian'),
    path('student_create/',Student_creation.as_view(),name='student_create'),
    path('student_edit/<int:pk>/edit/',student_update.as_view(),name='student_update'),
    path('student/',student_details.as_view(),name='student_detail'),
    path('student/<int:id>/',student_details.as_view(),name='student_detail'),

]