from django.contrib import admin
from .models import Category,Post,Tag,Contact
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('status','tags')
    list_display = ('title','status','publication_date','category','author')

class TagAdmin(admin.ModelAdmin):
   prepopulated_fields = {"slug": ("title",)}

# #I can put this code inside the class but then we repet our self
# class SlugAdmin(admin.ModelAdmin):
#     prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Contact)