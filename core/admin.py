from django.contrib import admin
from .models import *

# admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(UserSub)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email')
    fieldsets = (
        (None, {
            "fields": (
                ('username'), ('first_name', 'last_name'), ('email'), 'is_active'
            ),
        }),
    )
    

admin.site.register(Profile, UserAdmin)
