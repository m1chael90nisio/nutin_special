 #To install the Python client library:
# pip install -U selenium

# Import the Selenium 2 namespace (aka "webdriver")
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




# Google Chrome driver directory
driver = webdriver.Chrome('C:/Users/mixalis/Desktop/chromedriver_win32/chromedriver.exe')

#google translate link
driver.get('https://translate.google.gr/?hl=el#en/it/')
trans = input('Enter your text: ')

#path to send the element to translate
element = driver.find_element_by_xpath("//*[@id='source']")
element.send_keys(trans)

text = driver.find_element_by_xpath("//*[@id='gt-submit']")
text.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id='result_box']')))


metafrasi= driver.find_element_by_xpath("//*[@id='result_box']")

print ("YOUR TRANSLATE" +" "+metafrasi.text)

# assert "Hello, World!" in driver.get_page_source()

# Close the browser!
driver.quit()


