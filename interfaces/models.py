from django.db import models

# Create your models here.


# 一个项目中有多个接口，那么需要在多的一侧创建外键
class Interfaces(models.Model):
    name = models.CharField(verbose_name='接口名称', max_length=200, unique=True, help_text='接口名称')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)
    # 第一个参数为关联的模型路径(应用名.模型类)或是模型类
    # 第二个参数设置的是，当父表删除之后，该字段的处理方式 CASCADE-->子表也会被删除 SET_NULL-->当前外键值会被设置为None，null=True
    # PROJECT---> 会报错   SET_DEFAULT---> 设置默认值，同时需要指定默认值，null=True
    project = models.ForeignKey('projects.Projects', on_delete=models.CASCADE, verbose_name='所属项目', help_text='所属项目')

    # 定义子类Meta，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_interfaces'
        # 会在admin站点中，显示一个更人性化的表面
        verbose_name = '接口'
        verbose_name_plural = '接口'

    def __str__(self):
        return self.name

