
from django.urls import path
from . import views
#from django.views.generic import TemplateView



urlpatterns = [

    path('',views.index,name='index'),
    path('categories/<slug:category_slug>',views.category,name='categories'),
    path('tags/<slug:tag_slug>',views.tags,name='tags'),
    path('postDetails/<slug:post_slug>',views.postDetails,name='postdetails'),
    path('contant/',views.Contant,name='contant'),
    path('contant/success/',views.Contantsuccess,name='contantsuccess'),
    

] 