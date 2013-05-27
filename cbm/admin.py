from django.contrib import admin
from cbm.models import Consultant, Account, Service, WorkSession, WorkUnit

admin.site.register(Consultant)
admin.site.register(Account)
admin.site.register(Service)
admin.site.register(WorkSession)
admin.site.register(WorkUnit)
