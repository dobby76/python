from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# 크롬브라우저 실행
driver = webdriver.Chrome()
# 주소 접속
driver.get("https://www.naver.com")

p = driver.find_element(By.TAG_NAME, 'p')
print("p태그 첫번째 요소 가져옴")
print(p)
print(type(p))
print(p.text)