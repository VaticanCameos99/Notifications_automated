import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser
from selenium import webdriver
import urllib
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time

base_dir = '/home/nirvi/Downloads/Yale/Antonio/ViT/'

def element_presence(by, xpath, time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def send_message(url):
    driver.get(url)
    time.sleep(2)
    element_presence(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]', 40)
    msg_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    msg_box.send_keys('\n')
    time.sleep(1)

def prepare_msg(dataframe, name_col, phone_col):
    file = dataframe[[name_col, phone_col]]
    base_msg = """
*Hi {}*!
How are you? I hope you're doing well.

This is a test message

Thanks!
"""
    base_url = 'https://web.whatsapp.com/send?phone={}&text={}'
    for i,j in tqdm(file.iterrows()):
        phone_no = j[phone_col]
        Name = j[name_col].title()
        Vid_File = base_dir+phone_no.split(' ')[-1][1:-1] + '.mp4'

        print(phone_no, 'phoneno')
        print(Name, 'Name')
        print(Vid_File, 'VidFile')
        msg = urllib.parse.quote(base_msg.format(Name))
        url_msg = base_url.format(phone_no, msg)
        send_message(url_msg)

        time.sleep(2)
        # try:
        attachement_box = driver.find_element_by_xpath('//div[@title="Attach"]')
        attachement_box.click()
        time.sleep(1)

        image_box = driver.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(Vid_File)
        time.sleep(2)

        send_box = driver.find_element_by_xpath('//span[@data-icon="send"]')
        send_box.click()
        time.sleep(4)
        print('Done :)')



chrome_options = Options()
chrome_options.add_argument("--user-data-dir-Session")
chrome_options.add_argument("--profile-directory=Default")

PATH = "/home/nirvi/Downloads/chromedriver_linux64/chromedriver"
driver = webdriver.Chrome(PATH, options=chrome_options)

df = pd.read_csv('phone_numbers.csv')
prepare_msg(df, 'Name', 'Phone')