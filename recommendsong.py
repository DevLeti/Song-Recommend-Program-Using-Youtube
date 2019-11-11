#import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

#import time
def recommend(keyword):

    # Beautifulsoup4 시도.
    # Selenium으로 넘어간 이유는 밑에 서술

    # base_url = "https://www.youtube.com/results?search_query=" + keyword
    # html = requests.get(base_url).text
    # # print(html)
    # soup = BeautifulSoup(html, 'html.parser')
    
    # first_song = soup.select('a.yt-uix-tile-link')[0]['href']
    # # print(first_song)
    # first_song_url = 'https://www.youtube.com/watch?v=' + first_song
    #first_song_html = requests.get(first_song_url).text # 이것의 다음 동영상을 확인해야함
    # soup = BeautifulSoup(first_song_html, 'html.parser')
    # print(soup)
    # next_song_recommend = soup.select('a.yt-simple-endpoint')#[0]['href']
    # print(next_song_recommend)

    ################################################################
    # search 첫번째 동영상 url까지 따는걸 bs4로 하고                 #
    # 다음 동영상 url을 selenium으로 가져오려 했으나                 #
    # 직접적으로 들어갔을때 정보를 얻어오지 못하게 유투브에서 막는중. #
    # Selenium 방식                                                 #
    ################################################################
    driver = webdriver.Chrome('C:\\song_recommend\\chromedriver.exe')
    
    driver.get('https://youtube.com')
    driver.implicitly_wait(3) # 로딩 기다려주기

    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located(
            (By.CSS_SELECTOR, "button#search-icon-legacy")
            )
    )
    driver.find_element_by_id('search').send_keys(keyword)
    driver.find_element_by_css_selector('button#search-icon-legacy').click()
    
    driver.implicitly_wait(1) # 로딩 기다려주기
    
    #content 첫번째 xpath
    #/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a
    
    WebDriverWait(driver, 4).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a") # div 한개 로딩 되는거로 기다리기
            )
    )
    driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a').click()
    
    # CSS_SELECTOR
    # WebDriverWait(driver, 4).until(
    #     expected_conditions.presence_of_element_located(
    #         (By.CSS_SELECTOR, "ytd-video-renderer") # div 한개 로딩 되는거로 기다리기
    #         )
    # )
    # driver.find_element_by_css_selector('h3 > a#video-title').click()
    


    # 다음 동영상 xpath
    # /html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-autoplay-renderer
    driver.implicitly_wait(3) # 로딩 기다려주기

    WebDriverWait(driver, 14).until(
        expected_conditions.presence_of_element_located(
            (By.XPATH, "/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-autoplay-renderer")
            )
    )
    # CSS_SELECTOR로 다음 동영상 로딩 감지
    # WebDriverWait(driver, 7).until(
    #     expected_conditions.presence_of_element_located(
    #         (By.CSS_SELECTOR, "div#items>ytd-compact-autoplay-renderer") #h3 > span#video-title
    #         )
    # )
    next_song_tag = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[2]/div/div[3]/ytd-watch-next-secondary-results-renderer/div[2]/ytd-compact-autoplay-renderer/div[2]/ytd-compact-video-renderer/div[1]/div[1]/a/h3/span')
    
    next_song_name = next_song_tag.text # 또는 .get_attribute("text")
    print("크롤링 완료!")
    print("song name : {}".format(next_song_name))
    

if __name__ == "__main__":
    song_name_for_recommend = input("input song name : ")
    recommend(song_name_for_recommend)



