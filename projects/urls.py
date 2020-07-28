from django.urls import path
# from projects.views import index
from .views import index
from projects import views


# 每一个应用(模块)会维护一个子路由(当前应用的路由信息)
# 也是从上到下进行匹配，能匹配上，则执行path函数第二个参数指定的视图
urlpatterns = [
    # path('index', index)
    # 如果为类视图，path第二个参数为类视图名.as_view()
    path('', views.IndexView.as_view())
]


