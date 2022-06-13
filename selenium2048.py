from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Firefox()
driver.get('https://play2048.co/')

# Firefox will wait until the page is completely loaded (including ads) before starting. 
# TODO: Might consider switching to Chrome()?
sleep(3)

container = driver.find_element(by=By.TAG_NAME, value='html')

high_score = 0

#TODO list:
# - Prompt user to play a certain number of rounds. If not specified, do infinite until user pressed CTRL + C
# - Use OOP to break up bot functionality
# - Display some kind of stats at the end?
# - See if you can get a browser alert to display at the end


def start_round():
    start = driver.find_element(by=By.CLASS_NAME, value='restart-button')
    start.click()

def key_press_loop():
    container.send_keys(Keys.ARROW_RIGHT)
    # sleep(.1)
    container.send_keys(Keys.ARROW_DOWN)
    # sleep(.1)
    container.send_keys(Keys.ARROW_LEFT)
    # sleep(.1)
    container.send_keys(Keys.ARROW_UP)
    # sleep(.1)

def check_for_game_over(game_over, high_score):
            driver.find_element(by=By.CLASS_NAME, value='game-over')
            game_over = True
            # set high score to best score
            best_score_value = driver.find_element(by=By.CLASS_NAME, value='best-container')
            high_score = best_score_value.get_attribute('innerHTML')
            # restart round
            retry_button = driver.find_element(by=By.CLASS_NAME, value='retry-button')
            retry_button.click()
            return game_over, high_score

# TODO: remove hard-coded cycle and accept input prompt
for i in range(4):
    game_over = False
    start_round()
    while game_over == False:
        # TODO: randomize key entries
        key_press_loop()
    # TODO: try to find a different way to do this rather than a try/catch
        try: 
            game_over, high_score = check_for_game_over(game_over, high_score)
        except:
            continue

print(f'Best high score: {high_score}')