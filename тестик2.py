from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Сценарий 2
def scen_2():
    try:
        driver = webdriver.Chrome()
        start_time = time.time()  # Запускаем таймер

        # Открываем сайт
        driver.get("http://127.0.0.1:5000/")

        # Разворачиваем окно на весь экран
        driver.maximize_window()
        
        # Даем время на загрузку страницы
        time.sleep(1)
        
        # Получение текущего URL
        current_url = driver.current_url
        # Формирование нового URL
        new_url = current_url + "more"
        # Переход на новый URL
        driver.get(new_url)
        
        # Ждем несколько секунд, чтобы увидеть результат
        time.sleep(3)

    finally:
        end_time = time.time()  # Завершаем таймер
        execution_time = end_time - start_time
        
        # Закрываем браузер
        driver.quit()
        return execution_time



print(f"Время выполнения сценария 2, 'как посмотреть дополнительные задания?': {scen_2():.2f} секунд")
