# from rest_framework.serializers import ModelSerializer
# from projects.models import Projects
#
#
# class ProjectModelSerializer(ModelSerializer):
#     class Meta:
#         model = Projects
#         fields = "__all__"

from rest_framework import serializers


# 1.继承Serializer类或子类
class ProjectSerializer(serializers.Serializer):
    # 创建项目序列化器类
    # label相当于verbose_name
    # 需要输出哪些字段，那么在序列化器中就定义哪些字段
    # read_only=True指定该字段只能进行序列化输出
    # 定义的序列化器字段，默认既可以进行序列化输出，也可以进行反序列化输入
    # write_only=True指定该字段只能进行反序列化输入
    id = serializers.IntegerField(label='ID', read_only=True)
    name = serializers.CharField(label='项目名称', max_length=200, help_text='项目名称', write_only=True)
    leader = serializers.CharField(label='负责人', max_length=50, help_text='负责人')
    tester = serializers.CharField(label='测试人员', max_length=50, help_text='测试人员')
    programer = serializers.CharField(label='开发人员', max_length=50, help_text='开发人员')
    publish_app = serializers.CharField(label='发布应用', max_length=50, help_text='发布应用')
    desc = serializers.CharField(label='简要描述', allow_null=True, allow_blank=True, default='', help_text='简要描述')
