"""测试爬取请假学生"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import tempfile
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile


def main():
    """主函数"""
    # 登录链接、用户名、密码、目标链接
    login_url = 'https://www.12kcool.com/#/102064'
    un = 'admin'
    pwd = 'Ffkj-102064'
    target_url = 'https://www.12kcool.com/approve/#/approve/studentManage/approve'

    # 浏览器配置
    firefox_options = Options()
    firefox_options.add_argument('-profile')
    firefox_options.add_argument('/root/snap/firefox/common/.mozilla/firefox')

    # 为非root用户创建一个有写权限的临时用户数据目录
    user_data_dir = tempfile.mkdtemp()
    firefox_options.add_argument(f'--user-data-dir={user_data_dir}')

    # 继续配置
    firefox_options.add_argument('--headless')
    firefox_options.add_argument('--disable-gpu')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--disable-dev-shm-usage')

    # 打开浏览器，进入登录页面
    b = webdriver.Firefox(options=firefox_options, service=Service('/root/Downloads/geckodriver'))
    b.get(login_url)
    time.sleep(1)

    # 输入用户名、密码
    b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/div[1]/input').send_keys(un)
    b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/div[2]/input').send_keys(pwd)

    # 输入验证码
    cap_str = input('请输入看到的验证码')
    b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/div[3]/input').send_keys(cap_str)

    # 点击登录
    b.find_element(by=By.XPATH, value='//*[@id="app"]/section/main/div/div[2]/button').click()

    # 进入目标页面
    time.sleep(1)
    b.get(target_url)
    time.sleep(1)

    # 点击导出按钮
    b.find_element(by=By.XPATH, value='//*[@id="app"]/section/section/main/div/div/div[3]/div[2]/'
                                      'div/div/div/div[2]/div[1]/div/div[2]/button[3]').click()

    # 退出浏览器
    b.quit()


if __name__ == '__main__':
    main()
