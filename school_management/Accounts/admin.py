from django.contrib import admin
from .models import *

admin.site.register(User),
admin.site.register(Librarian),
admin.site.register(BookList),
admin.site.register(Bookissued),
admin.site.register(Office_staff),
admin.site.register(Student),
admin.site.register(Fee),
admin.site.register(LibraryTransaction),