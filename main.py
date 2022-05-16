import datetime
from selenium import webdriver
import time


def get_drvier():
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("https://automated.pythonanywhere.com")
    return driver


def clean_text(text):
    output = float(text.split(": ")[1])
    return output


def main():
    driver = get_drvier()
    element = driver.find_element(by="xpath",
                                  value="/html/body/div[1]/div/h1[2]")
    time.sleep(5)
    return clean_text(element.text)
while True:
      current_dt=datetime.datetime.now()
      current_dt_st= str(current_dt.strftime("%Y-%m-%d, %H:%M:%S"))
      extension= ".txt"
      file_name= current_dt_st + extension

      f = open(file_name, "w")
      f.write(str(main()))    
f.close()