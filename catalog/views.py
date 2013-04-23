from catalog.models import Category, Article, Item, STATE_CHOICES, STATE_AVAILABLE, CONDITION_CHOICES
from django.shortcuts import render, get_object_or_404


def index(request):
    articles = Article.objects.all().order_by('-category')
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def category_index(request):
    categories = Category.objects.all().order_by('-name')
    context = {
        'categories': categories,
    }
    return render(request, 'category_index.html', context)


def category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    subcategories = Category.objects.filter(main_category_id=category.id).order_by('-name')
    context = {
        'category': category,
        'subcategories': subcategories,
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
    error_message = []

    if(category_id == 0 or category_id == '0'):
        category = Category()
    else:
        category = get_object_or_404(Category, pk=category_id)
    category.name = request.POST['name']
    category.description = request.POST['description']

    if len(category.name) == 0:
        error = True
        error_message.append("Name is required")
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
            'categories': categories,
        }
        return render(request, 'category_add.html', context)
    else:
        category.save()
        context = {
            'category': category,
            'success_message': 'La categoria ' + category.name + ' ha sido guardada exitosamente.',
        }
        return render(request, 'category.html', context)


def category_remove(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    categories = Category.objects.all().order_by('-category')
    context = {
        'categories': categories,
        'success_message': 'La categoria ' + category.name + ' ha sido eliminada exitosamente.',
    }
    return render(request, 'category_index.html', context)


def category_article_add(request, category_id):
    article = Article()
    article.category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by('-name')
    context = {
        'article': article,
        'categories': categories,
    }
    return render(request, 'article_add.html', context)


def category_subcategory_add(request, category_id):
    category = Category()
    category.main_category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all().order_by('-name')
    context = {
        'category': category,
        'categories': categories,
    }
    return render(request, 'category_add.html', context)


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
    error_message = []
    try:
        if(article_id == 0 or article_id == '0'):
            article = Article()
        else:
            article = get_object_or_404(Article, pk=article_id)
        article.name = request.POST['name']
        article.description = request.POST['description']

        if len(article.name) == 0:
            error = True
            error_message.append("El nombre es requerido")

        article.category = Category.objects.get(id=request.POST['category'])

    except(KeyError, Category.DoesNotExist):
        error = True
        error_message.append("La categoria es requerida")

    if error:
        categories = Category.objects.all().order_by('-name')
        context = {
            'article': article,
            'error_message': error_message,
            'categories': categories,
        }
        return render(request, 'article_add.html', context)
    else:
        article.save()
        context = {
            'article': article,
            'success_message': 'El articulo ' + article.name + ' ha sido guardado exitosamente.',
        }
        return render(request, 'article.html', context)


def article_remove(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.delete()
    articles = Article.objects.all().order_by('-category')
    context = {
        'articles': articles,
        'success_message': 'El articulo ' + article.name + ' ha sido eliminado exitosamente.',
    }
    return render(request, 'index.html', context)


def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {
        'item': item,
    }
    return render(request, 'item.html', context)


def item_add(request, article_id):
    item = Item()
    item.article = get_object_or_404(Article, pk=article_id)
    articles = Article.objects.all().order_by('-name')
    context = {
        'item': item,
        'articles': articles,
        'STATE_CHOICES': STATE_CHOICES,
        'CONDITION_CHOICES': CONDITION_CHOICES,
    }
    return render(request, 'item_add.html', context)


def item_edit(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    articles = Article.objects.all().order_by('-name')
    context = {
        'item': item,
        'articles': articles,
        'STATE_CHOICES': STATE_CHOICES,
        'CONDITION_CHOICES': CONDITION_CHOICES,
    }
    return render(request, 'item_add.html', context)


def item_save(request, item_id):
    error = False
    error_message = []

    if(item_id == 0 or item_id == '0'):
        item = Item()
        item.state = STATE_AVAILABLE
    else:
        item = get_object_or_404(Item, pk=item_id)
    item.name = request.POST['name']
    item.description = request.POST['description']
    item.condition = request.POST['condition']

    if len(item.name) == 0:
        error = True
        error_message.append("El nombre es requerido")

    if len(item.condition) == 0:
        error = True
        error_message.append("La condicion es requerida")

    article_id = request.POST['article']
    if article_id != 0 and article_id != '0':
        item.article = Article.objects.get(id=article_id)
    else:
        item.article = None

    if error:
        articles = Article.objects.all().order_by('-name')
        context = {
            'item': item,
            'error_message': error_message,
            'articles': articles,
        }
        return render(request, 'item_add.html', context)
    else:
        item.save()
        article = Article.objects.get(pk=item.article.id)
        context = {
            'article': article,
            'success_message': 'El item ' + item.name + ' ha sido eliminado exitosamente.',
        }
        return render(request, 'article.html', context)


def item_remove(request, item_id):
    item = get_object_or_404(Category, pk=item_id)
    item.delete()
    article = Article.objects.get(pk=item.article.id)
    context = {
        'article': article,
        'success_message': 'El item ' + item.name + ' ha sido eliminado exitosamente.',
    }
    return render(request, 'article.html', context)
