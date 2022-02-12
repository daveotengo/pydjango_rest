"""pydjango_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from rest_framework.urlpatterns import format_suffix_patterns
from webapp import views
from webapp.views import EmployeeViewSet

router= DefaultRouter()
router.register('employee',EmployeeViewSet,basename='employee')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('employee', views.employee.as_view()),
    path('employee/<int:pk>', views.employeeById.as_view()),
    path('generic/employee/<int:id>', views.GenericApiView.as_view()),

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

]
