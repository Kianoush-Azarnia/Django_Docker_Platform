from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from docker_app.views import AppViewSet, RunViewSet

router = routers.DefaultRouter()
router.register(r'apps', AppViewSet, basename='app')
router.register(r'runs', RunViewSet, basename='run')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/?$', include(router.urls)),
    re_path(r'^api/apps/?$', AppViewSet.as_view({'get': 'list', 'post': 'create'}), name='app-list'),
    re_path(r'^api/apps/(?P<pk>\d+)/?$', AppViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='app-detail'),
    re_path(r'^api/apps/(?P<pk>\d+)/runs/?$', RunViewSet.as_view({'post': 'create', 'get': 'list'}), name='run-app'),
    re_path(r'^api/apps/(?P<pk>\d+)/runs/(?P<run_pk>\d+)/?$', RunViewSet.as_view({'get': 'retrieve'}), name='run-detail')
]

urlpatterns += router.urls
