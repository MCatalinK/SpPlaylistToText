import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def export_playlist(url):
    driver = webdriver.Firefox()

    try:
        pattern = r"https://open.spotify.com/playlist*"
        match = re.match(pattern, url)
        if not match:
            raise Exception("The url doesn't match")
        driver.get("https://www.chosic.com/spotify-playlist-exporter/")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "sp_message_iframe_1231397"))
        )
        driver.switch_to.frame("sp_message_iframe_1231397")
        cookie_option = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Options')]")
            )
        )

        cookie_accept = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Accept')]")
            )
        )
        cookie_accept.click()
        driver.switch_to.default_content()

        # Searchbox
        input_box = driver.find_element(By.ID, "search-word")
        input_box.clear()
        input_box.send_keys(url)
        driver.find_element(By.ID, "analyze").click()

        time.sleep(3)
        # Download
        export = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, "export"))
        )
        export.click()

    except Exception as ex:
        print(ex)
        return str(ex)
    finally:
        time.sleep(2)
        driver.quit()
        return "Successful"
