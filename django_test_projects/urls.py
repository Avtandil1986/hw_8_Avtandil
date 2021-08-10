"""django_test_projects URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products import views

urlpatterns = [

                  path('admin/', admin.site.urls),
                  path('hello/', views.hello_world_view),
                  path('activate/<str:code>/', views.activate),
                  path('', views.main_page_view),
                  path('add_product/', views.add_product),
                  path('logout/', views.logout),
                  path('login/', views.login),
                  path('register/', views.register),
                  path('search/', views.search),
                  path('javascript/', views.javascript),
                  path('products/<int:product_id>/', views.product_item_view)
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
