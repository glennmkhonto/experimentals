from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def ui_testing():
    driver = webdriver.Chrome(service=Service('/usr/lib/chromium-browser/chromedriver'))

    driver.get("http://localhost:3000")
    driver.maximize_window()
    try:
        time.sleep(2)
        sort_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/main/table/thead/tr/th[1]")))
        sort_icon.click()
        print("Sort icon clicked successfully")
        time.sleep(2)
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/section/main/table/tbody/tr")))
        print("waiting")
        movie_title_elements = driver.find_elements(By.XPATH, "/html/body/section/main/table/tbody/tr/td[1]")
        movie_titles = [title.text for title in movie_title_elements]

        print("getting the list")
        last_movie_title_element = movie_title_elements[-1]
        last_movie_title = last_movie_title_element.text
        print(f'last movie {last_movie_title}')
        last_movie_title_element.click()
        
        time.sleep(2)
        print("after click")
        planet_list = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/main/div[2]/div[2]")))

        planet_not_found = "Camino" not in planet_list.text
        print("panet not fount", planet_not_found)

        assert planet_not_found, f"Camino is found in the list of planets for the movie '{last_movie_title}'"
        print("after planet not found")
        time.sleep(2)
        back_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/nav/a")))
        back_button.click()

        empire_strikes_back_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/section/main/table/tbody/tr[2]/td[1]/a")))
        empire_strikes_back_link.click()
        print("Clicked on 'The Empire Strikes Back' link")
        time.sleep(2)
        species_list = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/section/main/div[2]/div[3]")))
        
        wookie_found = "Wookie" in species_list.text
        print("trying to check wookie", wookie_found)
        assert wookie_found, "Wookie is not found in the Species list of the movie 'The Empire Strikes Back'"

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

ui_testing()