from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the driver
driver = webdriver.Chrome()
driver.get("https://leetcode.com/problemset/")

# Wait for the filter button to appear
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Difficulty')]"))
)

# Click on the Difficulty filter
difficulty_filter = driver.find_element(By.XPATH, "//button[contains(text(), 'Difficulty')]")
difficulty_filter.click()
time.sleep(1)  # Small delay to allow filter options to load

# Selecting "Medium" difficulty from the dropdown
medium_option = driver.find_element(By.XPATH, "//button[contains(text(), 'Medium')]")
medium_option.click()
time.sleep(3)  # Wait for filter to apply

# Fetching filtered problem titles
problems = driver.find_elements(By.CLASS_NAME, "ellipsis")

print("Filtered Problems (Medium):")
for problem in problems:
    print(problem.text)

driver.quit()
