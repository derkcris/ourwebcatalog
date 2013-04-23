from catalog.models import Item
from django.db import models
from django.contrib import admin

# States choices
STATE_IN_LOAN = 'L'
STATE_LOST = 'O'
STATE_RETURNED = 'R'
STATE_CHOICES = (
    (STATE_IN_LOAN, 'En prestamo'),
    (STATE_LOST, 'Perdido'),
    (STATE_RETURNED, 'Devuelto'),
)

CONDITION_GOOD = 'G'
CONDITION_DEFECTIVE = 'D'
CONDITION_POOR = 'P'
CONDITION_OUT_OF_SERVICE = 'O'
CONDITION_CHOICES = (
    (CONDITION_GOOD, 'Bueno'),
    (CONDITION_DEFECTIVE, 'Defectuoso'),
    (CONDITION_POOR, 'Pesimo'),
    (CONDITION_OUT_OF_SERVICE, 'Fuera de servicio'),
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
    condition_loan = models.CharField(max_length=1,
                                      choices=CONDITION_CHOICES,
                                      null=False)
    condition_return = models.CharField(max_length=1,
                                        choices=CONDITION_CHOICES,
                                        null=True)
    observations_loan = models.TextField(null=True)
    observations_return = models.TextField(null=True)

    def __str__(self):
        return self.item.name

    def get_state(self):
        for s in STATE_CHOICES:
            if self.state == s[0]:
                return s[1]
        return STATE_IN_LOAN

    def get_condition_loan(self):
        for c in CONDITION_CHOICES:
            if self.condition_loan == c[0]:
                return c[1]
        return ''

    def get_condition_return(self):
        for c in CONDITION_CHOICES:
            if self.condition_return == c[0]:
                return c[1]
        return ''


class DependencyAdmin(admin.ModelAdmin):
    fields = ['name',
              'description']


class PeopleAdmin(admin.ModelAdmin):
    fields = ['first_name',
              'last_name',
              'email',
              'active',
              'dependency',
              'active_loans']


class LoanAdmin(admin.ModelAdmin):
    fields = ['item',
              'people',
              'start_date',
              'end_date',
              'estimated_end_date',
              'state',
              'condition_loan',
              'condition_return',
              'observations_loan',
              'observations_return']


admin.site.register(Dependency, DependencyAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Loan, LoanAdmin)
