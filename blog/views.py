from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Article, Category, Tag
import markdown

# Create your views here.
def index(request):
    article_list = Article.objects.all().order_by('-created_time')
    category_list = Category.objects.all()

    paginator = Paginator(article_list, 2)
    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    
    return render(request, 'blog/index.html', context={'articles': articles,
        'category_list': category_list})
    
    #return render(request, 'blog/index.html', context={'article_list': article_list,
    #    'category_list': category_list})

def category(request):
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    
    return render(request, 'blog/category.html', context={'category_list': category_list,
                                                                'tag_list' : tag_list})

def about(request):
   category_list = Category.objects.all()
   return render(request, 'blog/about.html', context={'category_list': category_list})

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.content = markdown.markdown(article.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
    category_list = Category.objects.all()

    return render(request, 'blog/detail.html', context={'article': article,
        'category_list': category_list})


def archives(request):
    dates = Article.objects.datetimes('created_time', 'month', order='DESC')
    article_list = Article.objects.all().order_by('-created_time')
 
    return render(request, 'blog/archives.html', context={'dates' : dates,
                                                        'article_list': article_list})
