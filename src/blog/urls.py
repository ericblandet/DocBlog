from django.urls import path
from .views import article, index

urlpatterns = [
    path('index/', index, name="blog-index"),
    path('article-<str:article_id>', article, name="blog-article")
]
