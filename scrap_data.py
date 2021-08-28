# Copyright (c) 2021 RoguedBear

import traceback
from datetime import datetime
from pprint import pprint
from time import sleep
from typing import List

import selenium.webdriver.remote.webelement
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# CONSTANTS
FOLDER_BUTTON_XPATH = "/html/body/app/div[1]/main/ng-component/div[1]/div/problemset-tree/div[1]/div[2]/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div/div/div/div/button"
QUESTIONS_XPATH = "/html/body/app/div[1]/main/ng-component/div[1]/div/problemset-tree/div[1]/div[2]/div/tree-root/tree-viewport/div/div/tree-node-collection/div/tree-node/div/tree-node-children/div/tree-node-collection/div/tree-node/div/tree-node-wrapper/div/div/div"
QUESTION_TITLE_XPATH = "div[1]/button/span[4]"
PROBLEM_NUMBER_XPATH = "div[1]/button/span[2]"
DUE_DATE_XPATH = "div[2]/div[1]/div/span/span[2]"
STATUS_XPATH = "div[2]/div[4]/div/span[2]"
DEBUG = False

# ========


def main(driver: webdriver.Chrome):
    print("A new CHROME browser window will open with the codezinger link in it")
    print("You have to enter your login and password.")
    # input("Press enter to continue... ")
    login_codezinger(driver)
    expand_all_labs(driver)
    data = get_data(driver)
    pprint(data)


def login_codezinger(driver: webdriver.Chrome, username: str = "", password: str = ""):
    driver.get("https://labs.codezinger.com/student/classes/611dc47ba6ae540012d2130f")

    # Auto login
    if DEBUG or (username and password):
        while "login" not in driver.title.lower():
            sleep(1)
        email = driver.find_element_by_xpath(
                "/html/body/app/div[1]/main/ng-component/section/div/div[1]/div/div/form/div[1]/div/div/input")
        email.send_keys(username)
        pwd = driver.find_element_by_xpath(
                "/html/body/app/div[1]/main/ng-component/section/div/div[1]/div/div/form/div[2]/div/div/input")
        pwd.send_keys(password)
        submit = driver.find_element_by_xpath(
                "/html/body/app/div[1]/main/ng-component/section/div/div[1]/div/div/form/div[3]/div/button")
        submit.click()
        sleep(1)
        try:
            yes = driver.find_element_by_xpath("/html/body/app/div[1]/main/ng-component/div/div/div/div[3]/button[2]")
            yes.click()
        except NoSuchElementException:
            pass
    # ------

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
    data_list: List[dict, ...] = []
    questions = driver.find_elements_by_xpath(QUESTIONS_XPATH)

    question: selenium.webdriver.remote.webelement.WebElement
    for question in questions:
        problem_no = question.find_element_by_xpath(PROBLEM_NUMBER_XPATH).text
        question_title = question.find_element_by_xpath(QUESTION_TITLE_XPATH).text
        due_date = question.find_element_by_xpath(DUE_DATE_XPATH).text.rstrip(" /-")
        status = question.find_element_by_xpath(STATUS_XPATH).text

        parsed_date: datetime = datetime.strptime(due_date, "%d %b %I:%M %p")
        parsed_date = parsed_date.replace(year=datetime.now().year)

        data = {
            "problem_desc": problem_no + " " + question_title,
            "assigned_date": "NULL",
            "submission_date": parsed_date.isoformat(),
            "status": status == "Submitted"
        }
        data_list.append(data)

    print("Scraped", len(questions), "questions")

    return data_list


if __name__ == '__main__':
    driver = webdriver.Chrome()
    try:
        main(driver)
        x = input("enter to close....")
        if x:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        driver.close()
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
        driver.close()
