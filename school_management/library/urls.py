from django.urls import path
from .views import *

urlpatterns =[
    path('library_history/',LibraryHistory.as_view(),name='history_library'),
    path('library_edit/<int:pk>/',LibraryUpdate.as_view(),name='library_edit'),
    path('libray_history_delete/<int:pk>/',library_delete.as_view(),name='libror_history_deletey'),
    path('libray_transaction_create/',Librarycreate.as_view(),name='transaction_create'),

]