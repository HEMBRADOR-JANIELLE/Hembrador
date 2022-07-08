"""maiksi"""

from django.contrib import admin
from django.urls import path
from django.urls import re_path as url
from aesys import views as aesys_views
from aesys import urls as aesys_urls
from django.conf.urls import include

urlpatterns = [
    url(r'^$', aesys_views.homepage, name='home'),
    url(r'^aesys/', include(aesys_urls)),
    url('admin/', admin.site.urls),
]



