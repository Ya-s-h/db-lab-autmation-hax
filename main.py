"""
    Copyright (c) 2021 Ya-s-h, RoguedBear

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import traceback
from time import sleep
from selenium import webdriver
from FileCreation import dataInsertion
from scrap_data import *
from db import *
import mysql.connector

host_args = {
    "host": "localhost",
    "user": "root",
    "password": ""
}

con = mysql.connector.connect(**host_args)

cur = con.cursor(dictionary=True)

sno = [[1, 6], [6, 14], [14, 25]]
date = ['2021-08-24', '2021-08-28', '2021-08-31']


def main(driver: webdriver.Chrome):
    print("A new CHROME browser window will open with the codezinger link in it")
    print("You have to enter your login and password.")
    # input("Press enter to continue... ")
    login_codezinger(driver)
    expand_all_labs(driver)
    data = get_data(driver)
    file_name = dataInsertion(data)
    exec_sql_file(cur, file_name)
    dateAssign(cur, sno, date)
    con.commit()
    con.close()


def driver_exists():
    import os
    import sys
    import webbrowser

    if not os.path.isfile("chromedriver.exe"):
        print("\033[5;31mYou need to install selenium chromedriver to run this program\033[0m")
        for i in range(1, 6):
            print(f"Opening download link in {5 - i}....", end="\r")
            sleep(1)
        print()
        webbrowser.open_new_tab("https://sites.google.com/a/chromium.org/chromedriver/downloads")
        sys.exit(1)


if __name__ == '__main__':
    driver_exists()
    driver = webdriver.Chrome(executable_path=r"C:\Users\Yash\Downloads\chromedriver_win32\chromedriver.exe")
    print("""DB-Hax  Copyright (C) 2021  RoguedBear, Ya-s-h
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.""")
    try:
        main(driver)
    except Exception as ex:
        traceback.print_exception(type(ex), ex, ex.__traceback__)
    finally:
        driver.close()
