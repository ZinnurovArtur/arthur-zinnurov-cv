from .views import *
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = \
    [
        path('',portfolio_index,name ='porfoliomy'),
        path('<str:filepath>/',download_file)

     ]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+=staticfiles_urlpatterns()