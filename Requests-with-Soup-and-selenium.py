"""
Using a Selenium Webdriver to access more complicated information from websites for more useful tools.
Will open the 2022 season Game-By-Game statistics from FGCU Women's soccer team.
https://fgcuathletics.com/sports/womens-soccer/stats?path=wsoc
Will read this page and count how many games then write this information to a file.
Will then repeat for the last two years (2021, 2020)
Will display (print) which season they did the best
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


def makerows(row):
    """
    This is just to show a bit of string manipulation and list handling.
    Will build a string of everything until the first digit is encountered.
    Then builds a list with that and a split (on empty) of the rest of the row.
    * = unpack (unpacks list into individual elements
        Used to avoid creating a temp, throw-away variable
    :param row: current row of table (as full string)
    :return: list of Statical description(str), Team(str,int,float), and Opponents(str,int,float)
    """

    words = ""
    for i, letter in enumerate(row):
        if not letter.isdigit():
            words += letter
        else:
            return [words.strip(), *row[i:].split(" ")]


"""
Basic overview of selenium over Beautiful Soup for webscrapping.

Loads multiple select options of a table then grabs the data.
Not optimized (good candidate for moving to async or multiprocess with bots)
"""
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("https://fgcuathletics.com/sports/womens-soccer/stats/2022")
    assert "Page not found" not in driver.page_source

    game_years = ["2022", "2021", "2020"]
    GameYear = 0
    TieGame = 0
    tie = False
    BestGame = 0

    # To get the first four
    for i in range(1, 4):
        # Get select option by index to make less weak
        selects = Select(driver.find_element(By.XPATH, "//select"))
        selects.select_by_index(i)

        table_rows = []

        driver.find_element(By.ID, "ui-id-3").click()  # clicks on GAME-BY-GAME

        driver.find_element(By.ID, "ui-id-12").click()  # clicks on GAME-BY-GAME

        table_data = driver.find_elements(By.XPATH, "//table[1]//thead//tr//th")
        # rather than [0:3] - just get any non-empty headers
        table_rows.append([h.text for h in table_data if h.text])

        table_data = driver.find_elements(By.XPATH, "//table[1]/tbody/tr")
        for row in table_data:
            if row.text:
                cur_row = makerows(row.text)
                # if cur_row is blank it will return None so check that & length
                if cur_row is None or len(cur_row) == 1:
                    continue
                else:
                    table_rows.append(cur_row)

        for j, row in enumerate(table_rows):
            with open('2022_sport', 'a') as f:
                f.write(f"Row {j} is: {row}\n")
        games = j+1
        with open('2022_sport', 'a') as f:
            f.write(f"----------Total games: {games}----------\n")

        if BestGame < games:
            BestGame = games
            GameYear = game_years[i-1]
        elif BestGame == games:
            TieGame = game_years[i-1]
            BestGame = games
            tie = True
    if tie:
        print(f"{GameYear} and {TieGame} tied for best with {BestGame} games played")
    else:
        print(f"{GameYear} was the best with {BestGame} games played")
    driver.close()



