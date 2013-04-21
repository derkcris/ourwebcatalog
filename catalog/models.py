from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# States choices
STATE_AVAILABLE = 'A'
STATE_LENT = 'L'
STATE_LOST = 'O'
STATE_NOT_AVAILABLE = 'N'
STATE_CHOICES = (
    (STATE_AVAILABLE, 'Available'),
    (STATE_LENT, 'Lent'),
    (STATE_LOST, 'Lost'),
    (STATE_NOT_AVAILABLE, 'Not available'),
)

CONDITION_RIGHT = 'R'
CONDITION_DEFECTIVE = 'D'
CONDITION_POOR = 'P'
CONDITION_OUT_OF_SERVICE = 'O'
CONDITION_CHOICES = (
    (CONDITION_RIGHT, 'Right'),
    (CONDITION_DEFECTIVE, 'Defective'),
    (CONDITION_POOR, 'Poor'),
    (CONDITION_OUT_OF_SERVICE, 'Out of service'),
)


class Dependency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dependency = models.ForeignKey(Dependency)

    def __str__(self):
        return self.user.get_full_name()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    main_category = models.ForeignKey('Category',
                                      blank=True,
                                      null=True,
                                      on_delete=models.SET_NULL)

    def __str__(self):
        if self.main_category:
            return self.name + ' (' + self.main_category.name + ')'
        else:
            return self.name


class Article(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=1,
                             choices=STATE_CHOICES,
                             default=STATE_AVAILABLE)
    condition = models.CharField(max_length=1,
                                 choices=CONDITION_CHOICES,
                                 default=CONDITION_RIGHT)

    def __str__(self):
        return self.article.name + ' - ' + self.name

    def is_available(self):
        return self.state == STATE_AVAILABLE


class Loan(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(UserProfile)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date', null=True)
    estimated_end_date = models.DateTimeField('Estimated end date',
                                              null=True)
    observations = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.item


# Admin class
class DependencyAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


class UserProfileAdmin(admin.ModelAdmin):
    fields = ['user', 'dependency']


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


class ArticleAdmin(admin.ModelAdmin):
    fields = ['category', 'name', 'description']


class ItemAdmin(admin.ModelAdmin):
    fields = ['article', 'name', 'description', 'state']

# Register class on Admin module
admin.site.register(Dependency, DependencyAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Item, ItemAdmin)
