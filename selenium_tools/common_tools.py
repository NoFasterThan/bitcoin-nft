# -*- coding: utf-8 -*-

import json
import logging
import time

from requests import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait




def acp_api_send_request(driver, message_type, data={}):
    message = {
        # this receiver has to be always set as antiCaptchaPlugin
        'receiver': 'antiCaptchaPlugin',
        # request type, for example setOptions
        'type': message_type,
        # merge with additional data
        **data
    }
    # run JS code in the web page context
    # preceicely we send a standard window.postMessage method
    return driver.execute_script("""
    return window.postMessage({});
    """.format(json.dumps(message)))


def smartproxy(HOSTNAME, PORT, DRIVER='CHROME'):
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    prox.ssl_proxy = '{hostname}:{port}'.format(hostname=HOSTNAME, port=PORT)
    if DRIVER == 'FIREFOX':
        capabilities = webdriver.DesiredCapabilities.FIREFOX
    elif DRIVER == 'CHROME':
        capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    return capabilities


def ip_swap():
    # win = gw.getWindowsWithTitle('COOL IP - jo123')
    time.sleep(0.1)


def ip_vpn():
    current_ip = get("https://api.ipify.org").text
    ip_swap()
    change_ip = get("https://api.ipify.org").text

    print(" [*] Current IP: %s / Changed IP: %s" % (current_ip, change_ip))

    if current_ip == change_ip:
        while True:
            print(current_ip, change_ip)
            ip_swap()
            change_ip = get("https://api.ipify.org").text

            if current_ip != change_ip:
                print(" [*] IP address is changed!")
                break
            time.sleep(2)

    return change_ip


def clickable(path, driver):
    driver.implicitly_wait(10)
    clk = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    clk.click()


def textable(path, driver):
    driver.implicitly_wait(10)
    clk = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    return clk.text


def sendable(path, keys, driver):
    driver.implicitly_wait(10)
    send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    send.send_keys(keys)


def new_tab(tab_name, tab_url, driver):
    driver.execute_script("window.open('about:blank', '%s');" % tab_name)
    driver.switch_to.window(tab_name)
    driver.get(tab_url)
    driver.implicitly_wait(10)
    time.sleep(1)
