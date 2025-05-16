from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pymongo


class FetchFromMongo:
    def __init__(self, url):
        self.url = url
        self.client = pymongo.MongoClient('mongodb://localhost:27017')
        self.db = self.client['mydb']
        self.collection = self.db['questions']

    def fetch(self) -> list:
        driver = webdriver.Chrome()
        # driver.maximize_window()
        driver.get(self.url)

        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "ellipsis"))
        )
        # button = driver.find_element(By.ID, 'radix-:rl:')
        # button.click()
        line = driver.find_elements(By.CLASS_NAME, "ellipsis")
        difficulties = driver.find_elements(By.CSS_SELECTOR, 'p.mx-0')
        script = """
        return Array.from(document.querySelectorAll('.text-sd-muted-foreground.flex'))
                    .map(element => element.innerText.trim());
        """
        values = driver.execute_script(script)
        # Acceptance = driver.find_elements(By.CSS_SELECTOR, 'div.text-sd-muted-foreground.flex')
        lst = []
        for title, diff, acp in zip(line, difficulties, values):
            d = {}
            x = title.text.split('. ')
            d['title'] = x[1]
            d['Question no.'] = x[0]
            d['Difficulty'] = diff.text
            d['Acceptance'] = acp
            lst.append(d)
        driver.quit()
        return lst

    def get_mongo_collection(self):
        return self.collection

    def fetch_data_and_insert_in_mongo(self) -> None:
        mylist = self.fetch()
        self.collection.insert_many(mylist)

    def get_all_data(self):
        all_values = []
        for x in self.collection.find():
            x.pop('_id')
            all_values.append(x)
        return all_values
