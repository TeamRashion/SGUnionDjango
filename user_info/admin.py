from django.contrib import admin
from .models import UserInfo, UserEmail

# Register your models here.
admin.site.register(UserInfo)
admin.site.register(UserEmail)
