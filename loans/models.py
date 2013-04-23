from catalog.models import Item
from django.db import models
from django.contrib import admin

# States choices
STATE_IN_LOAN = 'L'
STATE_LOST = 'O'
STATE_RETURNED = 'R'
STATE_CHOICES = (
    (STATE_IN_LOAN, 'In loan'),
    (STATE_LOST, 'Lost'),
    (STATE_RETURNED, 'Returned'),
)


class Dependency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class People(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    active = models.BooleanField()
    dependency = models.ForeignKey(Dependency)
    active_loans = models.PositiveSmallIntegerField(default=0)

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.get_full_name()


class Loan(models.Model):
    item = models.ForeignKey(Item)
    people = models.ForeignKey(People)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date', null=True)
    estimated_end_date = models.DateTimeField('Estimated end date',
                                              null=True)
    state = models.CharField(max_length=1,
                             choices=STATE_CHOICES,
                             default=STATE_IN_LOAN)
    observations = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.item.name


class DependencyAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


class PeopleAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'active', 'dependency']


class LoanAdmin(admin.ModelAdmin):
    fields = ['item', 'people', 'start_date', 'end_date', 'estimated_end_date', 'observations']


admin.site.register(Dependency, DependencyAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Loan, LoanAdmin)
