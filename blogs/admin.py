from django.contrib import admin
from blogs.models import Blogs


class BlogsData(admin.ModelAdmin):
    list_display = ("title", 'category',"description", "date", "author", "content")


admin.site.register(Blogs, BlogsData)


# Register your models here.
