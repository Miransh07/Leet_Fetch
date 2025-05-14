from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time
def fetch(url):
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get(url)


    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ellipsis"))
    )
    # button = driver.find_element(By.ID, 'radix-:rl:')
    # button.click()
    line = driver.find_elements(By.CLASS_NAME, "ellipsis")
    Difficulties = driver.find_elements(By.CSS_SELECTOR, 'p.mx-0')
    script = """
    return Array.from(document.querySelectorAll('.text-sd-muted-foreground.flex'))
                .map(element => element.innerText.trim());
    """
    values = driver.execute_script(script)
    # Acceptance = driver.find_elements(By.CSS_SELECTOR, 'div.text-sd-muted-foreground.flex')
    lst = []
    for title, diff, acp in zip(line, Difficulties, values):
        d = {}
        x = title.text.split('. ')
        d['title'] = x[1]
        d['Question no.'] = x[0]
        d['Difficulty'] = diff.text
        d['Acceptance'] = acp
        lst.append(d)
    driver.quit()
    return lst
