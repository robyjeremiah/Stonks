from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Account)
admin.site.register(models.SecurityQuestion)
admin.site.register(models.SecurityAnswer)
