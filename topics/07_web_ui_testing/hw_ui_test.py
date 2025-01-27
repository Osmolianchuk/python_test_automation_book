import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def test_text_box_form():
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get("https://demoqa.com/text-box")

    try:
        # Input data
        driver.find_element(By.ID, "userName").send_keys("Donald Duck")
        driver.find_element(By.ID, "userEmail").send_keys("donald.duck@example.com")
        driver.find_element(By.ID, "currentAddress").send_keys("56 Main St")
        driver.find_element(By.ID, "permanentAddress").send_keys("379 Apple Rd")

        # Submit form
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "submit"))
        )
        submit_button.click()

        # Check output
        WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "mb-1"))
        )
        name = driver.find_element(By.ID, "name").text
        email = driver.find_element(By.ID, "email").text
        current_address = driver.find_element(By.ID, "currentAddress").text
        permanent_address = driver.find_element(By.ID, "permanentAddress").text

        assert name == "Name:Donald Duck"
        assert email == "Email:donald.duck@example.com"
        assert current_address == "Current Address:56 Main St"
        assert permanent_address == "Permananet Address:379 Apple Rd"
    finally:
        driver.quit()


if __name__ == "__main__":
    pytest.main()