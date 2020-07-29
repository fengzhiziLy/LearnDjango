from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db.models import Q

# Create your views here.
from django.views import View
from projects.models import Projects


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

    # def get(self, request, pk):
    #     # 使用request.GET获取查询字符串参数，返回的是一个类字典对象，支持字典中的所有操作
    #     # 使用request.GET.getlist('user') 可以获取多个相同key值的参数
    #     datas = {
    #         "name": "疯子",
    #         "age": 20
    #     }
    #     return JsonResponse(data=datas, safe=False)
    #     return HttpResponse("<h1>GET请求：hello,Python</h1>")

    def get(self, request):
        # 创建数据 方法一
        # 创建模型类对象
        # one_obj = Projects(name='这是一个牛逼项目520', tester='apple', leader='bai', programer='小白', publish_app='这是一个厉害的应用', desc='无描述')
        # one_obj.save()  # 保存
        # 方法二
        # Projects.objects.create(name='这是一个牛逼项目222', tester='python', leader='风', programer='疯子', publish_app='这是一个厉害的应用', desc='无描述')
        # 获取一个数据的所有记录
        # QuerySet查询集，相当于一个列表(存放所有项目对象的列表)
        # Projects.objects.all()

        # 获取某一个指定的记录 get方法只能返回一条记录，如果返回多条记录或记录不存在，会抛出异常
        # get方法的参数往往为主键或唯一键
        # one_project = Projects.objects.get(id=7)
        # 获取某一些记录 filter() exclude() 使用特定的过滤方法
        # 使用filter返回的是满足条件之后的QuerySet leader__contains类似于模糊查询
        qs = Projects.objects.filter(leader__contains='bai')

        # 关联查询
        gs = Projects.objects.filter(interfaces__name='登录接口')
        # 比较查询
        ds = Projects.objects.filter(id__gte=2)
        # 逻辑关系：多个条件查询,如果给filter指定多个条件，那么条件之间是与的关系
        # ls = Projects.objects.filter(leader='风', name__contains='牛逼')
        # 如果使用Q变量指定多个条件，那么条件之间是或的关系
        ls = Projects.objects.filter(Q(leader='风') | Q(name__contains='牛逼'))

        # 查询集的操作 相当于一个列表，支持列表中的大多数操作(通过数字索引获取值，正向切片，for)
        # 查询集是对数据库操作的一种优化，查询集会缓存结果，支持惰性查询，还支持链式操作
        ll = Projects.objects.filter(leader__contains='bai').filter(tester='apple')

        # 更新操作
        one_project = Projects.objects.get(id=1)
        one_project.leader = '风之子'
        one_project.save()

        # 删除操作
        # delete_project = Projects.objects.filter(name__contains='222')
        # get_project = delete_project.first()
        # get_project.delete()

        # 排序操作 在字段名前面-代表从大到小排序
        sort = Projects.objects.filter(id__gte=2).order_by('-name', 'publish_app')
        return HttpResponse(sort)

    def post(self, request):
        # 使用request.POST['name']获取www-form表单参数
        # json格式的数据存放在body中，可以使用request.body获取
        # 上传文件，可以使用request.FILES获取
        import json
        one_str = request.body.decode('utf-8')
        one_dict = json.loads(one_str)
        print(one_dict['name'])
        return HttpResponse("<h1>POST请求：hello,Python</h1>")

    def delete(self, request):
        return HttpResponse("<h1>DELETE请求：hello,Python</h1>")

    def put(self, request):
        return HttpResponse("<h1>PUT请求：hello,Python</h1>")

