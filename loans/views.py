from loans.models import Article, Item
from django.shortcuts import render, get_object_or_404

def index(request):
    articles = Article.objects.all().order_by('-category')[:5]
    context = {'articles' : articles}
    return render(request, 'index.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    items = Item.objects.all().order_by('-name')
    context = {
        'article' : article,
        'items' : items}
    return render(request, 'article.html', context )

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    context = {'item', item}
    return render(request, 'item.html', context)
