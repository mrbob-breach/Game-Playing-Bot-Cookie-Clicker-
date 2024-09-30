from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

"""1. Create a list of item IDs"""
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
items = [item.get_attribute("id") for item in items]

time_after_5_seconds = time.time() + 5
time_after_5_minutes = time.time() + 300
"""2. Create a while loop for clicking cookies"""
cookie = driver.find_element(By.ID, value="cookie")
while True:
    cookie.click()

    """3. Set a timer to track every 5 seconds that passes"""
    if time.time() > time_after_5_seconds:
        time_after_5_seconds += 5

        """4. Check how much money we have. Remove any commas and convert to int"""
        money = driver.find_element(By.ID, value="money").text
        if "," in money:
            money = money.replace(",", "")
        money = int(money)

        """5. Check the prices of items in the store"""
        items_2 = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
        items_2 = [item.text for item in items_2]
        item_prices = [int(item.split("-")[1].replace(",", "")) for item in items_2 if item != ""]

        """6. Check the items that we can buy and which one is the most expensive"""
        items_dict = {key: value for (key, value) in zip(items, item_prices)}
        items_can_buy = []
        for key, value in items_dict.items():
            if money > value:
                items_can_buy.append(key)
            try:
                item_to_buy = items_can_buy[-1]
            except IndexError:
                pass

        """7. Buy the most expensive item in the list"""
        buying_item = driver.find_element(By.ID, value=item_to_buy)
        buying_item.click()

    """8. Stop the game after 5 minutes and print cookies per second metric"""
    # if time.time() > time_after_5_minutes:
    #     cps = driver.find_element(By.ID, value="cps").text
    #     cps = cps.split(":")[1].replace("'", "")
    #     print(f"You've reached {cps} cookies per second!")
    #     driver.quit()

