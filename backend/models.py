from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Dependency of user
class Dependency(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
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
    description = models.CharField(max_length=200)
    main_category_id = models.PositiveSmallIntegerField()
    
    def __str__(self):
        return self.name

# Article
class Article(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# States choices
STATE_AVAILABLE = 'A'
STATE_LENT = 'L'
STATE_LOST = 'O'
STATE_NOT_AVAILABLE = 'N'

# Item
class Item(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    state = models.CharField(max_length=1)
    
    def __str__(self):
        return self.article.name + ' - ' + self.name
        
    def is_available(self):
        return self.state == STATE_AVAILABLE

# Loan
class Loan(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(UserProfile)
    start_date = models.DateTimeField('Start Date')
    end_date = models.DateTimeField('End Date')
    estimated_end_date = models.DateTimeField('Estimated end date')
    observations = models.CharField(max_length=200)
    
    def __str__(self):
        return self.item


# Admin class
admin.site.register(Dependency)
admin.site.register(UserProfile)
admin.site.register(Category)
