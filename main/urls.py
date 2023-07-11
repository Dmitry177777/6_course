from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

from main.apps import MainConfig

app_name = MainConfig.name





urlpatterns = [
    path('', index.as_view(), name="index"),

    path('blog/', BlogListView.as_view(), name='blog_list'),

    path('blog_item/<str:slug>/', BlogDetailView.as_view(), name='blog_item'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),

]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)