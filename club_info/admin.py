from django.contrib import admin
from .models import ClubInfo, MemberInfo, AdminInfo

# Register your models here.
admin.site.register(ClubInfo)
admin.site.register(MemberInfo)
admin.site.register(AdminInfo)
