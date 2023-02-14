# -*- coding: utf-8 -*-
import logging
import random
import time
from datetime import datetime
from lib2to3.pgen2 import driver

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from extension import proxies
from selenium_tools.common_tools import clickable, new_tab, textable

logging.basicConfig(filename="logging.log", level=logging.INFO)
ANTICAPTCHA = 'anticaptcha.crx'
METAMASK = 'metamask10.14.crx'


def premintRegister(username=None, password=None, token=None):
    logging.info("premintRegister start")
    time.sleep(4)
    # 프리민트 페이지로 넘어감
    first_tab = driver.window_handles[0]
    driver.switch_to.window(window_name=first_tab)

    logging.info("premintRegister wallet connect")
    # 지갑 연결
    time.sleep(2)
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[1]",
        driver
    )
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[4]",
        driver
    )
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/button",
        driver
    )
    clickable(
        "/html/body/div[3]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/button",
        driver
    )
    # clickable("/html/body/div[2]/div/div/div[2]/div[1]/div",driver)

    # 지갑 연결중 화면 전환
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    clickable("/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]", driver)

    clickable("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]", driver)

    # 버튼2
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[2]",
        driver
    )
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    clickable("/html/body/div[1]/div/div[2]/div/div[3]/button[2]", driver)
    time.sleep(1)
    driver.switch_to.window(driver.window_handles[0])

    # 버튼3
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[3]",
        driver
    )
    ##캡챠
    WebDriverWait(driver, 120).until(
        lambda x: x.find_element(By.CSS_SELECTOR, '.antigate_solver.solved'))

    driver.implicitly_wait(10)

    ## 트위터 연결 허용
    driver.switch_to.window(driver.window_handles[1])
    clickable(
        "/html/body/div[2]/div/form/fieldset/input[1]",
        driver
    )

    driver.switch_to.window(driver.window_handles[0])
    # 팔로우 완료 했으면 뜬다?
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[3]/div/div/div/div[2]/a",
        driver
    )

    driver.switch_to.window(driver.window_handles[0])

    clickable(
        "/html/body/div[2]/div/form/fieldset/input[1]",
        driver
    )

    # 4번
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[4]",
        driver
    )

    # 성공
    success_phrase = textable(
        "//*[text() = 'Registration Complete!']",
        driver
    )


def profile_premint(browser, token):
    logging.info("premint profile start")
    new_tab(
        "premint_profile",
        "https://premint.xyz/profile",
        browser
    )
    # 메타마스크로 로그인
    clickable(
        "/html/body/div[1]/div/div/div/div/section/div/div/div/div[1]/button[1]",
        browser
    )
    # 서명 완료
    browser.implicitly_wait(10)
    browser.switch_to.window(browser.window_handles[-1])
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    clickable(
        "/html/body/div[1]/div/div[2]/div/div[3]/button[2]",
        browser
    )
    # 페이지 끝까지 스크롤
    browser.switch_to.window("premint_profile")
    browser.implicitly_wait(10)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 트위터 연결
    clickable(
        "/html/body/div[6]/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[8]/div/a",
        browser
    )
    # 다시 오면 페이지 끝까지 스크롤
    browser.switch_to.window("premint_profile")
    browser.implicitly_wait(10)
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 디스코드 연결
    clickable(
        "/html/body/div[6]/div[2]/div/div/div/div[2]/div[3]/div/div/div[1]/div[9]/div/a",
        browser
    )
    # 다시 로그인
    browser.implicitly_wait(10)
    for _ in range(30):
        browser.execute_script(token)
        if len(browser.find_elements(By.XPATH, '//*[text() = "PREMINT Login"]')) >= 1:
            break
    # 승인 버튼 autorize로 바꿀수도?
    clickable(
        "/html/body/div[1]/div[2]/div/div[1]/div/div[2]/div/div/div/div[2]/button[2]",
        browser
    )
    logging.info("premint profile completed")


def dragons_register(browser):
    new_tab(
        "dragons",
        "https://digidaigaku.com/dragons",
        browser
    )
    logging.info("dragons start")
    # 지갑 연결
    time.sleep(2)
    ## 1번 버튼
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[1]",
        browser
    )
    ## 개인정보 동의
    clickable(
        "/html/body/div/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/p/input",
        browser
    )
    ##Connect Wallet button
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/div/div/div[2]/button",
        browser
    )
    ## metamask select
    clickable(
        "/html/body/div[2]/div/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/button",
        browser
    )
    # clickable("/html/body/div[2]/div/div/div[2]/div[1]/div",driver)

    # 지갑 연결중 화면 전환
    browser.implicitly_wait(10)
    time.sleep(2)
    browser.switch_to.window(browser.window_handles[-1])
    clickable(
        "/html/body/div[1]/div/div[2]/div/div[3]/div[2]/button[2]",
        browser)

    clickable(
        "/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div[2]/footer/button[2]",
        browser)

    # 버튼2
    browser.switch_to.window("dragons")
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[2]",
        browser
    )
    browser.switch_to.window("metamask_init")
    clickable(
        "/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button",
        browser
    )

    ## activity click
    clickable(
        "/html/body/div[1]/div/div[3]/div/div/div/div[3]/ul/li[2]/button",
        browser
    )

    ## accept click
    clickable(
        "/html/body/div[1]/div/div[3]/div/div/div/div[3]/div/div/div/div[1]/div[2]",
        browser
    )
    ### sign
    clickable(
        "/html/body/div[1]/div/div[3]/div/div[3]/button[2]",
        browser
    )

    # 버튼3
    browser.switch_to.window("dragons")

    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[3]",
        browser
    )
    ##캡챠
    WebDriverWait(driver, 140).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/form/fieldset/input[1]")))

    ## 트위터 연결 허용
    clickable(
        "/html/body/div[2]/div/form/fieldset/input[1]",
        browser
    )
    try:
        # 팔로우 완료 했으면 뜬다?
        clickable(
            "/html/body/div[1]/div/main/div/div[1]/div[2]/div[3]/div/div/div/div[2]/a",
            browser
        )
        # 새 트위청 뜨고
        browser.switch_to.window(browser.window_handles[-1])

        clickable(
            "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[1]",
            browser
        )
    except:
        pass

    browser.switch_to.window("dragons")
    clickable(
        "/html/body/div/div/main/div/div[1]/div[2]/div[3]/div/div/div/button",
        browser
    )

    # 4번
    clickable(
        "/html/body/div[1]/div/main/div/div[1]/div[2]/div[2]/div/div/div/div/button[4]",
        browser
    )

    # 성공
    success_phrase = textable(
        "//*[text() = 'Registration Complete!']",
        browser
    )
    if success_phrase:
        logging.info("dragons success")


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
            # 메타마스크 셋팅 함수
            metamask_setting(driver)
            # #트위터 팔로우

            login_twitter(driver, tweet_id[1833 - num_idx], tweet_password[1833 - num_idx], tweet_phone[1833 - num_idx],
                          cookie=tweet_cookie[1833 - num_idx])

            # should be excuted after url init
            # acp_api_send_request(
            #     driver,
            #     'setOptions',
            #     {'options': {'antiCaptchaApiKey': 'c48e6a0ade358666ec236e8b27244e58'}}
            # )
            # 드래곤스 등록
            dragons_register(driver)

            driver.quit()
            logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            logging.warning("success")
            logging.warning(f",,success")
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
        print("[%d/%d] Whole process Completed for %.2f" % (num_idx, 600, time.time() - start))
        logging.info("[%d/%d] Whole process Completed for %.2f" % (num_idx, 600, time.time() - start))
    logging.fatal(f"{failed}")
