from django.contrib import admin

# Register your models here.

from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time')

admin.site.register(Article, ArticleAdmin)


