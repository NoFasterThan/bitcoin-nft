from common_tools import *


def save_pharse_address(seed, address, key):
    if not os.path.isfile("seed_address.txt"):
        f = open("seed_address.txt", 'w')
        f.close()

    with open("seed_address.txt", "a") as f:
        f.write(seed)
        f.write(':')
        f.write(address)
        f.write(':')
        f.write(key)
        f.write("\n")
    logging.info(f"{seed},{address},{key}")


pw = '12345678'  # 메타마스크 비밀번호 (전부다 똑같음)
num_account = 1  # 봇돌릴 계정 갯수 입력
mm_path = r'selenium_mekaverse_drivers\selenium_function\metamask-10.12.4-an+fx.xpi'  # 본인에 맞게 수정해야함 참고로 윈도우에선 \ 이고 맥이나 우분투에선 /로 디렉토리 구분


def seed_puzzle(seed_phrase, driver):
    seed_length = 12
    driver.implicitly_wait(5)
    seed_list = []

    for seed_idx in range(seed_length):
        instance = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div[5]/div[%d]' % (seed_idx + 1))))
        seed_list.append(instance.text)

    true_seed = seed_phrase.split(' ')

    for s_idx in range(seed_length):
        for c_idx in range(seed_length):
            if true_seed[s_idx] == seed_list[c_idx]:
                clickable('/html/body/div[1]/div/div[2]/div/div/div[2]/div[5]/div[%d]' % (c_idx + 1), driver)
                # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[2]/div[5]/div[%d]' % (c_idx + 1)).click()
            else:
                pass

    clickable('/html/body/div[1]/div/div[2]/div/div/div[2]/button', driver)
    clickable('/html/body/div[1]/div/div[2]/div/div/button', driver)


def metamask_setting(browser, extension_id="nkbihfbeogaeaoehlefnkodbefgpgknn", ):
    new_tab(
        "metamask_init",
        f"chrome-extension://{extension_id}/home.html#initialize/welcome",
        browser
    )
    # 화면 전체화 하고 메타마스크 비번 치고 클릭클릭 넘어감
    # driver.switch_to.window(driver.window_handles[1])
    # 시작하기
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div/button",
        browser
    )
    # 새로운 지갑 생성
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[2]/div[2]/button",
        browser
    )
    # 개인정보 동의
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div/div[5]/div[1]/footer/button[2]",
        browser
    )
    # 비밀번호 입력
    sendable(
        '//*[@id="create-password"]',
        pw,
        browser)
    sendable('//*[@id="confirm-password"]',
             pw,
             browser)
    # 비밀번호 이용약관 동의
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/div",
        browser
    )

    # 비밀번호 저장
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div[2]/form/button",
        browser
    )
    # error prevent
    time.sleep(2)
    # 시드 안내 영상
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div[2]/button",
        browser
    )
    # 시드 오픈
    clickable(
        "/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div[2]",
        browser
    )

    # 시드 텍스트
    seed_phrase = browser.find_element(
        by=By.XPATH,
        value='/html/body/div[1]/div/div[2]/div/div/div[2]/div[1]/div[1]/div[5]/div') \
        .text

    # 시드 텍스트 다음
    clickable('/html/body/div[1]/div/div[2]/div/div/div[2]/div[2]/button[2]', browser)

    # 시드구문 퍼즐 푸는 함수하고 클릭클릭
    browser.implicitly_wait(3)
    time.sleep(1)
    seed_puzzle(seed_phrase, browser)
    time.sleep(2)

    # 점 세개 누르고
    clickable('/html/body/div[1]/div/div[3]/div/div/div/div[1]/button', browser)
    clickable('/html/body/div[2]/div[2]/button[2]', browser)
    time.sleep(1)

    # 주소랑 프라이빗 키 저장
    address = textable('/html/body/div[1]/div/span/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]', browser)
    clickable('/html/body/div[1]/div/span/div[1]/div/div/div/button[3]', browser)
    sendable('/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/input', pw, browser)
    clickable('/html/body/div[1]/div/span/div[1]/div/div/div/div[7]/button[2]', browser)
    pri_key = textable('/html/body/div[1]/div/span/div[1]/div/div/div/div[5]/div', browser)

    # 메마 접속 완료하고 시드, 주소, 프빗키 저장
    save_pharse_address(seed_phrase, address, pri_key)
