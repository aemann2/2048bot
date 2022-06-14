from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from itertools import count
import random
import inquirer

class GameBot:
    
    def __init__(self):
        self.high_scores = []
        # setting number of rounds to play via sysargs
        try:
            self.rounds = int(sys.argv[1])
        except ValueError:
            print('Round values must be a number.')
            sys.exit()
        except:
            self.rounds = None
        self.game_speed = self._speed_prompt()
        self.driver = webdriver.Chrome()
        # initializing the selenium driver
        self.driver.get('https://play2048.co/')
        self.rounds_completed = 0
        self.keys = [Keys.ARROW_RIGHT, Keys.ARROW_DOWN, Keys.ARROW_LEFT, Keys.ARROW_UP]
        self.container = self.driver.find_element(by=By.TAG_NAME, value='html')

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
        except:
            self.driver.quit()
            print('Game stopped!')

    def end_message(self):
        if not self.rounds_completed:
            print('Game stopped too early to capture stats')
        else:
            print(
f"""Best high score over {self.rounds_completed} rounds: {self.high_scores[-1]} 
Average score per round: {round(sum(self.high_scores) / self.rounds_completed)}""")

    def _round_loop(self):
        round_over = False
        self._start_round()
        while round_over == False:
            self._key_press_loop_random()
            # if _check_for_game_over throws an error, it's because the game is still going, so we'd except and continue the loop
            try: 
                high_score = self._check_for_game_over()
                self.high_scores.append(int(high_score))
                round_over = True
            except:
                continue
        self.rounds_completed += 1

    def _start_round(self):
        start = self.driver.find_element(by=By.CLASS_NAME, value='restart-button')
        start.click()
    
    def _key_press_loop_random(self):
        i = random.randrange(0, 4)
        self.container.send_keys(self.keys[i])
        sleep(self.game_speed)

    def _key_press_loop_circular(self):
        for i in range(0, 4):
            self.container.send_keys(self.keys[i])
            sleep(self.game_speed)

    def _check_for_game_over(self):
            self.driver.find_element(by=By.CLASS_NAME, value='game-over')
            # set high score to best score
            best_score_value = self.driver.find_element(by=By.CLASS_NAME, value='best-container')
            high_score = best_score_value.get_attribute('innerHTML')
            # restart round
            retry_button = self.driver.find_element(by=By.CLASS_NAME, value='retry-button')
            retry_button.click()
            return high_score

    def _speed_prompt(self):
        speed_choices = ['Fast', 'Medium', 'Slow']
        sleep_times = [.1, .3, .5]
        questions = [
            inquirer.List('speed',
                message="Choose a speed for the bot:",
                choices=speed_choices,
            )]
        answer = inquirer.prompt(questions)
        idx = speed_choices.index(answer['speed'])
        game_speed = sleep_times[idx]
        return game_speed