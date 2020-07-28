from django.db import models

# Create your models here.
# 每一个应用下的数据库模型类，需要在当前目录下的models.py中定义
# 有一个数据库模型类相当于一个数据表(Table)，并且需要继承models.Model或Model的子类


class Person(models.Model):
    """创建Person类"""
    # makemigrations projects   migrate projects --> Tools--> Run manage.py Task
    # 一个类属性，相当于数据库表中的一个字段
    # 默认会创建一个自动递增的ID主键
    # 默认创建的数据库名为 应用名_数据库模型类(小写)
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        # 会在admin站点中，显示一个更人性化的表面
        verbose_name = '人类'
        verbose_name_plural = '人类'


class Projects(models.Model):
    """创建Projects模型类"""
    # verbose_name用于设置人性化的字段名
    # help_text 用于api文档中的一个中文名称
    name = models.CharField(verbose_name='项目名称', max_length=200, unique=True, help_text='项目名称')
    leader = models.CharField(verbose_name='负责人', max_length=50, help_text='负责人')
    tester = models.CharField(verbose_name='测试人员', max_length=50, help_text='测试人员')
    programer = models.CharField(verbose_name='开发人员', max_length=50, help_text='开发人员')
    publish_app = models.CharField(verbose_name='发布应用', max_length=100, help_text='发布应用')
    # null设置数据库中此字段允许为空，blank用于设置前端可以不传递，default设置默认值
    desc = models.TextField(verbose_name='简要描述', help_text='简要描述', blank=True, default='', null=True)

    # 定义子类Meta，用于设置当前数据模型的元数据信息
    class Meta:
        db_table = 'tb_projects'
        # 会在admin站点中，显示一个更人性化的表面
        verbose_name = '项目'
        verbose_name_plural = '项目'

    def __str__(self):
        return self.name


