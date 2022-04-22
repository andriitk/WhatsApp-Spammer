from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from pyfiglet import Figlet
from time import sleep
import keyboard
import datetime
import random

SER = Service("chromedriver.exe")


def get_file_lines(filename: str):
    try:
        with open(filename, encoding="utf-8") as f:
            symbols = f.read().split("\n")
            symbols = list(symbols)
            return symbols
    except FileNotFoundError:
        print(f"\n\033[31m\033[1m[ERROR]\033[0m Please check if file \033[31m\033[4m{filename}\033[0m exists\n")
        exit()


def send_wa_msg(phone_numbers: list, text: list):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=SER, options=options)

    try:
        driver.get(url='https://web.whatsapp.com/')
        sleep(15)

        for number in phone_numbers:
            number = number.strip()
            try:
                driver.get(url=f'https://web.whatsapp.com/send?phone={number}')
                WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
                text_box = driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                for line in text:
                    text_box.send_keys(line.strip())
                    text_box.send_keys(' ' * 180)
                keyboard.send('enter')
                cur_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(
                    f'\033[32m\033[1m[{cur_time} - GOOD]\033[0m \033[33m\033[1mMessage to\033[0m \033[31m\033[1m{number}\033[0m \033[33m\033[1msent successfully!\033[0m')
                sleep(random.randint(2, 5))

            except:
                cur_time = datetime.datetime.now().strftime("%H:%M:%S")
                print(
                    f'\033[31m\033[1m[{cur_time} - BAD]\033[0m \033[33m\033[1mMessage wasn`t sent to \033[31m\033[1m{number}\033[0m \033[33m\033[1m(((\033[0m')

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

        return 'Work done! Thanks for using, have a good day!'


def main():
    preview_text = Figlet(font='doom', width=200)
    title = preview_text.renderText('W h a t s A p p     S p a m m e r')
    print(f'\033[32m\033[1m{title}\033[0m')
    print("\033[32m\033[1m-\033[0m" * 125 + '\n')

    with open('text.txt', encoding='utf-8') as f:
        text = f.readlines()
    phone_numbers = get_file_lines('phone_numbers.txt')
    send_wa_msg(phone_numbers=phone_numbers, text=text)


if __name__ == '__main__':
    main()
