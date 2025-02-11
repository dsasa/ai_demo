from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import post
import re
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 加载环境变量
load_dotenv()

# 设置Twitter账号信息
username = os.getenv('MY_TWITTER_USERNAME')
password = os.getenv('MY_TWITTER_PASSWORD')

# 初始化浏览器驱动
driver = webdriver.Chrome()

# 打开Twitter登录页面
driver.get("https://twitter.com/i/flow/login")

# 等待页面加载
time.sleep(2)

# 输入用户名
username_input = driver.find_element(By.NAME, "text")
username_input.send_keys(username)
username_input.send_keys(Keys.RETURN)

# 等待密码输入框加载
time.sleep(2)

# 输入密码
password_input = driver.find_element(By.NAME, "password")
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)

# 等待登录完成
time.sleep(5)

# 获取帖子内容
post_content = post.get_post_content(topic="油泼面", platform="推特")

# 过滤掉非BMP字符
post_content = re.sub(r'[^\u0000-\uFFFF]', '', post_content)

# 输入帖子内容
post_input = driver.find_element(By.CSS_SELECTOR, "div[data-testid='tweetTextarea_0']")
post_input.send_keys(post_content)
print(post_content)

time.sleep(5)  # 等待1秒，确保文本输入完成

# 等待发布按钮加载并点击
try:
    # 等待元素出现在DOM中
    post_button = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-testid='tweetButtonInline']"))
    )
    
    # 检查元素是否可见和可用
    if post_button.is_displayed() and post_button.is_enabled():
        post_button.click()
        print("帖子已发布")
    else:
        print("发布按钮不可用。")
except TimeoutException:
    print("发布按钮未找到，请检查选择器或页面结构。")


# 等待5秒后关闭浏览器
time.sleep(5)
driver.quit()