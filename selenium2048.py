from game_bot import GameBot

def main():
    game_bot = GameBot()
    game_bot.game_loop()
    game_bot.end_message()

if __name__ == '__main__':
    main()