"""
Using a Selenium Webdriver to access more complicated information from websites for more useful tools.
Will open the 2022 season Game-By-Game statistics from FGCU Women's soccer team.
https://fgcuathletics.com/sports/womens-soccer/stats?path=wsoc
Will read this page and count how many games then write this information to a file.
Will then repeat for the last two years (2021, 2020)
Will display (print) which season they did the best
"""

from selenium import webdriver

if __name__ == '__main__':
    # opens google chrome
    driver = webdriver.Chrome()
