from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from models import Profile, Job, UserD, UserDVideo, Company

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(UserAdmin):
    inlines = (ProfileInline, )

class UserDVideoAdmin(admin.ModelAdmin):
    pass

class UserDAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

class JobAdmin(admin.ModelAdmin):
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserDVideo, UserDVideoAdmin)
admin.site.register(UserD, UserDAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)

