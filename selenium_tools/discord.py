import logging
import time
from lib2to3.pgen2 import driver
from common_tools import clickable, new_tab
from selenium.webdriver.common.by import By
import random
import common_tools


def login_discord(token, browser, new_browser=False):
    if new_browser:
        browser.get("https://discord.com")
    else:
        common_tools.new_tab(
            "discord",
            "https://discord.com",
            browser
        )

    logging.info("discord login start")

    for _ in range(30):
        browser.execute_script(token)
        if len(browser.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[1]/header[2]/nav/div[2]/a')) >= 1:
            break
    # open discord
    common_tools.clickable(
        "/html/body/div[1]/div/div/div[1]/div[1]/header[2]/nav/div[2]/a",
        browser
    )

    logging.info("discord login complete")
    time.sleep(2)


def invite_discord(browser, invite_code, new_browser=False):
    if new_browser:
        browser.get(f"https://discord.com/invite/{invite_code}")
    else:
        common_tools.new_tab(
            "discord_invite",
            f"https://discord.com/invite/{invite_code}",
            browser
        )

    logging.info("discord invite start")
    common_tools.clickable(
        "//*[text()='Accept Invite']",
        browser
    )
    # TODO: 디스코드 초대 프로세스: 캡챠 우회, 로그인 후 롤 따기

    # 팝업창 제거
    common_tools.clickable('/html/body', driver)
    common_tools.clickable('/html/body', driver)

    logging.info("discord invite complete")
    time.sleep(2)

def disconnect_discord(browser, login_completed=True, token=None):
    logging.info("disconnecting discord")
    if not login_completed:
        login_discord(browser, token)
    new_tab(
        "discord_disconnect",
        "https://premint.xyz/disconnect",
        browser
    )
    time.sleep(random.randint(1, 2) + random.random())
    clickable(
        "/html/body/div[1]/div/div/div/div/section/div/div/div/div/div[3]/a[2]",
        browser
    )
    for i in range(30):
        browser.execute_script(token)
        if i % 10 == 0 and len(browser.find_elements(By.XPATH, '//*[text() = "PREMINT Login"]')) >= 1:
            break
    clickable(
        "/html/body/div[1]/div[2]/div/div[1]/div/div/div/div/div/div[2]/button[2]",
        browser
    )
    logging.info("discord disconnect completed")
