#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

s = Service('chromedriver')
driver = webdriver.Chrome(service=s)


driver.maximize_window()
driver.get('https://accounts.spotify.com/en/login')
driver.find_element(
    By.ID, 'login-username').send_keys('LOGIN')
driver.find_element(By.ID, 'login-password').send_keys('PASSWORD')
driver.find_element(By.ID, 'login-button').click()
time.sleep(2)


songs_urls = []
with open('songs.txt') as songsfile:
    for line in songsfile:
        songs_urls.append('https://open.spotify.com/search/' +
                          line.strip().rstrip('\n') + '/tracks')

with open('notadded.txt', 'w') as notfound:
    for song in songs_urls:
        driver.get(song)
        time.sleep(10)
        try:
            button = driver.find_element(
                By.XPATH, '//*[@id="searchPage"]/div/div/div/div[1]/div[2]/div[2]/div[1]/div/div[4]/button[1]')
            if 'Save' in button.get_attribute('aria-label'):
                button.click()
        except NoSuchElementException:
            notfound.write(song + '\n')


time.sleep(1)  
driver.quit()
