"""一些方便调用的工具类"""
import pytz


class DataTool:
    def __init__(self):
        # 部门分类
        self.departments = (
            ('高一', '高一'),
            ('高二', '高二'),
            ('高三', '高三'),
            ('美术', '美术'),
            ('体音', '体音'),
            ('行管', '行管'),
        )

        # 项目管理员
        self.managers = ['zz106dyc', '李国红']

        # 时区设置为东八区北京时间
        self.tz = pytz.timezone('Etc/GMT-8')
