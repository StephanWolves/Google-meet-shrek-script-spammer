from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Sets crome preferences
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 2, 
"profile.default_content_setting_values.notifications": 2 
})

driver = webdriver.Chrome(chrome_options=opt, executable_path=r'C:\Users\samue\Desktop\Chrome Driver\chromedriver.exe')

meeting_code = 'rcn-vizy-ibq'

## retreives env variables
email = os.getenv('email')
password = os.environ.get('password')

## gets shrek script
shrek = open("Shrek.txt", "r")
text = shrek.read()

## Signs into google
def sign_in():

    driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.192029741.682179699.1619555763-258156599.1619555763&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    ## Puts in email
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "identifierId"))).send_keys(email)
    driver.find_element_by_id("identifierNext").click()

    ##Puts in password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "password"))).send_keys(password)
    driver.find_element_by_id("passwordNext").click()


    ## Waits
    WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME, "gb_uc")))

    ## Does the stuff inside google meet
def google_meet():
   
    ## Enters meeting code
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div/div[1]/label/input"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div/div[1]/label/input"))).send_keys(meeting_code)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz/div/div[2]/div/div[1]/div[3]/div/div/div[1]/label/input"))).send_keys(Keys.ENTER)
    time.sleep(.1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button']//span[contains(text(), 'Join now')]"))).click()
    time.sleep(10)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[1]/div[3]/div/div[2]/div[3]/span"))).click()
    time.sleep(2)
    
    

def send():
    for word in text.split():
        driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(word)
        driver.find_element_by_xpath('/html/body/div[1]/c-wiz/div[1]/div/div[9]/div[3]/div[4]/div/div[2]/div[2]/div[2]/span[2]/div/div[4]/div[1]/div[1]/div[2]/textarea').send_keys(Keys.ENTER)
        time.sleep(.5)

def spam():
     for i in range(1):
         send()

sign_in()
google_meet()
spam()



time.sleep(1000000)






