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

def write_file(text):
  current_dt=datetime.datetime.now()
  current_dt_st= str(current_dt.strftime("%Y-%m-%d, %H:%M:%S"))
  extension= ".txt"
  file_name= current_dt_st + extension
  with open (file_name, "w") as file:
    file.write(text)


def main():
    driver = get_drvier()
    while True:
      time.sleep(2)
      element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
      text= str(clean_text(element.text))
      write_file(text) 

print(main())
