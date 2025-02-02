from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json

# Чтение конфигурации
with open('config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

def scen_1():
    try:
        driver = webdriver.Chrome()
        start_time = time.time()  # Запускаем таймер

        driver.get(data['url'])  # Открываем сайт
        driver.maximize_window() # Разворачиваем окно на весь экран
        time.sleep(1)  # Даем время на загрузку страницы
        
        current_url = driver.current_url # Получение текущего URL
        new_url = current_url + "more"  # Формирование нового URL                     
        driver.get(new_url) # Переход на новый URL
        time.sleep(3) # Ждем несколько секунд, чтобы увидеть результат
        
    finally:
        end_time = time.time()  # Завершаем таймер
        execution_time = end_time - start_time
        driver.quit() # Закрываем браузер
        return execution_time


if __name__ == '__main__':
    print(f"Время выполнения сценария 2, дополнительные задания: {scen_1():.2f} секунд")
