from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View


def index(request):  # 函数视图
    """
    index视图
    :param request，视图函数的第一个参数，是HttpResponse对象，包含前端用户的所有请求信息
    :return 必须返回一个HttpResponse对象或子对象
    """
    if request.method == 'GET':
        return HttpResponse("<h1>GET请求：hello,Python</h1>")
    elif request.method == 'POST':
        return HttpResponse("<h1>POST请求：hello,Python</h1>")
    else:
        return HttpResponse("<h1>其他请求：hello,Python</h1>")


# 类视图
class IndexView(View):
    """
    index主页类视图
    """
    # def get(self, request):
    #     # return HttpResponse("<h1>GET请求：hello,Python</h1>")
    #     datas = [
    #         {
    #             'project_name': '前横带',
    #             'leader': '可有',
    #             'app_name': 'P2P平台'
    #         },
    #         {
    #             'project_name': '探索火星',
    #             'leader': '小小',
    #             'app_name': '吊炸天项目'
    #         },
    #         {
    #             'project_name': '牛逼项目',
    #             'leader': '疯子',
    #             'app_name': '神秘应用'
    #         }
    #     ]
    #     return render(request, 'index.html', locals())

    def get(self, request):
        # 使用request.GET获取查询字符串参数，返回的是一个类字典对象，支持字典中的所有操作
        # 使用request.GET.getlist('user') 可以获取多个相同key值的参数
        return HttpResponse("<h1>GET请求：hello,Python</h1>")

    def post(self, request):
        return HttpResponse("<h1>POST请求：hello,Python</h1>")

    def delete(self, request):
        return HttpResponse("<h1>DELETE请求：hello,Python</h1>")

    def put(self, request):
        return HttpResponse("<h1>PUT请求：hello,Python</h1>")

