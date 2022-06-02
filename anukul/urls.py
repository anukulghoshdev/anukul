
from django.contrib import admin
from django.urls import path, include



from django.conf import settings # for imgae/media
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('user_auth/', include('user_auth.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
