from django.contrib import admin
from .models import Category, Article, Comment


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_title_length']
    list_display_links = ['title']

    def get_title_length(self, article):
        return len(article.title)


admin.site.register(Category)

admin.site.register(Article, ArticleAdmin)

admin.site.register(Comment)
