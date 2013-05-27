from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Consultant(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    rate = models.FloatField(default=0.00)
    def __unicode__(self):
        return self.name

class WorkSession(models.Model):
    consultant = models.ForeignKey(Consultant)
    account = models.ForeignKey(Account)
    date = models.DateField()
    def __unicode__(self):
        return self.consultant.name + ' - ' + self.account.name + ' - ' + str(self.date)

class WorkUnit(models.Model):
    workSession = models.ForeignKey(WorkSession)
    service = models.ForeignKey(Service)
    duration = models.FloatField(default=0.00)
    def __unicode__(self):
        return str(self.workSession) + ' - ' + self.service.name + ' - ' + str(self.duration) + ' hours'
