import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from selenium_tools.common_tools import new_tab, clickable, textable


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
    WebDriverWait(browser, 140).until(
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
