import base64
import logging
import random
from lib2to3.pgen2 import driver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common_tools import *


def login_twitter(browser, username, password, phone_number, cookie, new_browser=False):
    try:
        if new_browser:
            browser.get("https://twitter.com/login")
        else:
            new_tab(
                "twitter",
                "https://twitter.com/login",
                browser,
            )
        decoded = (base64.b64decode(cookie).decode('UTF-8'))
        decoded = json.loads(decoded)

        for cookie in decoded:
            try:
                if cookie['sameSite'] == 'unspecified':
                    del cookie['sameSite']

                if cookie['sameSite'] == 'lax':
                    cookie['sameSite'] = 'Lax'
            except:
                continue

            browser.add_cookie(cookie)
        ##captcha key injection
        acp_api_send_request(
            browser,
            'setOptions',
            {'options': {'antiCaptchaApiKey': 'c48e6a0ade358666ec236e8b27244e58'}}
        )
        logging.info("twitter login start")
        username_field = WebDriverWait(browser, 18).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@autocomplete="username"]')))
        username_field.click()
        username_field.send_keys(username)
        username_field.send_keys(Keys.ENTER)
        browser.implicitly_wait(5)

        password_field = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//input[@name="password"]')))
        # password_field.click()

        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)
        browser.implicitly_wait(15)

        if len(browser.find_elements(By.XPATH,
                                     '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')) != 0:
            # print("번호인증")
            # browser.quit()
            phone_box = browser.find_elements(By.XPATH,
                                              '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
            phone_box[0].send_keys(phone_number)
            phone_box[0].send_keys(Keys.ENTER)

        # 개인정보 확인
        # //*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div

        browser.implicitly_wait(10)
        time.sleep(3)

        if len(browser.find_elements(By.XPATH,
                                     '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div')) != 0:
            # print("번호인증")
            # browser.quit()
            private_verify = browser.find_elements(By.XPATH,
                                                   '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/div')
            private_verify[0].click()
            clickable(
                "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]",
                browser
            )
        if len(notice_verify_list := browser.find_elements(By.XPATH,
                                                           '//*[text() = "Skip for now"]')) != 0:
            # print("번호인증")
            # browser.quit()
            notice_verify_list[0].click()
            clickable(
                "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]",
                browser
            )

        clickable('/html/body', browser)
        if len(alert_button := browser.find_elements(By.XPATH,
                                                     '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]/div')):

            alert_button[0].send_keys(Keys.ENTER)

        if len(my_num := browser.find_elements(By.XPATH,
                                               "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[2]/div[1]")):

            my_num[0].send_keys(Keys.ENTER)

        if len(review_your_phone := browser.find_elements(By.XPATH,
                                                          "//*[text() = 'Yes, that is my number']")) != 0:
            browser.implicitly_wait(10)

            review_your_phone[0].send_keys(Keys.ENTER)

        logging.info("twitter login completed")

        logging.info("twitter follow start")

        twitter_follow(
            "@notablesart",
            browser
        )
        #홈버튼
        clickable(
            "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[1]",
            browser
        )

        twitter_follow(
            "@0xDith",
            browser
        )
        logging.info("twitter follow completed")

    except Exception as e:
        logging.info("twitter login failed")
        logging.info(f"{username}")
        print("예외가 발생했습니다.", str(e))


def twitter_follow(twitter_id ,browser):
    ##검색창에 검색
    sendable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input",
        twitter_id,
        browser
    )
    browser.implicitly_wait(5)
    # people 클릭
    clickable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div/span",
        browser
    )
    time.sleep(random.randint(0, 1) + random.random())
    # follow 클릭
    clickable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div",
        browser
    )
    time.sleep(random.random())
    if len(cancel_box := browser.find_elements(By.XPATH,
                                               '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div')) != 0:
        # 이중 클릭시 언팔로우 안하는 방지 코드
        cancel_box[0].click()
    time.sleep(random.randint(1, 2) + random.random())
    # follow 클릭
    clickable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[2]/div",
        browser
    )
    time.sleep(random.random())
    if len(cancel_box := browser.find_elements(By.XPATH,
                                               '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div[2]/div[2]/div')) != 0:
        # 이중 클릭시 언팔로우 안하는 방지 코드
        cancel_box[0].click()
    time.sleep(random.randint(1, 2) + random.random())
    clickable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span",
        browser
    )
    time.sleep(random.randint(1, 2) + random.random())
    logging.info(f"twitter {twitter_id} follow completed")


def disconnect_twitter(browser, login_completed=True, username=None, password=None, phone_number=None, cookie=None):
    logging.info("twitter disconnecting")
    if not login_completed:
        login_twitter(browser, username, password, phone_number, cookie)
    new_tab(
        "twitter_disconnect",
        "https://premint.xyz/disconnect",
        browser
    )
    time.sleep(random.randint(1, 2) + random.random())
    clickable(
        "/html/body/div/div/div/div/div/section/div/div/div/div/div[3]/a[1]",
        browser
    )
    clickable(
        "/html/body/div[2]/div/form/fieldset/input[1]",
        browser
    )
    browser.implicitly_wait(10)
    if len(browser.find_elements(By.XPATH, '//*[text() = "Create account with wallet"]')) >= 1:
        logging.info("twitter disconnect completed")
    else:
        logging.info("twitter disconnect failed")

def twitter_retweet_with_url(browser, url, retweet_name, login_completed=True, username=None, password=None, phone_number=None, cookie=None, tweet_contents = None):
    logging.info("twitter_retweet_with_url start")
    if not login_completed:
        login_twitter(browser, username, password, phone_number, cookie)
    new_tab(
        retweet_name,
        url,
        browser
    )

    reweet_action = ActionChains(browser)
    reweet_action.move_to_element(
        tweet_box := browser.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[1]/div/div/div/div/div/label/div[1]/div/div/div/div"
        )
    )
    reweet_action.click(
        tweet_box
    )
    reweet_action.perform()

    sendable(
        "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/section/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div",
        tweet_contents,
        browser
    )

    clickable(
        "//*[text()='Reply']",
        browser
    )


