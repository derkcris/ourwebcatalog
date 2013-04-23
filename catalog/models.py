from django.db import models
from django.contrib import admin

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

CONDITION_GOOD = 'G'
CONDITION_DEFECTIVE = 'D'
CONDITION_POOR = 'P'
CONDITION_OUT_OF_SERVICE = 'O'
CONDITION_CHOICES = (
    (CONDITION_GOOD, 'Good'),
    (CONDITION_DEFECTIVE, 'Defective'),
    (CONDITION_POOR, 'Poor'),
    (CONDITION_OUT_OF_SERVICE, 'Out of service'),
)


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
        return self.name + ' (' + self.category.name + ')'


class Item(models.Model):
    article = models.ForeignKey(Article)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=1,
                             choices=STATE_CHOICES,
                             default=STATE_AVAILABLE)
    condition = models.CharField(max_length=1,
                                 choices=CONDITION_CHOICES,
                                 default=CONDITION_GOOD)

    def __str__(self):
        return self.article.name + ' - ' + self.name

    def is_available(self):
        return self.state == STATE_AVAILABLE

    def get_state(self):
        for s in STATE_CHOICES:
            if self.state == s[0]:
                return s[1]
        return STATE_AVAILABLE

    def get_condition(self):
        for c in CONDITION_CHOICES:
            if self.condition == c[0]:
                return c[1]
        return CONDITION_GOOD


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name',
              'description',
              'main_category']


class ArticleAdmin(admin.ModelAdmin):
    fields = ['category',
              'name',
              'description']


class ItemAdmin(admin.ModelAdmin):
    fields = ['article',
              'name',
              'description',
              'state',
              'condition']

# Register class on Admin module
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Item, ItemAdmin)
