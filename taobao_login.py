# -*- coding: utf-8 -*-
from selenium import webdriver
# 导入显式等待类
from selenium.webdriver.support.ui import WebDriverWait
# 导入期望场景类
from selenium.webdriver.support import expected_conditions as EC
# 导入By类
from selenium.webdriver.common.by import By
# 导入异常类
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException
# 导入模拟鼠标操作包
from selenium.webdriver.common.action_chains import ActionChains
import time


# 登录界面
driver = webdriver.Chrome()
driver.get('https://login.taobao.com/')
wait = WebDriverWait(driver, 10, 0.2)
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="J_QRCodeLogin"]/div[5]/a[1]')))
    driver.maximize_window()
except TimeoutException as e:
    print(e)
except NoSuchElementException as e:
    print(e)
except Exception as e:
    print(e)

# 进入账户密码模式
driver.find_element_by_xpath('//*[@id="J_QRCodeLogin"]/div[5]/a[1]').click()
# 输入账号
driver.find_element_by_id('TPL_username_1').send_keys('xxxxxxxxxx')
# 输入密码
driver.find_element_by_id('TPL_password_1').send_keys('xxxxxxxxxx')
# 拖动滑块
dragger = driver.find_element_by_id('nc_1_n1z')
action_chains = ActionChains(driver)
action_chains.drag_and_drop_by_offset(dragger, 300, 0).perform()

# 缓慢移动滑块，提升成功率，但效果并不显著
# action_chains.click_and_hold(dragger).perform()  #鼠标左键按下不放
# for index in range(150):
#     action_chains.move_by_offset(2, 0).perform() #平行移动鼠标
#     action_chains.reset_actions()
#     time.sleep(0.1)  #等待停顿时间
# action_chains.release() # 释放鼠标

# 延时2秒，便于显示滑动成功失败状态文字
time.sleep(2)

# 设置验证通过标志
flag = 1
try:
    assert '验证通过' in driver.page_source
except Exception as e:
    flag = 'move failed'

# 登录
if flag != 1:
    print(flag)
else:
    print('move success')
    driver.find_element_by_id('J_SubmitStatic').click()


