"""prouni URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers, serializers, viewsets

from analytics.models import UfCampus


class UfCampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = UfCampus
        fields = ['uf', 'total_campus']

class UfCampusViewSet(viewsets.ModelViewSet):
    queryset = UfCampus.objects.all()
    serializer_class = UfCampusSerializer

router = routers.DefaultRouter()
router.register(r'uf-campus', UfCampusViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
