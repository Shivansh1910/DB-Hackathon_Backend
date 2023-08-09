from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.DBUser)
admin.site.register(models.Book)
admin.site.register(models.UserBook)
admin.site.register(models.CounterParty)
admin.site.register(models.Security)
admin.site.register(models.Trade)
admin.site.register(models.Notification)
admin.site.register(models.Report)
admin.site.register(models.Watchlist)
