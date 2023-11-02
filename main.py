import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import cprint
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyautogui
import time 
import keyboard
from pynput.keyboard import Key, Controller

def open_new_tab(driver, url):
    driver.execute_script(f'console.log("Открываю новую вкладку");')
    driver.execute_script(f'window.open("{url}", "_blank");')
    driver.execute_script(f'console.log("Новая вкладка открыта");')

def main(zero, ads_id):
    driver = None  

    try:
        open_url = "http://local.adspower.net:50325/api/v1/browser/start?user_id=" + ads_id
        close_url = "http://local.adspower.net:50325/api/v1/browser/stop?user_id=" + ads_id

        resp = requests.get(open_url).json()
        cprint(f"Ответ от сервера: {resp}", "yellow")

        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", resp["data"]["ws"]["selenium"])
        
        # Создание экземпляра браузера
        driver = webdriver.Chrome(options=chrome_options)
        cprint("Браузер успешно запущен", "green")
        
        for handle in driver.window_handles:
            driver.switch_to.window(handle)
            if "acc_id" in driver.current_url:
                break
        time.sleep(2)
        xpath = "/html/body/div[2]/div[1]/div[3]/div[1]/div[2]"
        element = driver.find_element(By.XPATH, xpath)
        serial_number = element.text
        print("Значение serial_number:", serial_number)

        
        
        

        # Попробуем нажать клавиши Alt+Shift+M
        keyboard = Controller()
        time.sleep(2)
        keyboard.press(Key.alt)
        keyboard.press(Key.shift)
        keyboard.press('m')
        keyboard.release('m')
        keyboard.release(Key.shift)
        keyboard.release(Key.alt)
        time.sleep(2)




        driver.switch_to.window(driver.window_handles[-1])

        print("Ищу кнопку импорт...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/ul/li[2]/button'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")
        


        print("Ищу кнопку...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div/button[2]'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        driver.switch_to.default_content()

        serial_number = int(serial_number)
        words = "слова слова слова слова"
        wordsArray = words.split(' ')
        chunkSize = 12
        resultArray = []

        for i in range(0, len(wordsArray), chunkSize):
            chunk = wordsArray[i:i + chunkSize]
            resultArray.append(chunk)

        id_element = serial_number - 200

        if id_element < 0:
            id_element = 200 - serial_number

        firstElement = resultArray[id_element]
        joinedWords = ' '.join(firstElement)
        seeed = joinedWords.split(" ")

        for i in range(12):
            globals()['word' + str(i + 1)] = seeed[i] if i < len(seeed) else ""

        
        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-0')) #1
        )
        
        element.clear()  
        element.send_keys(word1)

        print(f'Текст введен в элемент word1: {word1}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-1')) #2
        )
        
        element.clear()  
        element.send_keys(word2)

        print(f'Текст введен в элемент word2: {word2}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-2')) #3
        )
        
        element.clear()  
        element.send_keys(word3)

        print(f'Текст введен в элемент word3: {word3}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-3'))
        )
        
        element.clear()  
        element.send_keys(word4)

        print(f'Текст введен в элемент word4: {word4}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-4'))
        )
        
        element.clear()  
        element.send_keys(word5)

        print(f'Текст введен в элемент word5: {word5}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-5'))
        )
        
        element.clear()  
        element.send_keys(word6)

        print(f'Текст введен в элемент word6: {word6}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-6'))
        )
        
        element.clear()  
        element.send_keys(word7)

        print(f'Текст введен в элемент word7: {word7}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-7'))
        )
        
        element.clear()  
        element.send_keys(word8)

        print(f'Текст введен в элемент word8: {word8}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-8'))
        )
        
        element.clear()  
        element.send_keys(word9)

        print(f'Текст введен в элемент word9: {word9}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-9'))
        )
        
        element.clear()  
        element.send_keys(word10)

        print(f'Текст введен в элемент word10: {word10}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-10'))
        )
        
        element.clear()  
        element.send_keys(word11)

        print(f'Текст введен в элемент word11: {word11}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#import-srp__srp-word-11'))
        )
        
        element.clear()  
        element.send_keys(word12)

        print(f'Текст введен в элемент word12: {word12}')

        print("Ищу кнопку...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[4]/div/button'
        wait = WebDriverWait(driver, 30)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        password = 43211234

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#app-content > div > div.main-container-wrapper > div > div > div > div.box.box--margin-top-3.box--flex-direction-row.box--justify-content-center.box--display-flex > form > div:nth-child(1) > label > input'))
        )
        
        element.clear()  
        element.send_keys(password)
        print(f'Текст введен в элемент password1: {password}')

        element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#app-content > div > div.main-container-wrapper > div > div > div > div.box.box--margin-top-3.box--flex-direction-row.box--justify-content-center.box--display-flex > form > div:nth-child(2) > label > input'))
        )
        
        element.clear()  
        element.send_keys(password)
        print(f'Текст введен в элемент password2: {password}')

        print("Ищу кнопку...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        print("Ищу кнопку...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        print("Ищу кнопку понятно...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        print("Ищу кнопку понятно2...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        print("Ищу кнопку далее...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
        wait = WebDriverWait(driver, 10)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")

        print("Ищу кнопку выполнено...")
        button_xpath = '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/button'
        wait = WebDriverWait(driver, 5)  # Максимальное время ожидания - 10 секунд
        button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))

        if button:
            print("Кнопка найдена. Нажимаю на кнопку...")
            actions = ActionChains(driver)
            actions.move_to_element(button).click().perform()
            print("Кнопка нажата.")
        else:
            print("Кнопка не найдена.")


        keyboard = Controller()
        time.sleep(2)
        keyboard.press(Key.alt)
        keyboard.press(Key.shift)
        keyboard.press('m')
        keyboard.release('m')
        keyboard.release(Key.shift)
        keyboard.release(Key.alt)
        time.sleep(2)
        print("Ну что, вроде всё")


        driver.switch_to.window(driver.window_handles[-1])



               


    except Exception as e:
            print(f'An error occurred: {e}')

    except Exception as ex:
        cprint(f"Произошла ошибка: {ex}", "red")
        if driver is not None:
            driver.quit()  # Закрываем браузер в случае ошибки
        requests.get(close_url)
        cprint("Браузер успешно закрыт", "yellow")

    finally:
        driver.close()
        requests.get(close_url)


with open("/Users/nimble/Desktop/launch/id_users.txt", "r") as f:
    id_users = [row.strip() for row in f]

for zero, ads_id in enumerate(id_users):
    main(zero, ads_id)


