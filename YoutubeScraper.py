from selenium import webdriver
import os
import pandas as pd

#Construct the Youtube link
ytlink_prefix = 'https://www.youtube.com/c/'
ytlink_suffix = '/videos?view=0&sort=p&flow=grid'
channel_name = input('Enter Youtube Channel Name: ')
url = f'{ytlink_prefix}{channel_name}{ytlink_suffix}'

#Launch Chrome
driver = webdriver.Chrome(executable_path=os.path.abspath("F:\surya\Videos\chromedriver_win32 (1)\chromedriver.exe"))
driver.get(url)

#Scrape videos
videos = driver.find_elements_by_class_name("style-scope ytd-grid-video-renderer")
video_count = 10

#List of all videos
scraped_Videos = []

#Title, Views, Time of the popular videos
for video in videos[:video_count]:
    title = video.find_element_by_xpath('.// *[ @ id = "video-title"]').text
    views = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[1]').text
    time = video.find_element_by_xpath('.//*[@id="metadata-line"]/span[2]').text

    scraped_Videos.append({
        "Title of the video": title,
        "Views": views,
        "Posted on":time}
    )

# Creating a DataFrame for scraped videos
df = pd.DataFrame(scraped_Videos)

df.set_index('Title of the video',inplace=True)

print(df)
