from django.contrib import admin
from django.urls import path
from main.views import MainView, Thanks, main, order, pets_list
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order/', order, name='order'),
    path('pets_list/', pets_list, name='pets_list'),
    path('thanks/', Thanks.as_view(), name='thanks'),
    path('', MainView.as_view(), name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

