from catalog.models import Category, Article, Item
from django.shortcuts import render, get_object_or_404


def index(request):
    articles = Article.objects.all().order_by('-category')
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def category_index(request):
    categories = Category.objects.all().order_by('-category')
    context = {
        'categories': categories,
    }
    return render(request, 'category_index.html', context)


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'category': category,
    }
    return render(request, 'category.html', context)


def category_add(request):
    category = Category()
    categories = Category.objects.all().order_by('-name')
    context = {
        'category': category,
        'categories': categories,
    }
    return render(request, 'category_add.html', context)


def category_edit(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by('-name')
    context = {
        'category': category,
        'categories': categories,
    }
    return render(request, 'category_add.html', context)


def category_save(request, category_id):
    error = False
    error_message = ''
    error_fields = []

    if(category_id == 0 or category_id == '0'):
        category = Category()
    else:
        category = get_object_or_404(Category, pk=category_id)
    category.name = request.POST['name']
    category.description = request.POST['description']

    if len(category.name) == 0:
        error = True
        error_message = "Some fields are required"
        error_fields.append('Name')
    main_category = request.POST['main_category']
    if main_category != 0 and main_category != '0':
        category.main_category = Category.objects.get(id=main_category)
    else:
        category.main_category = None

    if error:
        categories = Category.objects.all().order_by('-name')
        context = {
            'category': category,
            'error_message': error_message,
            'error_fields': error_fields,
            'categories': categories,
        }
        return render(request, 'category_add.html', context)
    else:
        category.save()
        context = {
            'category': category,
            'success_message': 'The category ' + category.name + ' has been added.',
        }
        return render(request, 'category.html', context)


def category_remove(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    categorys = Category.objects.all().order_by('-category')
    context = {
        'categorys': categorys,
        'success_message': 'The category ' + category.name + ' has been delete.',
    }
    return render(request, 'category_index.html', context)


def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context = {
        'article': article,
    }
    return render(request, 'article.html', context)


def article_add(request):
    article = Article()
    categories = Category.objects.all().order_by('-name')
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'article_add.html', context)


def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    categories = Category.objects.all().order_by('-name')
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'article_add.html', context)


def article_save(request, article_id):
    error = False
    error_message = ''
    error_fields = []
    try:
        if(article_id == 0 or article_id == '0'):
            article = Article()
        else:
            article = get_object_or_404(Article, pk=article_id)
        article.name = request.POST['name']
        article.description = request.POST['description']

        if len(article.name) == 0:
            error = True
            error_message = "Some fields are required"
            error_fields.append('Name')

        article.category = Category.objects.get(id=request.POST['category'])

    except(KeyError, Category.DoesNotExist):
        error = True
        error_message = "Some error_fields are required"
        error_fields.append('Category')

    if error:
        categories = Category.objects.all().order_by('-name')
        context = {
            'article': article,
            'error_message': error_message,
            'error_fields': error_fields,
            'categories': categories,
        }
        return render(request, 'article_add.html', context)
    else:
        article.save()
        context = {
            'article': article,
            'success_message': 'The article ' + article.name + ' has been added.',
        }
        return render(request, 'article.html', context)


def article_remove(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    articles = Article.objects.all().order_by('-category')
    context = {
        'articles': articles,
        'success_message': 'The article ' + article.name + ' has been delete.',
    }
    return render(request, 'index.html', context)


def item_add(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    item = Item()
    context = {
        'article': article,
        'item': item,
    }
    return render(request, 'item_add.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item.html', context)
