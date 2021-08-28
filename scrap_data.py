from time import sleep
from typing import List

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# CONSTANTS
FOLDER_BUTTON_XPATH = "/html/body/app/div[1]/main/ng-component/div[1]/div/problemset-tree/div[1]/div[2]/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div/div/div/div/button"
QUESTIONS_XPATH = "/html/body/app/div[1]/main/ng-component/div[1]/div/problemset-tree/div[1]/div[2]/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-children/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div/div/div"
QUESTION_TITLE_XPATH = "div[1]/button/span[4]"
DUE_DATE_XPATH = "div[2]/div[1]/div/span/span[2]"
STATUS_XPATH = "div[2]/div[4]/div/span[2]"
# ========


def main(driver: webdriver.Chrome):
    print("A new CHROME browser window will open with the codezinger link in it")
    print("You have to enter your login and password.")
    # input("Press enter to continue... ")
    login_codezinger(driver)
    expand_all_labs(driver)
    data = get_data(driver)


def login_codezinger(driver: webdriver.Chrome):
    driver.get("https://labs.codezinger.com/student/classes/611dc47ba6ae540012d2130f")

    while "login" in driver.title.lower():
        sleep(1)

    print("logged in")
    # driver.get("https://labs.codezinger.com/student/classes/611dc47ba6ae540012d2130f")


def expand_all_labs(driver: webdriver.Chrome):
    buttons = driver.find_elements_by_xpath(FOLDER_BUTTON_XPATH)
    # print(buttons)
    for button in buttons:
        button.click()
    print("Expanded", len(buttons), "folders.")


def get_data(driver: webdriver.Chrome) -> List[dict]:
    data: List[dict, ...] = []

    breakpoint()

    return data

if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        main(driver)
        x = input("enter to close....")
        if x:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
