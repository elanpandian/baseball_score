from flask import Flask, render_template_string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
import time

# Initialize the Flask application
app = Flask(__name__)

# HTML template to render scores
HTML_TEMPLATE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Baseball Scores</title>
  </head>
  <body>
    <h1>Baseball Playoff Scores</h1>
    {% if scores %}
      <ul>
        {% for score in scores %}
          <li>{{ score }}</li>
        {% endfor %}
      </ul>
    {% else %}
      <p>No scores available or an error occurred.</p>
    {% endif %}
  </body>
</html>
"""

@app.route('/')
def get_scores():
    # Start virtual display (required for headless servers like in some CI environments)
    display = Display(visible=0, size=(800, 800))
    display.start()

    # Auto-install the correct version of ChromeDriver
    chromedriver_autoinstaller.install()

    # Set up Chrome options for Selenium
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1200,1200")
    chrome_options.add_argument("--ignore-certificate-errors")

    # Initialize Selenium WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the sports website (e.g., ESPN, MLB)
        driver.get('https://www.espn.com/mlb/scoreboard')

        # Wait for the scoreboard to load
        time.sleep(5)

        # Retrieve scores (adjust the selector as per the website's structure)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.scoreboard'))
        )
        scores_elements = driver.find_elements(By.CSS_SELECTOR, '.scoreboard .team-score')

        # Extract text from each score element
        scores = [score.text for score in scores_elements if score.text]

    except Exception as e:
        print(f"Error fetching scores: {e}")
        scores = ["Error fetching scores"]

    finally:
        # Close the browser session
        driver.quit()
        display.stop()

    # Render the results on a webpage using Flask
    return render_template_string(HTML_TEMPLATE, scores=scores)

if __name__ == '__main__':
    app.run(debug=True)
