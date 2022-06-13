from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from itertools import count
import random

class GameBot:
    
    def __init__(self):
        self.high_scores = []
        # setting number of rounds to play via sysargs
        try:
            self.rounds = int(sys.argv[1])
        except:
            self.rounds = None
        self.driver = webdriver.Chrome()
        # initializing the selenium driver
        self.driver.get('https://play2048.co/')
        self.roundsCompleted = 0
        self.keys = [Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_UP]
        self.container = self.driver.find_element(by=By.TAG_NAME, value='html')

    def _start_round(self):
        start = self.driver.find_element(by=By.CLASS_NAME, value='restart-button')
        start.click()
    
    def _key_press_loop_random(self):
        i = random.randrange(0, 4)
        self.container.send_keys(self.keys[i])
        sleep(.1)

    def _key_press_loop_circular(self):
        for i in range(0, 4):
            self.container.send_keys(self.keys[i])
            sleep(.1)

    def _check_for_game_over(self):
            self.driver.find_element(by=By.CLASS_NAME, value='game-over')
            # set high score to best score
            best_score_value = self.driver.find_element(by=By.CLASS_NAME, value='best-container')
            high_score = best_score_value.get_attribute('innerHTML')
            # restart round
            retry_button = self.driver.find_element(by=By.CLASS_NAME, value='retry-button')
            retry_button.click()
            return high_score

    def game_loop(self):
        try:
            if self.rounds:
                for i in range(self.rounds):
                    self._round_loop()
            # infinite game loop     
            else:
                for i in count(0):
                    self._round_loop()
            self.driver.quit()
        except KeyboardInterrupt:
            self.driver.quit()
            print('Game stopped!')
    
    def _round_loop(self):
        round_over = False
        self._start_round()
        while round_over == False:
            self._key_press_loop_circular()
            try: 
                high_score = self._check_for_game_over()
                round_over = True
                self.high_scores.append(int(high_score))
            except:
                continue
        self.roundsCompleted += 1

    def end_message(self):
        if not self.roundsCompleted:
            print('Game stopped too early to capture stats')
        else:
            print(
f"""Best high score over {self.roundsCompleted} rounds: {self.high_scores[-1]} 
Average score per round: {round(sum(self.high_scores) / self.roundsCompleted)}""")