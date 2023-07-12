from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from docker_app.views import AppViewSet, RunViewSet

router = routers.DefaultRouter()
router.register(r'apps', AppViewSet, basename='app')
router.register(r'runs', RunViewSet, basename='run')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
    
    path('api/', include([
        re_path(r'^apps/(?P<pk>\d+)/runs/?$', RunViewSet.as_view({'post': 'create', 'get': 'list'}), name='run-app'),
        re_path(r'^apps/(?P<pk>\d+)/runs/(?P<run_pk>\d+)/?$', RunViewSet.as_view({'get': 'retrieve'}), name='run-detail'),
    ])),
]
