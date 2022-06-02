from django.contrib import admin
from django.urls import path

from . import views


app_name = 'user_auth'


from django.conf import settings # for imgae/media
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_in/', views.log_in, name='log_in'),
    path('log_out/', views.log_out, name='log_out'),
    path('profile/', views.profile, name='profile'),
    path('user_profile_change/', views.user_profile_change, name='user_profile_change'),
    path('password/', views.password_change , name='password_change'),
    path('add_pro_pic/', views.add_pro_pic, name='add_pro_pic'),
    path('change_pro_pic/', views.change_pro_pic, name='change_pro_pic')

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
