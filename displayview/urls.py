from django.contrib import admin
from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', ArticleDetailView.as_view(), name='article-detail'),
   
]


