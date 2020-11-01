from django.urls import path
from . import views
from .views import ArticleWeekArchiveView
from weekview.views import first


urlpatterns = [
    path('',views.first,name='first'),
    # Example: /2012/week/23/
    path('<int:year>/week/<int:week>/',ArticleWeekArchiveView.as_view(),
         name="archive_week"),
]


# http://127.0.0.1:8000/2020/week/25/
# admin details 
#     user admim
#     pass admim
