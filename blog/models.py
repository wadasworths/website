from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from DjangoUeditor.models import UEditorField
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=70)
    
    content = models.TextField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    excerpt = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    STATUS_CHOICES = (
        ('draft','草稿'),
        ('published','已发布'),
        )
    
    content = UEditorField('内容', height=300, width=800,max_length=1024000000000,
                           default=u'', blank=True, imagePath="images/",
                           toolbars='besttome', filePath='files/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
