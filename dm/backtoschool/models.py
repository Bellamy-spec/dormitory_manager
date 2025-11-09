from django.db import models
import copy


# Create your models here.
class Task(models.Model):
    """任务模型"""
    # 发布日期及字符串表示
    date = models.DateField(auto_now_add=True)
    date_str = models.CharField(max_length=10)

    # 包含年级
    grade_include = models.CharField(max_length=10)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.date_str


class Class(models.Model):
    """班级模型"""
    # 班级名称
    name = models.CharField(max_length=5)

    # 所属任务
    task = models.ForeignKey(Task, on_delete=models.CASCADE)

    # 所属年级字符串表示
    grade = models.CharField(max_length=5)

    # 应到人数
    total = models.IntegerField(default=0)

    # 请假学生字符串表示
    absent_students = models.CharField(max_length=100, default='无')

    # 实到人数
    come = models.IntegerField(default=0)

    # 是否已提交
    done = models.BooleanField(default=False)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name


class Student(models.Model):
    """学生模型"""
    # 姓名，宿舍及性别
    name = models.CharField(max_length=5)
    dorm = models.CharField(max_length=10)
    gender = models.CharField(choices=(('男', '男'), ('女', '女')), default='男',
                              max_length=2)

    # 所属班级
    _class = models.ForeignKey(Class, on_delete=models.CASCADE)

    # 请假原因及预计返校时间
    reason = models.CharField(max_length=100)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.name

    def deep_clone(self):
        """深拷贝对象实例"""
        clone_kwargs = copy.deepcopy(self.__dict__)

        # 取出不需要的键值对
        del clone_kwargs['_state']
        del clone_kwargs['id']

        # 新建实例
        clone = Student(**clone_kwargs)
        clone.save()
        return clone
