from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.get('https://play2048.co/')

# Firefox will wait until the page is completely loaded (including ads) before starting
sleep(3)

container = driver.find_element(by=By.TAG_NAME, value='html')

high_score = 0

#TODO list:
# - Prompt user to play a certain number of rounds. If not specified, do infinite until user pressed CTRL + C
# - Use OOP to break up bot functionality
# - Display some kind of stats at the end?
# - See if you can get a browser alert to display at the end

# TODO: remove hard-coded cycle and accept input prompt
for i in range(4):
    game_over = False
    # TODO: functionize start cycle
    start = driver.find_element(by=By.CLASS_NAME, value='restart-button')
    start.click()
    while game_over == False:
        # TODO: functionize (and maybe randomize) key entries. consider adding a small sleep between each key press
        container.send_keys(Keys.ARROW_RIGHT)
        container.send_keys(Keys.ARROW_DOWN)
        container.send_keys(Keys.ARROW_LEFT)
        container.send_keys(Keys.ARROW_UP)
    # TODO: functionize game-over loop
    # TODO: try to find a different way to do this rather than a try/catch
        try: 
            driver.find_element(by=By.CLASS_NAME, value='game-over')
            game_over = True
            # set high score to best score
            best_score_value = driver.find_element(by=By.CLASS_NAME, value='best-container')
            high_score = best_score_value.get_attribute('innerHTML')
            retry_button = driver.find_element(by=By.CLASS_NAME, value='retry-button')
            retry_button.click()
        except:
            continue

print(f'Best high score: {high_score}')