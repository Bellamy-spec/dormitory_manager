"""测试爬取请假学生"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    """主函数"""
    # 登录链接、用户名、密码、目标链接
    login_url = 'https://www.12kcool.com/#/102064'
    un = 'admin'
    pwd = 'Ffkj-102064'
    target_url = 'https://www.12kcool.com/approve/#/approve/studentManage/approve'

    # 浏览器配置
    chrome_options = Options()
    # chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')

    # 打开浏览器，进入登录页面
    b = webdriver.Chrome(options=chrome_options, service=Service('chromedriver-linux64/chromedriver'))
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

    # 保持页面
    # input()

    # 退出浏览器
    time.sleep(3)
    b.quit()


if __name__ == '__main__':
    main()
