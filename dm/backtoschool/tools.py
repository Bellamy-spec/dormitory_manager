"""一些方便调用的工具"""
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import base64
from urllib3.exceptions import MaxRetryError
import time
import json


class DataTool:
    """数据工具类"""
    def __init__(self):
        """初始化类的属性"""
        # 年级与数字对应关系字典
        self.grade_num = {'高一': 1, '高二': 2, '高三': 3}

        # 匹配数字
        self.num_regex = re.compile(r'\d+')

        # 此项目的管理员
        self.super_users = ['李宪伟', 'zz106dyc']

        # 可以操作上报数据的用户
        self.operators = self.super_users + ['headteacher']

        # 运行着的无头浏览器，默认不打开
        self.b = None

        # 当前验证码字符串
        self.current_captcha_str = ''

        # 验证码试验次数限制
        self.tr = 0
        self.max_tr = 5

    def get_class_num(self, cs):
        """根据班级名称得出年级班级数字二元组"""
        cs_num = int(self.num_regex.findall(cs)[0])
        return self.grade_num[cs[:2]], cs_num

    def refresh_browser(self):
        """刷新浏览器"""
        # 关闭可能已存在的浏览器
        try:
            self.b.quit()
        except AttributeError:
            pass

        # 打开新的浏览器
        if os.name == 'nt':
            driver_path = ChromeDriverManager().install()
        else:
            driver_path = '/root/dormitory_manager/test/chromedriver-linux64/chromedriver'

        # 浏览器配置
        chrome_options = Options()
        chrome_options.add_argument('--headless=new')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')

        # 打开浏览器
        self.b = webdriver.Chrome(options=chrome_options, service=Service(driver_path))

    def get_captcha_str(self):
        """获取验证码二进制字符串"""
        # 进入登录页面
        login_url = 'https://www.12kcool.com/#/102064'
        self.b.get(login_url)

        # 获取验证码图像
        captcha_ele = self.b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/div[4]/img')
        captcha_binary = captcha_ele.screenshot_as_png
        captcha_binary = base64.b64encode(captcha_binary)
        captcha_str = captcha_binary.decode(encoding='utf-8')
        self.current_captcha_str = captcha_str

    def try_to_login(self, captcha):
        """利用所给的验证码尝试登录，并返回状态码"""
        # 记录试验次数
        self.tr += 1

        # 用户名、密码
        un = 'admin'
        pwd = 'Ffkj-102064'

        try:
            # 依次输入
            self.b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]'
                                                 '/div[1]/input').send_keys(un)
            self.b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]'
                                                 '/div[2]/input').send_keys(pwd)
            self.b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]'
                                                 '/div[3]/input').send_keys(captcha)

            # 点击登录
            self.b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/button').click()
        except AttributeError:
            # 重试
            return 2
        except MaxRetryError:
            # 也重试
            return 2
        else:
            time.sleep(2)

        # 判断是否成功登入
        if '登录' in self.b.page_source:
            # 未成功登录，返回验证码错误提示
            return 1
        else:
            # 成功登录，记录正确的验证码
            captcha_str = self.current_captcha_str
            bank_path = os.path.join('media', 'captcha_bank.json')

            # 首次使用确定文件存在
            if not os.path.exists(bank_path):
                # print('首次创建！')
                with open(bank_path, 'w', encoding='utf-8') as ff:
                    ff.write(json.dumps({}))

            with open(bank_path, encoding='utf-8') as cfi:
                captcha_bank_ds = cfi.read()

            try:
                captcha_bank_dict = json.loads(captcha_bank_ds)
            except json.JSONDecodeError:
                # 出现未知原因错误，跳过记录验证码，直接显示获取结果
                pass
            else:
                if captcha_str not in captcha_bank_dict.keys():
                    captcha_bank_dict[captcha_str] = captcha
                    with open(bank_path, 'w', encoding='utf-8') as cfo:
                        cfo.write(json.dumps(captcha_bank_dict))

            # 退出浏览器
            time.sleep(2)
            self.b.quit()

            return 0
