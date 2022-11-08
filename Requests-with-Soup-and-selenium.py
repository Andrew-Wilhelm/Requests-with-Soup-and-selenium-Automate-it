"""
Using a Selenium Webdriver to access more complicated information from websites for more useful tools.
Will open the 2022 season Game-By-Game statistics from FGCU Women's soccer team.
https://fgcuathletics.com/sports/womens-soccer/stats?path=wsoc
Will read this page and count how many games then write this information to a file.
Will then repeat for the last two years (2021, 2020)
Will display (print) which season they did the best
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # literally keys on the keyboard for input
from selenium.webdriver.common.by import By


def makerows(row):
    words = ""

    for i, letter in enumerate(row):
        if not letter.isdigit():
            words += letter
        else:
            return [words.strip(), *row[i:].split(" ")]


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://fgcuathletics.com/sports/womens-soccer/stats/2022")
    assert "page not found" not in driver.page_source

    table_rows = []

    table_data = driver.find_elements(By.XPATH, "//table[1]//thread//tr//th")
    table_rows.append([h.text for h in table_data if h.text])

    table_data = driver.find_elements(By.XPATH, "//table[1]/tbody/tr")
    for row in table_data:
        if row.text:
            cur_row = makerows(row.text)
            if cur_row is None or len(cur_row) == 1:
                continue
            else:
                table_rows.append(cur_row)

    for i, row in enumerate(table_rows):
        print(f"Row {i} is:{row}")
    driver.close()
