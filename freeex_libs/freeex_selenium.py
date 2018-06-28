from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from time import sleep
import os 

class FreeexSelenium():
	def __init__(self):
		self.driver = webdriver.Chrome()
		self.base_url = os.getenv("BASE_URL")
		self.user_mail = os.getenv("USER_MAIL")
		self.user_pass = os.getenv("USER_PASS")

	def login(self):
		driver = self.driver
		driver.get("{}/login".format(self.base_url))

		email = driver.find_element_by_id('email')
		email.send_keys(self.user_mail)

		password = driver.find_element_by_id('password')
		password.send_keys(self.user_pass)

		button = driver.find_element_by_id('btn-normal')
		button.click()

	def regist_newsletter(self, record, enable_save_mode = True):
		driver = self.driver
		driver.get("{}/admin/newsletter/create".format(self.base_url))
		
		published_at = driver.find_element_by_id('published_at')
		published_at.send_keys(Keys.ESCAPE)
		published_at.clear()
		published_at.send_keys(record['date'])
		published_at.send_keys(Keys.ENTER)

		title = driver.find_element_by_id('title')
		title.send_keys(record['title'])

		tab = driver.find_element_by_id('tab-plain')
		tab.click()

		# テキストが長文の場合、send_keysでは、時間がかかるので、JavaScriptで対応
		plainTextArea = driver.find_element_by_id('plainTextArea')
		driver.execute_script("arguments[0].value = arguments[1];",
plainTextArea, record['body']);

		# JavaScriptでのテキスト入力では、テキストが認識されなかった
		# スペースキーとバックスペースを送信して元のテキストへを変更せずに認識させる
		plainTextArea.send_keys(' ')
		plainTextArea.send_keys(Keys.BACK_SPACE)

		tab = driver.find_element_by_id('tab-visual')
		tab.click()

		# 念のため、1秒待機
		sleep(3)

		button = driver.find_element_by_id('btn-submit')
		button.click()

	def quite(self):
		self.driver.close()
		self.driver.quit()