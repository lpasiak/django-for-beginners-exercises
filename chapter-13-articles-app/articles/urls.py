from django.urls import path
from .views import (ArticleListView,
                    ArticleDetailView,
                    ArticleUpdateView,
                    ArticleDeleteView)

urlpatterns = [
   path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
   path('<pk:int>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
   path('<pk:int>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
   path('', ArticleListView.as_view(), name='article_list')
]