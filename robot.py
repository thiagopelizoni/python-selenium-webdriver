import sys
import pytest
import pytz
import pathlib
import argparse
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

elemental_url = "http://172.16.2.172/users/sign_in"
elemental_login = "login_here"
elemental_password = "password_here"

headless = True

def log(message):
    now = datetime.now(pytz.timezone('America/Sao_Paulo')).strftime('%d/%m/%Y %H:%M:%S')
    print(f"[{now}]: {message}")

def get_options():
    options = Options()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-setuid-sandbox")

    if headless:
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')

    return options

def restart_elemental():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=get_options())
    driver.implicitly_wait(7)

    driver.get(elemental_url)
    driver.maximize_window()

    user_login = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[1]")
    user_login.send_keys(elemental_login)

    user_password = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/input[2]")
    user_password.send_keys(elemental_password)

    submit_login = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[3]/div/a")
    submit_login.submit()

    stop_streaming = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/form/div[2]/table/tbody/tr[1]/td[13]/div[2]/div/i")
    stop_streaming.click()
    sleep(15)

    refresh_streaming = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/form/div[2]/table/tbody/tr[1]/td[13]/div[3]/div/i")
    refresh_streaming.click()
    sleep(15)

    start_streaming = driver.find_element(By.XPATH, "/html/body/div[2]/div[2]/div/div[2]/form/div[2]/table/tbody/tr[1]/td[13]/div[1]/div/i")
    start_streaming.click()
    log("O Elemental foi reiniciado com sucesso!")
    sleep(10)

vimeo_url = "https://vimeo.com/log_in"
vimeo_login = "login_here"
vimeo_password = "password_here"
vimeo_event_url = "https://vimeo.com/manage/events/2229728/preview#destinations"

def vimeo():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=get_options())
    driver.implicitly_wait(10)

    driver.get(vimeo_url)
    driver.maximize_window()

    user_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/article/div/div/div/div/form/div[2]/input")
    user_login.send_keys(vimeo_login)

    user_password = driver.find_element(By.XPATH, "/html/body/div[1]/div/article/div/div/div/div/form/div[3]/input")
    user_password.send_keys(vimeo_password)

    submit_login = driver.find_element(By.XPATH, "/html/body/div[1]/div/article/div/div/div/div/form/div[8]/input")
    submit_login.click()
    sleep(10)

    driver.get(vimeo_event_url)
    sleep(10)
    return driver

def vimeo_end_event():
    driver = vimeo()
    end_event = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div[1]/div[2]/button[2]")
    end_event.click()
    log(f"Evento {vimeo_event_url} encerrado")
    sleep(5)

def vimeo_go_live():
    driver = vimeo()
    go_live = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div/div[1]/div[2]/div/div[2]/div[1]/span/div/button")
    go_live.click()
    log(f"Evento {vimeo_event_url} iniciado")

def get_vimeo_current_video_id():
    driver = vimeo()

    vimeo_event_2229728_url = "https://vimeo.com/event/2229728"
    driver.get(vimeo_event_2229728_url)
    sleep(5)

    return driver.current_url.split("/")[-2]

def run():
    try:
        vimeo_end_event()
    except:
        log("Erro ao finalizar evento na Vimeo")
    sleep(10)

    try:
        restart_elemental()
    except:
        log("Erro ao reiniciar o serviço Elemental")
    sleep(10)

    try:
        vimeo_go_live()
    except:
        log("Erro ao executar o GoLive")
    sleep(10)

def main():
    log("Inicio da execução do robô")
    run()
    log("Fim da execução do robô")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Habilita a execução direta via browser")
    parser.add_argument("--no-headless", dest="headless", action='store_false')

    headless = parser.parse_args().headless

    main()
