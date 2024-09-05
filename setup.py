from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Correct path to your ChromeDriver executable
chrome_driver_path = r'C:\WebDriver\chromedriver-win64\chromedriver.exe'  # Ensure this path is correct

# Initialize WebDriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Example usage
driver.get("https://videotube-rust.vercel.app/")
print(driver.current_url)  # Should print "Google"
driver.quit()
