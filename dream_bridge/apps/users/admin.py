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
    verbose_name_plural = 'User Videos'

class UserDAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Users'
    pass

class CompanyAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Companies'
    pass

class JobAdmin(admin.ModelAdmin):
    verbose_name_plural = 'Jobs'
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(UserDVideo, UserDVideoAdmin)
admin.site.register(UserD, UserDAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)

