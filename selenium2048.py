from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from itertools import count
import random

class GameBot:
    
    def __init__(self):
        self.high_score = 0
        self.game_over = False
        try:
            self.rounds = int(sys.argv[1])
        except:
            self.rounds = None
        self.driver = webdriver.Chrome()
        self.roundsCompleted = 0
        self.driver.get('https://play2048.co/')
        self.container = self.driver.find_element(by=By.TAG_NAME, value='html')

    def _start_round(self):
        start = self.driver.find_element(by=By.CLASS_NAME, value='restart-button')
        start.click()
    
    def _key_press_loop(self):
        self.container.send_keys(Keys.ARROW_RIGHT)
        # sleep(.1)
        self.container.send_keys(Keys.ARROW_DOWN)
        # sleep(.1)
        self.container.send_keys(Keys.ARROW_LEFT)
        # sleep(.1)
        self.container.send_keys(Keys.ARROW_UP)
        # sleep(.1)

    def _check_for_game_over(self):
            self.driver.find_element(by=By.CLASS_NAME, value='game-over')
            game_over = True
            # set high score to best score
            best_score_value = self.driver.find_element(by=By.CLASS_NAME, value='best-container')
            high_score = best_score_value.get_attribute('innerHTML')
            # restart round
            retry_button = self.driver.find_element(by=By.CLASS_NAME, value='retry-button')
            retry_button.click()
            return game_over, high_score

    def game_loop(self):
        if self.rounds:
            for i in range(self.rounds):
                self._round_loop()
                
        else:
            for i in count(0):
                self._round_loop()
    
    def _round_loop(self):
        self.game_over = False
        self._start_round()
        while self.game_over == False:
            # TODO: randomize key entries
            self._key_press_loop()
            try: 
                self.game_over, self.high_score = self._check_for_game_over()
            except:
                continue
        self.roundsCompleted += 1

game_bot = GameBot()
game_bot.game_loop()

print(f'Best high score over {game_bot.roundsCompleted} rounds: {game_bot.high_score}')