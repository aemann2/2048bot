# 2048 Bot

This is a Selenium bot that plays [2048](https://play2048.co/). Idea taken from [this chapter](https://automatetheboringstuff.com/2e/chapter12/) of Automate the Boring Stuff.


## Installation instructions:
- Install Python 3
- Set up a virtual environment in the repo's root directory: `python -m venv venv`
- Activate env: `source venv/bin/activate`
- Install dependencies in requirements.txt w/ `pip install -r requirements.txt`
- Follow instructions for installing Chromedrive for Chrome: https://chromedriver.chromium.org/getting-started
- Run project w/ `python selenium2048.py`

**Notes**: 
- The 2048 website is a bit janky, and the ads on the page sometimes cause the browser to crash. If that happens, you may have to restart the program.
- This project was create on OSX Monterey 12.3.1. YMMV on other operating systems.
