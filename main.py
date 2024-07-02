import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui

# Load your list of seat numbers and mothers' names from a CSV file
data = pd.read_csv('seat_numbers.csv')  # Assuming your file is named seat_numbers.csv


# URL of the results page
base_url = "https://onlineresults.unipune.ac.in/Result/Dashboard/Default"

# Setup Selenium WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(base_url)

# Wait for the page to load completely
time.sleep(2)

# Focus on the search bar
pyautogui.press('tab', presses=4)

# Enter the search term
search_term = "23- june"
pyautogui.write(search_term)
pyautogui.press('enter')

# Wait for the search results to load
time.sleep(2)

# Press tab once to navigate to the "Go for Result" button and hit enter
pyautogui.press('tab')
time.sleep(0.5)
pyautogui.press('enter')

# Wait for the result page to load
time.sleep(2)

# Function to wait for an element
def wait_for_element(by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, value))
    )

for index, row in data.iterrows():
    seat_number = row['SeatNumber']
    mothers_name = row['MothersName']

    try:
        # Find and fill the seat number field
        seat_number_field = wait_for_element(By.NAME, 'SeatNo')
        seat_number_field.clear()
        seat_number_field.send_keys(seat_number)

        # Find and fill the mother's name field
        mothers_name_field = wait_for_element(By.NAME, 'MotherName')
        mothers_name_field.clear()
        mothers_name_field.send_keys(mothers_name)

        # Find and click the "Check Result" button
        check_result_button = wait_for_element(By.ID, 'btn')
        check_result_button.click()

        # Wait for the result to load
        time.sleep(9)  # Adjust the sleep time if necessary

        # Save the result as a PDF  
        pyautogui.hotkey('ctrl', 'p')
        time.sleep(1)  # Wait for the print dialog to open
        pyautogui.press('enter')
        time.sleep(1)

        # Enter the seat number as the PDF name
        pyautogui.write(f"{seat_number}")
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(3)  # Wait for the save dialog to close

        # Go back to the main results page
        driver.get(base_url)

        # Re-perform the search to get back to the results
        time.sleep(2)
        pyautogui.press('tab', presses=4)
        pyautogui.write(search_term)
        pyautogui.press('enter')
        time.sleep(2)
        pyautogui.press('tab')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(2)  # Wait for the result page to load again

    except Exception as e:
        print(f"Error processing seat number {seat_number}: {str(e)}")

print("All results downloaded.")
driver.quit()