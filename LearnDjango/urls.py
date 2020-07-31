"""LearnDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from projects.views01 import index

# 全局路由配置
# 列表中的一个元素，就代表一个路由
# 从上到下进行匹配，如果能匹配上，Django会导入和调用path函数第二个参数指定的视图或者去子路由中匹配
# 如果匹配不上，会自动抛出一个404错误
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', index)
    # path('projects/', include('projects.urls'))
    path('', include('projects.urls')),
    # path('api/', include('rest_framework.urls'))
]
