from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Replace with the path to your ChromeDriver
chrome_driver_path = '/path/to/chromedriver'

# Initialize WebDriver
driver = webdriver.Chrome(service=Service(chrome_driver_path))

# Open the sports website (e.g., ESPN, MLB)
driver.get('https://www.espn.com/mlb/scoreboard')

# Give the page some time to load
time.sleep(5)

# Locate elements that contain scores of completed matches
# Example: Find elements by their CSS class names that might contain the scores.
# The following is an example and needs to be adapted based on the website's structure.
try:
    # Wait until the score elements are loaded (adjust CSS selectors as needed)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.scoreboard'))
    )
    
    # Retrieve all score elements (this selector is an example)
    scores = driver.find_elements(By.CSS_SELECTOR, '.scoreboard .team-score')
    
    # Extract and print the scores
    for score in scores:
        print(score.text)

except Exception as e:
    print(f"Error fetching scores: {e}")

# Close the browser session
driver.quit()
