import xadmin
from .models import Article, Category, Tag
# Register your models here.


class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name'] 

class TagAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name'] 

class ArticleAdmin(object):
    list_display = ['title', 'created_time', 'category', 'tags', 'author']
    search_fields = ['title', 'category', 'tags', 'author']
    list_filter = ['title', 'category', 'tags', 'author'] 

xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Article, ArticleAdmin)