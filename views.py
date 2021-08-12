from django import template
import django.template
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import context, loader
from .models import Category,Post,Tag,Contact
from .forms import ContactForms
from django.utils import timezone
from django.core.paginator import Paginator
from django.db.models import Q
from authy.models import Profile
#from django.contrib.auth.models import User
# Create your views here.

def index(request):
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()

     #Search
    query = request.GET.get("q")
     
    if query:
        articles = articles.filter(
            Q(title__icontains = query) |
            Q(content__icontains = query)
        ).distinct()


    #Pagination
    paginator = Paginator(articles,2)
    #Current page
    page_number = request.GET.get('page')
    articles_paginator = paginator.get_page(page_number)

  
    
    template = loader.get_template('index.html')
    context = {
        'articles':articles_paginator,
        'categories':categories
    }
    return HttpResponse(template.render(context,request))

def category(request,category_slug):
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category,slug = category_slug)
        articles = articles.filter(category=category)
    
    template = loader.get_template('category.html')
    
    context = {
        'articles':articles,
        'categories':categories
    }
    return HttpResponse(template.render(context,request))

def postDetails(request,post_slug):
    articles = get_object_or_404(Post,slug=post_slug)
    user = request.user.id
    profile = Profile.objects.get(user__id = user)
    #For the color of the favorite button
    if profile.favorites.filter(slug=post_slug).exists():
        favorited = True
    else:
        favorited = False

    #Handle the post to add the article to user favorites
    
    if request.method == 'POST':
        if profile.favorites.filter(slug=post_slug).exists():
            profile.favorites.remove(articles)
        else:
            profile.favorites.add(articles)

    template = loader.get_template('post_details.html')
    context = {
        'articles':articles,
        'favorited':favorited
        
    }
    return HttpResponse(template.render(context,request))




def tags(request,tag_slug):
    tags = Tag.objects.all()
    articles = Post.objects.filter(status='published').order_by('-publication_date')
    categories = Category.objects.all()
    if tag_slug:
        tag = get_object_or_404(Tag,slug=tag_slug)
        articles = articles.filter(tags=tag)
    template = loader.get_template('tags.html')
    
    context = {
        'articles':articles,
        'tags':tags
    }
    return HttpResponse(template.render(context,request))

def Contant(request):
    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.message_date = timezone.now()
            form.save() 
            #There is a difference between the two:
            #In the case of HttpResponseRedirect the first argument can only be a url.
            #redirect which will ultimately return a HttpResponseRedirect can accept a model, 
            # view, or url as it's "to" argument.
            # So it is a little more flexible in what it can "redirect" to.
            return redirect('contantsuccess')
    #For the get method, we just load the form
    else:
        form = ContactForms()
    context = {
        'form' : form,
    }
    return render(request,'contant.html',context)

    #static website for the form contact

def Contantsuccess(request):
    return render(request,'contantsuccess.html',)


