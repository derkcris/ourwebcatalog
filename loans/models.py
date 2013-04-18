from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Dependency of user
class Dependency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

# User
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    dependency = models.ForeignKey(Dependency)

    def __str__(self):
        return self.user.get_full_name()

# Category of Article
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    main_category = models.ForeignKey('loans.Category',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# Article
class Article(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


# Item
class Item(models.Model):
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

    article = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=1,
        choices=STATE_CHOICES,
        default=STATE_AVAILABLE)

    def __str__(self):
        return self.article.name + ' - ' + self.name

    def is_available(self):
        return self.state == STATE_AVAILABLE

# Loan
class Loan(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(UserProfile)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date', null=True)
    estimated_end_date = models.DateTimeField('Estimated end date', null=True)
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

