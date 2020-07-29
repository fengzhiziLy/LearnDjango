from django.urls import path
# from projects.views import index
from .views import index
from projects import views


# 每一个应用(模块)会维护一个子路由(当前应用的路由信息)
# 也是从上到下进行匹配，能匹配上，则执行path函数第二个参数指定的视图
urlpatterns = [
    # path('index', index)
    # 如果为类视图，path第二个参数为类视图名.as_view()
    path('', views.IndexView.as_view()),
    # path('<int:pk>/', views.IndexView.as_view())  # int为路径参数类型转换器 :左边为转换器，右边为参数别名
    # 转换器类型：int slug uuid
    # url路径中的参数
]


