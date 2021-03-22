"""test_bigbox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from bigbox.views import box, box_id, redireccion, activity, activity_id, box_slug

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redireccion, name=''),
    path('box/', box, name='box' ),
    path('box/<int:id>/', box_id, name="box_id"),
    path('box/<slug>/', box_slug, name='box_slug'),
    path('box/<int:id>/activity/', activity, name='activity'),
    path('box/<int:id>/activity/<int:activity_id>/', activity_id, name='actividad'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
