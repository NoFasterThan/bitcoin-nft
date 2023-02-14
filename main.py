# -*- coding: utf-8 -*-
import logging
import random
import time
from datetime import datetime
from lib2to3.pgen2 import driver

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from extension import proxies
from selenium_tools.twitter import login_twitter, twitter_follow, twitter_retweet_with_url

logging.basicConfig(filename="logging.log", level=logging.INFO)
ANTICAPTCHA = 'anticaptcha.crx'
METAMASK = 'metamask10.14.crx'

proxy_hai = open("HaiProxy.txt", "r").read().split("\n")

user_agents_desktop = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 "
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
    "Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
]

tweets = pd.read_csv("tweet_all.csv")
discords = pd.read_csv("discord_all.csv")
tweet_id = tweets.iloc[:, 0].tolist()
tweet_password = tweets.iloc[:, 1].tolist()
tweet_phone = tweets.iloc[:, 2].tolist()
# It is mobile user agent
tweet_useragent = tweets.iloc[:, 3].tolist()
tweet_cookie = tweets.iloc[:, 4].tolist()
discord_token = discords.iloc[:, 0].tolist()
discord_token_parse = list(map(lambda x: x.replace("\n", ""), discord_token))

if __name__ == '__main__':
    failed = []
    for num_idx in range(7, len(tweet_id)):

        start = time.time()
        try:
            logging.warning("\n")
            logging.warning("\n")
            logging.warning("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning(f"{datetime.now()}")
            logging.warning(
                f"+++++++++++++++++++++++++++++      {num_idx}         +++++++++++++++++++++++++++++++++++++")
            options = webdriver.ChromeOptions()
            # options.add_argument("--headless")
            # options.add_argument('--no-sandbox')
            # options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-gpu')
            options.add_argument('--start-maximized')
            options.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
            # options.add_argument("user-agent=" + tweet_useragent[num_idx])
            options.add_argument(
                "user-agent=" + user_agents_desktop[random.randint(0, len(user_agents_desktop) - 1)])
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            # options.add_argument("--disable-blink-features=AutomationControlled")
            # options.add_experimental_option('useAutomationExtension', False)
            options.add_extension(ANTICAPTCHA)
            options.add_extension(METAMASK)

            # proxies_extension = proxies("user-jo1234-sessionduration-1", "uosai2021", "us.smartproxy.com", "10001")
            ip = proxy_hai[num_idx].split(":")[0]
            port = proxy_hai[num_idx].split(":")[1]
            proxies_extension = proxies("jo123", "Pwjustforhack4$", ip, port)
            options.add_extension(proxies_extension)
            # options.add_argument("--headless=new")
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                                      options=options)

            # twitter login
            login_twitter(driver, tweet_id[1833 - num_idx], tweet_password[1833 - num_idx], tweet_phone[1833 - num_idx],
                          cookie=tweet_cookie[1833 - num_idx])

            # twitter follow
            twitter_follow(
                "@notablesart",
                driver,
                sequenced=True
            )

            twitter_follow(
                "@0xDith",
                driver
            )
            twitter_retweet_with_url(
                "https://twitter.com/0xDith/status/1625154314191659008",
                "OxDith",
                driver
            )
            twitter_retweet_with_url(
                "https://twitter.com/notablesart/status/1625185570115797007",
                "notablesart",
                driver
            )

            driver.quit()
            logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning("whole process success")
            logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning("\n")
        except Exception as e:
            print(str(e))
            driver.quit()
            logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning("fail")
            failed.append(num_idx)
            logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning("\n")
        # 종료하고 담 반복문으로
        print("[%d/%d] Whole process Completed for %.2f" % (num_idx, 1000, time.time() - start))
        logging.info("[%d/%d] Whole process Completed for %.2f" % (num_idx, 1000, time.time() - start))
    logging.fatal(f"{failed}")
