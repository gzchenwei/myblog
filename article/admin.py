from django.contrib import admin

# Register your models here.

from article.models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_time','author','update_time')
#    class Media:
#        js = (
#            'js/editor/kindeditor-4.1.7/kindeditor-all.js',
#            'js/editor/kindeditor-4.1.7/lang.zh_CN.js',
#            'js/editor/kindeditor-4.1.7/config.js',
#        )

admin.site.register(Article, ArticleAdmin)




