from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

chrome_options = webdriver.ChromeOptions()    
# Add your options as needed    
options = [
  # Define window size here
   "--window-size=1200,1200",
    "--ignore-certificate-errors"
 
    #"--headless",
    #"--disable-gpu",
    #"--window-size=1920,1200",
    #"--ignore-certificate-errors",
    #"--disable-extensions",
    #"--no-sandbox",
    #"--disable-dev-shm-usage",
    #'--remote-debugging-port=9222'
]

for option in options:
    chrome_options.add_argument(option)
   
driver = webdriver.Chrome(options = chrome_options)

# Set the path to the ChromeDriver inside the 'drivers/' folder
# driver_path = os.path.join(os.path.dirname(__file__), 'drivers', 'chromedriver')

# Initialize the WebDriver with the specified path
# driver = webdriver.Chrome(service=Service(driver_path))

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
