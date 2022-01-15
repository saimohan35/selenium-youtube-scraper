from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--disable-dev-shm-usage')
  driver = webdriver.Chrome(options=chrome_options)
  return driver

if __name__ == "__main__":
  print('connecting driver')
  driver = get_driver()
  driver.get(YOUTUBE_TRENDING_URL)
  print('page title:', driver.title)
  video_divs = driver.find_elements_by_tag_name('ytd-video-renderer')
  print(f'found {len(video_divs)} videos')