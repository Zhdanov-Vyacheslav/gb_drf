"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include, re_path

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact

from project.views import ProjectModelLimitedViewSet
from todo_notes.views import TODO_NoteModelLimitedViewSet
from user.views import UserModelLimitedViewSet

schema_view = get_schema_view(
    Info(
        title='TODO Notes',
        default_version='1.0',
        description='description',
        license=License(name='MIT'),
        contact=Contact(email='info@todonotes.com')
    )
)

router = DefaultRouter()
router.register('users', UserModelLimitedViewSet)
router.register('projects', ProjectModelLimitedViewSet)
router.register('notes', TODO_NoteModelLimitedViewSet)

urlpatterns = [
    re_path(r'swagger(?P<format>\.json|\.yaml)', schema_view.without_ui()),
    path('swagger/ui/', schema_view.with_ui()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token)
]
