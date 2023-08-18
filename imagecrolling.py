

from selenium import webdriver
import os
import urllib.request
import time
import datetime
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
browser = webdriver.Chrome(options=options)
params = {'behavior': 'allow', 'downloadPath': r'C:\Users\jewoon.woo\Downloads'}
browser.execute_cdp_cmd('Page.setDownloadBehavior', params)

def doScrollDown(whileSeconds, driver):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSeconds)
    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(1)
        if datetime.datetime.now() > end:
            break



def crawl(keywords):
    path = "https://www.google.com/search?q=" + keywords + "&newwindow=1&rlz=1C1CAFC_enKR908KR909&sxsrf=ALeKk01k_BlEDFe_0Pv51JmAEBgk0mT4SA:1600412339309&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj07OnHkPLrAhUiyosBHZvSBIUQ_AUoAXoECA4QAw&biw=1536&bih=754"
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    driver.get(path)
    driver.maximize_window()
    time.sleep(1)

    counter = 0
    succounter = 0

    print(os.path)
    if not os.path.exists('data'):
        os.mkdir('data')
    if not os.path.exists('data/' + keywords):
        os.mkdir('data/' + keywords)

    for x in driver.find_elements_by_class_name('rg_i.Q4LuWd'):
        counter = counter + 1
        print(counter)
        # 이미지 url
        img = x.get_attribute("data-src")
        if img is None:
            img = x.get_attribute("src")
        print(img)

        # 이미지 확장자
        imgtype = 'jpg'

        # 구글 이미지를 읽고 저장한다.

        try:
            raw_img = urllib.request.urlopen(img).read()
            File = open(os.path.join('data/' + keywords, keywords + "_" + str(counter) + "." + imgtype), "wb")
            File.write(raw_img)
            File.close()
            succounter = succounter + 1
        except:
            print('error')

    print(succounter, "succesfully downloaded")
    driver.close()


crawl("못ㅅㅇ긴 셀카")
