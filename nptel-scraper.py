from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
load_dotenv()
import time
import os

# === Step 1: Take Credentials ===
email = os.getenv("SWAYAM_EMAIL")
password = os.getenv("SWAYAM_PASSWORD")

# === Setup Chrome Driver ===
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

wait = WebDriverWait(driver, 20)

# === Step 2: Open My Courses page directly ===
driver.get("https://swayam.gov.in/mycourses")

# === Step 3: Click Microsoft Login ===
wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Microsoft')]"))).click()

# === Step 4: Microsoft Login ===
wait.until(EC.presence_of_element_located((By.NAME, "loginfmt"))).send_keys(email)
driver.find_element(By.ID, "idSIButton9").click()  # Next Button

wait.until(EC.presence_of_element_located((By.NAME, "passwd"))).send_keys(password)
driver.find_element(By.ID, "idSIButton9").click()  # Sign In

# === Step 5: Stay Signed In Prompt ===
try:
    wait.until(EC.element_to_be_clickable((By.ID, "declineButton"))).click()  # Click No
except:
    print("Stay signed-in popup did not appear, continuing...")

# === Step 6: Automatically click first course ===
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='learnerCard']")))

try:
    first_card = driver.find_element(By.XPATH, "//div[@class='learnerCard']")
    go_to_course = first_card.find_element(By.XPATH, ".//a[span[contains(text(),'Go to Course')]]")
    go_to_course.click()
    print("✅ Automatically entered the first course.")
except Exception as e:
    print("❌ Could not find or click Go to Course button!")
    driver.quit()
    exit()

# === Step 7: Handle 'Continue Where You Left' Popup ===
time.sleep(5)  # Allow time for the popup to appear
try:
    close_popup = driver.find_element(By.XPATH, "//button[contains(text(),'Close') and @onclick='close_modal()']")
    driver.execute_script("arguments[0].click();", close_popup)
    print("✅ Closed 'Continue Where You Left' popup.")
except:
    print("ℹ No 'Continue Where You Left' popup appeared.")

# === Step 8: Detect Available Weeks ===
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'unit_heading')][a[contains(text(),'Week')]]")))

weeks = driver.find_elements(By.XPATH, "//div[contains(@class,'unit_heading')][a[contains(text(),'Week')]]")

if not weeks:
    print("❌ No weeks found!")
    driver.quit()
    exit()

print("\nDetected Weeks:")
for i, week in enumerate(weeks):
    week_text = week.text.strip()
    print(f"Week {i}: {week_text}")

# === Step 9: Ask user for week choice safely ===
while True:
    try:
        week_choice = int(input("Enter the Week number you want to open (e.g., 0 for Week 0): "))
        if 0 <= week_choice < len(weeks):
            break
        else:
            print(f"⚠ Please enter a valid week number between 0 and {len(weeks)-1}")
    except ValueError:
        print("⚠ Please enter a valid number only (e.g., 0, 1, 2...)")


selected_week = weeks[week_choice]

# === Step 10: Expand the selected week ===
driver.execute_script("arguments[0].click();", selected_week)
print(f"✅ Week {week_choice} clicked and expanded.")
time.sleep(4)  # Allow time for expand animation

# === Step 11: Detect Assignments inside the expanded week ===
assignments = selected_week.find_elements(By.XPATH, ".//following-sibling::ul[1]//a[contains(text(),'Assignment')]")

if not assignments:
    print("❌ No Assignment found in this week!")
    driver.quit()
    exit()

print("✅ Assignment found! Opening...")
driver.execute_script("arguments[0].click();", assignments[0])  # Click Assignment

# === Step 12: Handle Continue Popup if present ===
time.sleep(5)
try:
    cont_btn = driver.find_element(By.XPATH, "//button[contains(.,'Continue')]")
    cont_btn.click()
except:
    pass

# === Step 13: Take Answers from User ===
answers_input = input("\nEnter your answers separated by commas (ex: 1,2,3,1,4,...): ")
answers = [int(ans.strip()) for ans in answers_input.split(",")]

# === Step 14: Auto Fill Answers ===
time.sleep(6)
questions = driver.find_elements(By.XPATH, "//div[contains(@class,'qt-mc-question')]")

if len(answers) != len(questions):
    print(f"❌ Answer count ({len(answers)}) does not match question count ({len(questions)})")
    driver.quit()
    exit()

for i, question in enumerate(questions):
    option_number = answers[i]
    try:
        option_xpath = f".//input[@data-index='{option_number - 1}']"
        option = question.find_element(By.XPATH, option_xpath)
        driver.execute_script("arguments[0].click();", option)
        print(f"Answered Q{i+1} with option {option_number}")
    except Exception as e:
        print(f"Failed to select answer for Q{i+1}")

# === Step 15: Submit Assignment ===
try:
    submit_button = driver.find_element(By.ID, "submitbutton")
    submit_button.click()
    print("✅ Assignment Submitted Successfully!")
except:
    print("❌ Submit Failed or Submit Button Not Found!")

driver.quit()
# === End of Script ===
