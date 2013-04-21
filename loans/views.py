from loans.models import Category, Article, Item
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    context = {}
    return render(request, 'index.html', context)

def article_index(request):
    articles = Article.objects.all().order_by('-category')
    context = {
        'articles' : articles
    }
    return render(request, 'article_index.html', context)

def article_add(request):
    article = Article()
    article.description = ''
    categories = Category.objects.all().order_by('-name')
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'article_add.html', context )

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    items = Item.objects.all().order_by('-name')
    context = {
        'article' : article,
        'items' : items,
    }
    return render(request, 'article.html', context )

def article_save(request):
    error = False
    error_message = ''
    fields = []
    try:
        article = Article()
        article.name = request.POST['name']
        article.description = request.POST['description']

        if len(article.name) == 0:
            error = True
            error_message = "Some fields are required"
            fields.append('Name')

        article.category = Category.objects.get(id=request.POST['category'])

    except(KeyError, Category.DoesNotExist):
        error = True
        error_message = "Some fields are required"
        fields.append('Category')

    if error:
        categories = Category.objects.all().order_by('-name')
        context = {
            'article': article,
            'error_message': error_message,
            'fields' : fields,
            'categories': categories,
        }
        return render(request, 'article_add.html', context )
    else:
        article.save()
        return HttpResponseRedirect(reverse('article', args=(article.id,)))

def item_add(request):
    context = {}
    return render(request, 'item_add.html', context)

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item', item,
    }
    return render(request, 'item.html', context)

