"""hnuapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from test1.views import home,classinfo,query_table_otsteam,building_gallery,form_ots,query_event,class_info_erjiao,class_info_shuijiao,class_info_tijiao
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^classinfo/', classinfo,name='classinfo'),
    url(r'^query_table_otsteam/', query_table_otsteam,name='query_table_otsteam'),
    url(r'^form_ots/(\d+)$', form_ots, name='form_ots'),
    url(r'^building_gallery/', building_gallery, name='building_gallery'),
    url(r'^query_event/', query_event, name='query_event'),
    url(r'^class_info_erjiao/', class_info_erjiao, name='class_info_erjiao'),
    url(r'^class_info_shuijiao/', class_info_shuijiao, name='class_info_shuijiao'),
    url(r'^class_info_tijiao/', class_info_erjiao, name='class_info_tijiao'),
    url(r'^admin/', admin.site.urls),
]
urlpatterns+=staticfiles_urlpatterns()


