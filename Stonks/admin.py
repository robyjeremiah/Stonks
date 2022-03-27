from django.contrib import admin
from . import models

admin.site.register(models.User)
admin.site.register(models.Account)
admin.site.register(models.SecurityQuestion)
admin.site.register(models.SecurityAnswer)
admin.site.register(models.Transaction)
admin.site.register(models.Journal_Transaction)
admin.site.register(models.Journal)
