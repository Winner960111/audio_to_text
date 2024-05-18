from selenium import webdriver
from openpyxl import workbook
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
service = Service(executable_path="C:\chromedriver-win64\chromedriver.exe")
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9030")
driver = webdriver.Chrome(service=service, options=options)
# driver.maximize_window()

# url = "https://www.globalplayer.com/podcasts/42KbSh/"
# driver.get(url)
sleep(5)

def Find_Element(driver, whichBy, unique: str) -> WebElement:
    while True:
        try:
            element = driver.find_element(whichBy, unique)
            break
        except:
            pass
        sleep(3)
    return element
try:
    print("start..")
    catalogues = driver.find_elements(By.CLASS_NAME, 'style_podcastEpisode__APEZP')
    music_lists = []
    video_lists = []
    total_list = []
    print("get lists...")
    for item in range(1, 400):
    # Get title
        while True:
            try:
                sleep(0.5)
                catalogues = driver.find_elements(By.CLASS_NAME, 'style_podcastEpisode__APEZP')
                if catalogues:
                    break
            except:
                sleep(0.5)
                pass
        
        music_name = catalogues[item-1].find_element(By.CLASS_NAME, 'style_episodeText__Ppy1R').find_element(By.TAG_NAME, 'h4').find_element(By.TAG_NAME, 'a').text
        music_lists.append(music_name)
        print("music naem:", music_name)
        sleep(0.5)
    # click each music link
        while True:
                try:
                    sleep(0.5)
                    music_link_click = catalogues[item-1].find_element(By.CLASS_NAME, 'style_episodeText__Ppy1R').find_element(By.TAG_NAME, 'h4').find_element(By.TAG_NAME, 'a')
                    break
                except:
                    sleep(0.5)
                    pass
        
        driver.execute_script("arguments[0].click();", music_link_click)
    # click play button

        while True:
            try:
                sleep(0.5)
                play_btn = driver.find_element(By.CLASS_NAME, "style_gpBtn__nhbDP")
                break
            except:
                sleep(0.5)
                pass
        driver.execute_script("arguments[0].click();", play_btn)
        print("click the play button")
        while True:
            try:
                sleep(0.5)
                video_link = driver.find_element(By.TAG_NAME,"video").get_attribute("src")
                if video_link:
                    break
            except:
                sleep(0.5)
                pass
        video_lists.append(video_link)
        print("this is video Link", video_link)
        sleep(0.5)
    # return back
        while True:
            try:
                sleep(0.5)
                back_btn = driver.find_element(By.CLASS_NAME, "style_link__7WBXv").find_element(By.TAG_NAME, "a")
                break
            except:
                sleep(0.5)
                pass
        driver.execute_script("arguments[0].click();", back_btn)
        sleep(0.5)

        total_list.append({"music_name" : music_name, "music_link" : video_link})
    
    with open("output.json", 'w') as data:
        json.dump(total_list, data)
    print("Successfully finish!")
except Exception as e:
    print("Error:", e)
