import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Scraper:

    targetDays = []
    targetTimeSlots = []
    updatedTargetDays = []
    temp = []

    def __init__(self, days, timeSlots):
        self.targetDays = days
        self.targetTimeSlots = timeSlots

    # prevents selenium from instantly closing, when initiated
    options = Options()
    options.add_experimental_option("detach", True)

    s = Service("C:\Program Files (x86)\chromedriver.exe")
    driver = webdriver.Chrome(service=s, options=options)

    def run(self):
        self.driver.get("https://bookings.better.org.uk/location/britannia-leisure-centre/badminton-60min/")
        self.driver.maximize_window()
        time.sleep(5)

        pageOne = self.driver.find_elements(By.CSS_SELECTOR, "a[class='DateComponent__Wrapper-sc-1821zu4-0 fupiPD'] > div:nth-child(1)")
        pageOneActive = self.driver.find_element(By.CSS_SELECTOR, "a[class='DateComponent__Wrapper-sc-1821zu4-0 fupiPD active'] > div:nth-child(1)")

        for i in range(len(self.targetDays)):
            if pageOneActive.get_attribute("innerHTML") == self.targetDays[i]:
                self.updatedTargetDays.append(pageOneActive.get_attribute("innerHTML"))
                self.temp.append(pageOneActive)

        for i in range(len(pageOne)):
            for j in range(len(self.targetDays)):
                if pageOne[i].get_attribute("innerHTML") == self.targetDays[j]:
                    self.updatedTargetDays.append(pageOne[i].get_attribute("innerHTML"))
                    self.temp.append(pageOne[i])

        for i in range(len(self.updatedTargetDays)):
            button = self.temp[i]
            button.click()
            time.sleep(4)

            print(self.updatedTargetDays[i])

            pageTwo = self.driver.find_elements(By.XPATH, "//div[@class='ClassCardComponent__ClassTime-sc-1v7d176-3 kOypzl']")
            count = 0

            for j in range(len(pageTwo)):
                for k in range(len(self.targetTimeSlots)):
                    if pageTwo[j].get_attribute("innerHTML") == self.targetTimeSlots[k]:
                        count = count + 1
                        pageThree = self.driver.find_elements(By.XPATH, "//span[@class='ContextualComponent__BookWrap-sc-eu3gk6-1 etPXJI']")
                        if pageThree[k].text[0] == "0":
                            print("(" + self.targetTimeSlots[k] + "): No availability")
                        else:
                            print("(" + self.targetTimeSlots[k] + "): Availabilities: " + pageThree[k].text[0])
            print()
            print(count)
