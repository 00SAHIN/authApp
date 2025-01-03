from django.urls import path
from home.views import home, contact, about, success_page
from vege.views import login_page, logout_page, receipes,delete_receipe, register_page,update_receipe
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('receipes/', receipes, name='receipes'),
    path('', home, name='home'),
    path('delete_receipe/<id>/', delete_receipe, name="delete_receipe"),
    path('update_receipe/<id>/', update_receipe, name="update_receipe"),
    path('contact/', contact, name='contact'),
    path('about/', about, name='about'),
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name= 'register_page'),
    path('success_page/', success_page, name='success_page'),
    path('logout/', logout_page,name='logout_page'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
