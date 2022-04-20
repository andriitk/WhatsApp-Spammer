from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = 'chromedriver.exe'
options = webdriver.ChromeOptions()
# options.add_argument('headless')

driver = webdriver.Chrome(executable_path=PATH, options=options)


def get_file_lines(filename: str):
    try:
        with open(filename, encoding="utf-8") as f:
            symbols = f.read().split("\n")
            symbols = set(symbols)
            symbols = list(symbols)
            return symbols
    except FileNotFoundError:
        print(f"\n\033[31m\033[1m[ERROR]\033[0m Please check if file \033[31m\033[4m{filename}\033[0m exists\n")
        exit()


def send_wa_msg(phone_numbers: list, text):
    try:
        driver.get(url='https://web.whatsapp.com/')
        sleep(10)

        for number in phone_numbers:
            number = number.strip()
            try:
                driver.get(url=f'https://web.whatsapp.com/send?phone={number}')
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,
                                                                                  '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')))
                text_box = driver.find_element(By.XPATH,
                                               '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
                sleep(5)
                text_box.send_keys(text)
                text_box.send_keys('\n')

                print(f'The message was sent to {number} sent success!')
                sleep(5)

            except Exception as ex:
                print(f'The message wasn`t sent to {number} (((')

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

        return 'Work done! Thanks for using, have a good day!'


def main():
    with open('text.txt', encoding='utf-8') as f:
        text = f.read()
    text = text
    phone_numbers = get_file_lines('phone_numbers.txt')
    send_wa_msg(phone_numbers=phone_numbers, text=text)


if __name__ == '__main__':
    main()
