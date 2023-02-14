from selenium_tools.common_tools import acp_api_send_request


def set_captcha_key(browser):
    acp_api_send_request(
        browser,
        'setOptions',
        {'options': {'antiCaptchaApiKey': 'c48e6a0ade358666ec236e8b27244e58'}}
    )