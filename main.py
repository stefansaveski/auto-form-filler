from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Random emails
first_names = [
    "Marko", "Elena", "Aleksandar", "Jovana", "Kristijan", "Simona", "Stefan", "Marija", "Filip", "Ana",
    "Mihail", "Ivana", "Darko", "Teodora", "Bojan", "Katerina", "Petar", "Sanja", "Nikola", "Tijana",
    "Viktor", "Milena", "Dario", "Angela", "Ilija", "Tamara", "Vladimir", "Emilija", "Daniel", "Sara",
    "Goran", "Martina", "Blagoj", "Dragana", "Goce", "Veronika", "Martin", "Kristina", "Hristijan", "Ivona"
]

last_names = [
    "Stojanovski", "Petrovska", "Trajkovski", "Ilievska", "Nikolov", "Ristovska", "Kostadinov", "Georgievska",
    "Angelov", "Milevska", "Todorov", "Stefanovska", "Mitrevski", "Ivanovska", "Spasovski", "Zafirovska",
    "Kitanov", "Dimitrovska", "Veljanoski", "Naumovska", "Pavlov", "Radevska", "Cvetanovski", "Gjorgjieva",
    "Zdravkovski", "Aleksandrova", "Mladenovski", "Arsovska", "Petreski", "Lazarevska"
]

domains = ["gmail.com", "yahoo.com", "outlook.com", "hotmail.com", "t-home.mk"]


def generate_random_email():
    first = random.choice(first_names).lower()
    last = random.choice(last_names).lower()
    number = str(random.randint(1, 9999))
    domain = random.choice(domains)

    formats = [
        f"{first}.{last}{number}@{domain}",
        f"{first[0]}{last}{number}@{domain}",
        f"{last}.{first}{random.randint(1, 99)}@{domain}",
        f"{first}{last}{random.randint(10, 99)}@{domain}",
        f"{last}{random.randint(100, 999)}@{domain}",
        f"{first}{random.randint(1000, 9999)}@{domain}"
    ]

    return random.choice(formats)


def submit_form():
    # Setup
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    # Open the form
    driver.get('https://docs.google.com/forms/d/e/1FAIpQLScuWQTqiCAioJItf2f0kgVrX9wQbbRPj0mxiFWLcwfApuqagg/viewform')
    time.sleep(2)

    # === Page 1: Demographics ===

    # Select gender (e.g., Жeнски)
    gender_option = driver.find_element(By.XPATH, '//div[@role="radio" and @aria-label="Женски"]')
    gender_option.click()
    # time.sleep(0.5)

    # Select age group (e.g., 27-39)
    age_option = driver.find_element(By.XPATH, '//div[@role="radio" and @aria-label="27-39"]')
    age_option.click()
    # time.sleep(0.5)

    # Enter email (Fix selector)
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, 'input.whsOnd'
        ))
    )
    email = generate_random_email()
    email_field.send_keys(email)

    # Click "Next"
    next_button = driver.find_element(By.XPATH, '//span[text()="Next"]/ancestor::div[@role="button"]')
    next_button.click()
    # time.sleep(2)

    # === Page 2: 40 Questions ===
    # All are radio questions with scale 1 to 7

    # Select answer for all 40 questions
    # (Here we simulate random answers for demonstration)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[@role="listitem"]'))
    )

    # Find all question blocks
    questions = driver.find_elements(By.XPATH, '//div[@role="listitem"]')

    print(f"Found {len(questions)} questions")

    for idx, question in enumerate(questions):
        try:
            # Find all answer options within the question
            options = question.find_elements(By.XPATH, './/div[@role="radio"]')

            if not options:
                print(f"Question {idx + 1}: No answer options found")
                continue

            # Pick a random option index (or use fixed if needed)
            answer_index = random.randint(0, len(options) - 1)
            options[answer_index].click()
            print(f"Answered question {idx + 1} with option {answer_index + 1}")
        except Exception as e:
            print(f"Failed to answer question {idx + 1}: {e}")

    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Submit") or contains(text(), "Прати")]'))
    )
    submit_btn.click()
    driver.quit()


if __name__ == "__main__":
    N = 700  # <-- change this to however many times you want
    for i in range(N):
        print(f"Running submission {i + 1}/{N}")
        submit_form()
