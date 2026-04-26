from django.contrib import admin
from django.urls import include, path
from . import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls', namespace='blog')),
    path('posts/', include('blog.urls', namespace='blog')),
    path('category/', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='pages')),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
