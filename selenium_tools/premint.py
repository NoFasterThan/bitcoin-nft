from selenium_tools.common_tools import new_tab, clickable


def profile_premint(browser, token):
    import logging
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
