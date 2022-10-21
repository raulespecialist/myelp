from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls import include
from django.conf.urls.static import static
from award.views import search_business, index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('award/', include('award.urls')),
    path('search/', search_business),
    path('', index),
]
