from django.contrib import admin
from .models import Article, Comment


class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]
    list_display = [
        'title',
        'author',
        'date'
    ]

admin.site.register(Comment)
