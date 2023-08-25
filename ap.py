from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from sys import platform

# Initialize the web driver (you need to provide the path to your chromedriver executable)
if platform == "linux" or platform == "linux2":
	chrome_driver_path = "./chromedriver"
elif platform == "darwin":
	chrome_driver_path = "./mac/chromedriver"
elif platform == "win32":
	chrome_driver_path = "chromedriver.exe"

service = Service(executable_path=r'C:\Users\DELE\Downloads\chromedriver-win64\chromedriver.exe')

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("http://www.python.org")

# Get all the text content of the web page
page_text = driver.page_source

# Print the extracted text
print(page_text)

# Close the web driver
driver.quit()
