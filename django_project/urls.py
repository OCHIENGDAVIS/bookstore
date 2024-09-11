from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='pages')),
    path('accounts/', include('allauth.urls')),
    path('books/', include('books.urls', namespace='books'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
