from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# --- CONFIGURATION ---
EMAIL = "email@email.com"         # Replace with your Naukri login email
PASSWORD = "password"          # Replace with your Naukri password
NEW_SUMMARY = "Software Developer with 3 years of experience in building high-performance web apps using Java, Spring Boot, JPA, SQL, and React. Skilled in integrating APIs, AWS services, and object detection models. Passionate about performance optimization."  # Update this daily if you want

# Path to chromedriver.exe (you can leave blank if it's in the same folder or in PATH)
CHROME_DRIVER_PATH = "C:/Users/Gagan/Downloads/chrome-win64/chrome-win64"  # or full path like "C:/path/to/chromedriver.exe"

# --- SETUP CHROME ---
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:

    # --- STEP 1: Open Naukri and Login ---
    driver.get("https://www.naukri.com/")
    time.sleep(3)

    driver.find_element(By.ID, "login_Layer").click()
    time.sleep(2)

    email_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")
    email_input.send_keys(EMAIL)
    time.sleep(1)

    password_input = driver.find_element(By.XPATH, "//input[@placeholder='Enter your password']")
    password_input.send_keys(PASSWORD)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # --- STEP 2: Go to Profile Page ---
    driver.get("https://www.naukri.com/mnjuser/profile")
    time.sleep(5)

    # --- STEP 3: Click 'Edit' in Resume Headline Section ---
    edit_button = driver.find_element(By.XPATH, "//div[@id='lazyResumeHead']//span[@class='edit icon']")
    edit_button.click()
    time.sleep(2)

    # --- STEP 4: Update the Resume Headline TextArea ---
    textarea = driver.find_element(By.ID, "resumeHeadlineTxt")
    driver.execute_script("arguments[0].scrollIntoView(true);", textarea)
    time.sleep(1)

    textarea.clear()
    textarea.click()
    time.sleep(1)

    # Simulate typing the new summary
    textarea.send_keys(NEW_SUMMARY)
    time.sleep(2)

    # Blur to trigger change detection (if React or JS needs it)
    driver.execute_script("arguments[0].blur();", textarea)
    time.sleep(1)

    # --- STEP 5: Save the changes ---
    save_button = driver.find_element(By.XPATH, "//form[@name='resumeHeadlineForm']//button[text()='Save']")
    save_button.click()
    time.sleep(3)

    print("✅ Resume headline updated successfully!")

except Exception as e:
    print("❌ Error occurred:", e)

finally:
    # --- Close browser ---
    driver.quit()
