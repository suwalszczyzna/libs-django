from django.urls import path, include
from rest_framework import routers
from .views import site_meta_info, site_favicon, TagList, LinkList

app_name = "api"

router = routers.DefaultRouter()
router.register('link', LinkList, basename='link')
router.register('tag', TagList, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
    path('service/site_info/', site_meta_info),
    path('service/site_favicon/', site_favicon),
]
