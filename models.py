from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField
from django.db.models.deletion import CASCADE

from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
STATUS_CHOICES = (
    ('draft','Dradt'),
    ('published','Published')
)


class Category(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title')
    slug = models.SlugField(max_length=150 ,unique=True)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('categories',args=[self.slug])
    def __str__(self):
        return f'{self.title}'

class Tag(models.Model):
    title = models.CharField(max_length=50,verbose_name='Title')
    slug = models.SlugField(max_length=100 ,unique=True)
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags',args=[self.slug])
    def __str__(self):
        return f'{self.title}'

class Post(models.Model):
    title = models.CharField(max_length=120,verbose_name='Title')
    slug = models.SlugField(unique=True)
    status = models.CharField(choices=STATUS_CHOICES,default='draft',max_length=10,verbose_name='Status')
    publication_date = models.DateTimeField(verbose_name='Created')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='Category')
    picture = models.ImageField(upload_to='uploads/%Y/%m/%d/',verbose_name='Picture',blank=True,null=True)
    #picture = ResizedImageField(crop=['top', 'left'],quality=100,size=[100, 100],upload_to='uploads/%Y/%m/%d/',verbose_name='Picture',blank=True,null=True)

    content = RichTextUploadingField(verbose_name='Content')
    author =  models.CharField(max_length=30,default='Anonymous',verbose_name='Author')
    tags = models.ManyToManyField(Tag)
    likes = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def get_absolute_url(self):
        return reverse('postdetails',args=[self.slug])
    def __str__(self):
        return f'{self.title}'

class Contact(models.Model):
    name = models.CharField(max_length=150,verbose_name='Name')
    email = models.EmailField()
    message_date = models.DateField()
    message = models.TextField(max_length=3000)

    def __str__(self) -> str:
        return self.name + self.email
        







