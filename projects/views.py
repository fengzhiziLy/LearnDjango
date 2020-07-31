from django.http import HttpResponse, JsonResponse, Http404
from django.views import View
from projects.models import Projects
import json
from projects.serialize import ProjectSerializer
# from rest_framework.viewsets import ModelViewSet


class ProjectsList(View):
    def get(self, request):
        # 1. 从数据库中获取所有的项目信息
        project_qs = Projects.objects.all()
        # 2. 将数据库模型实例转化为字典类型(嵌套字典的列表)
        # project_list = []
        # for project in project_qs:
        #     # one_dict = {
        #     #     "name": project.name,
        #     #     "leader": project.leader,
        #     #     "tester": project.tester,
        #     #     "programer": project.programer,
        #     #     "publish_app": project.publish_app,
        #     #     "desc": project.desc
        #     # }
        #     # project_list.append(one_dict)
        #     project_list.append({
        #         "name": project.name,
        #         "leader": project.leader,
        #         "tester": project.tester,
        #         "programer": project.programer,
        #         "publish_app": project.publish_app,
        #         "desc": project.desc
        #     })
        # JsonResponse第一个参数只能为dict字典，如果要设置其他类型，需要将safe=false
        # 如果返回的是列表数据（多条数据）时，那么需要添加many=True这个参数
        serializer = ProjectSerializer(instance=project_qs, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        """新增项目接口
        1. 从前端获取json格式数据，转换为Python中的类型
        为了严谨性，需要做各种复杂的校验
        比如：是否为json、传递的项目数据是否符合要求、有些必传参数是否携带
        2. 向数据库中新增项目
        3. 将模型类对象转换为字典，然后返回
        """
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')
        # new_project = Projects.objects.create(name=python_data['name'],
        #                         leader=python_data['leader'],
        #                         tester=python_data['tester'],
        #                         programer=python_data['programer'],
        #                         publish_app=python_data['publish_app'],
        #                         desc=python_data['desc'])
        serializer = ProjectSerializer(data=python_data)
        # 校验前端输入的数据
        # 可以调用序列化器对象的is_valid方法，开始校验前端参数
        # 如果检验成功，则返回True，校验失败，返回False
        # raise_exception=True校验失败之后会抛出异常
        # 当调用is_valid方法之后，才可以调用errors属性，获取校验的错误提示(字典)
        try:
            serializer.is_valid(raise_exception=True)
            # 校验成功之后的数据可以使用validated_data属性类获取
        except Exception as e:
            return JsonResponse(serializer.errors)
        new_project = Projects.objects.create(**serializer.validated_data)
        # one_dict = {
        #     "name": new_project.name,
        #     "leader": new_project.leader,
        #     "tester": new_project.tester,
        #     "programer": new_project.programer,
        #     "publish_app": new_project.publish_app,
        #     "desc": new_project.desc
        # }
        serializer = ProjectSerializer(new_project)
        return JsonResponse(serializer.data, status=201)


class ProjectsDetail(View):
    def get_object(self, pk):
        try:
            return Projects.objects.get(id=pk)
        except Projects.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        # 1. 校验前端传递的pk(项目ID)值是否存在，类型是否正确(正整数)，在数据库中是否存在
        # 2. 获取指定pk值的项目
        project = self.get_object(pk)

        # 3. 将模型类对象转换为字典
        # one_dict = {
        #     "name": project.name,
        #     "leader": project.leader,
        #     "tester": project.tester,
        #     "programer": project.programer,
        #     "publish_app": project.publish_app,
        #     "desc": project.desc
        # }

        # 1.通过模型类对象(或者查询集)传给instance，就可以进行序列化操作
        # 2.通过序列化器ProjectSerializer对象的data属性就可以后去转化之后的字典
        serialize = ProjectSerializer(instance=project)
        return JsonResponse(serialize.data)

    def put(self, request, pk):
        # 1.校验前端传递的pk(项目ID)值是否存在，类型是否正确(正整数)，在数据库中是否存在
        project = self.get_object(pk)
        # 2.获取指定ID为pk值的项目
        project = Projects.objects.get(id=pk)
        # 3.从前端获取json格式的数据，转换为Python中的类型
        json_data = request.body.decode('utf-8')
        python_data = json.loads(json_data, encoding='utf-8')
        serializer = ProjectSerializer(data=python_data)
        try:
            serializer.is_valid(raise_exception=True)
            # 校验成功之后的数据可以使用validated_data属性类获取
        except Exception as e:
            return JsonResponse(serializer.errors)
        # 4.更新项目
        # serializer.validated_data
        project.name = serializer.validated_data['name']
        project.leader = serializer.validated_data['leader']
        project.tester = serializer.validated_data['tester']
        project.programer = serializer.validated_data['programer']
        project.publish_app = serializer.validated_data['publish_app']
        project.desc = serializer.validated_data['desc']
        project.save()
        # 5.将模型类对象转换为字典
        # one_dict = {
        #     "name": project.name,
        #     "leader": project.leader,
        #     "tester": project.tester,
        #     "programer": project.programer,
        #     "publish_app": project.publish_app,
        #     "desc": project.desc
        # }
        serialize = ProjectSerializer(instance=project)
        return JsonResponse(serialize.data, safe=False, status=201)

    def delete(self, request, pk):
        """删除项目
        1.校验前端传递的pk(项目ID)值是否存在，类型是否正确(正整数)，在数据库中是否存在
        2.获取指定ID为pk值的项目
        """
        # project = Projects.objects.get(id=pk)
        project = self.get_object(pk)
        project.delete()
        return JsonResponse(None, safe=False, status=204)


"""数据增删改差流程
增：校验请求参数-->反序列化-->保存数据-->将保存的对象序列化并返回
删：判断要删除的数据是否存在-->执行数据库删除
改：判断要修改的数据是否存在-->校验请求参数-->反序列化-->保存数据-->将保存的对象序列化并返回
查：查询数据库-->将数据序列化并返回
"""


# class ProjectViewSet(ModelViewSet):
#     queryset = Projects.objects.all()
#     serializer_class = ProjectModelSerializer
