"""
Using a Selenium Webdriver to access more complicated information from websites for more useful tools.
Will open the 2022 season Game-By-Game statistics from FGCU Women's soccer team.
https://fgcuathletics.com/sports/womens-soccer/stats?path=wsoc
Will read this page and count how many games then write this information to a file.
Will then repeat for the last two years (2021, 2020)
Will display (print) which season they did the best
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys     # literally keys on the keyboard for input
from selenium.webdriver.common.by import By

if __name__ == '__main__':

    driver = webdriver.Chrome()
    driver.get("https://fgcuathletics.com/sports/womens-soccer/stats/2022")
    assert "page not found" not in driver.page_source

    elem = driver.find_element(By.CLASS_NAME, "sidearm-table")
    print(elem.text)


    driver.close()