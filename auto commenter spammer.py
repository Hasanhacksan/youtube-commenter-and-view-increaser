import time
import pyautogui,time
from selenium import webdriver
from apiclient.discovery import build
from selenium.webdriver.common.keys import Keys


g='iamhacksan@gmail.com'
p='hacksan@123'
c='  very nice ggod'

url='https://www.youtube.com/watch?v=HcSEs945g_U'
driver = webdriver.Chrome(r'C:\Users\Hacksan\Desktop\mywork PYTHON\chromedriver_win32\chromedriver.exe')  
driver.get(url)
print('page loadeded sucess')


driver.implicitly_wait(5)
pyautogui.press('pagedown')
pyautogui.press('pageup')
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(5)
pyautogui.scroll(200)
pyautogui.scroll(-600)
driver.implicitly_wait(2)
cmt=driver.find_element_by_xpath('//*[@id="placeholder-area"]')
cmt.click()
print('initializing scroll')



email1=driver.find_element_by_xpath('//*[@id="identifierId"]')
email1.click()
pyautogui.typewrite(g)
pyautogui.press("enter")
print('sucessfully email entered')

driver.implicitly_wait(6)
em=driver.find_element_by_name("password").send_keys(p)
pyautogui.press("enter")
driver.implicitly_wait(30)
print('sucess!! password')



driver.implicitly_wait(5)
time.sleep(5)
pyautogui.press("enter")
pyautogui.press("pagedown")
driver.execute_script("window.scrollBy(0,800)","")
pyautogui.scroll(200)
pyautogui.press('pagedown')
time.sleep(5)
pyautogui.press('pageup')

print('loading for commenting')
time.sleep(3)
driver.execute_script("window.scrollBy(0,200)","")
pyautogui.scroll(100)
pyautogui.typewrite('enter')
pyautogui.press('tab')    
pyautogui.press('enter')   
driver.execute_script("window.scrollBy(0,200)","")
time.sleep(5)
pyautogui.press('pageup')
cmt1=driver.find_element_by_xpath('//*[@id="placeholder-area"]')
cmt1.click()
driver.implicitly_wait(2)
pyautogui.typewrite(c)
pyautogui.write(c)
pyautogui.typewrite(c)
time.sleep(1)
pyautogui.press('enter')
pyautogui.hotkey('ctrl','enter')
print('comment sucess')

pyautogui.press('f5')
time.sleep(1)
driver.execute_script("window.scrollBy(0,800)","")
pyautogui.press('pagedown')
print('refresh sucess')


'''time.slee
u=driver.get("url")
print(u)
setxt=''
while not setxt:
    try:
     setxt=driver.find_element_by_xpath('//*[@id="placeholder-area"]')
     setxt.sendkeys('nice')
    except: continue'''

'''comentbox=driver.find_element_by_xpath('//*[@id="identifierId"]')
comentbox.sendkeys(g)
comentbox.click()

comentbt=driver.find_element_by_xpath('//*[@id="submit-button"]')
comentbt.click()'''


