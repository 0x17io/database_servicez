from django.contrib import admin

from .models import *
# test
admin.site.register(Account)
admin.site.register(Client)
admin.site.register(Contractor)
admin.site.register(Service)
admin.site.register(ServiceType)
admin.site.register(Request)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Review)
admin.site.register(Administrator)
admin.site.register(AdminRole)