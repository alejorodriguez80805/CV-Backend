from django.contrib import admin
from backend.models import Profile,CV, Education,Experience, Courses 

# class ProfileInLine(admin.StackedInLine):
# 	model = Profile
# 	extra = 1


class CVAdmin(admin.ModelAdmin):
	fields = ['container']



admin.site.register(CV, CVAdmin)
admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Courses)
