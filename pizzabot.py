from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
from time import sleep
print("Launching pizzabot.py...")
driver = webdriver.Chrome()
driver.get("https://www.pizzahut.com/index.php?f=change&zip=del#/home")
start = driver.find_element_by_css_selector('#heroImg')
start.click()
print("Sending destination...")
delivery = driver.find_element_by_css_selector('#ph-localization-id > div.row.ph-occasion-heading.ph-padding-top-none > div:nth-child(1) > div > div > label > span.center-block.icon-delivery-default')
delivery.click()
address = driver.find_element_by_css_selector('#syo-address1')
#Enter your address below
address.send_keys()
city = driver.find_element_by_css_selector('#city')
#Enter your city below
city.send_keys()
state = driver.find_element_by_css_selector('#state')
state.click()
myState = driver.find_element_by_css_selector('#state > option:nth-child(23)')
myState.click()
zip = driver.find_element_by_css_selector('#zip-input')
#Enter Zip code here
zip.send_keys()
findAStore = driver.find_element_by_css_selector('#ph-find-store')
findAStore.click()
sleep(3)
print("Ordering...")
orderNow = driver.find_element_by_xpath('//*[@id="ph-localization-id"]/div[3]/div[2]/div[2]/div/div[1]/div/div/div/div/div[3]/a')
orderNow.click()
print("Processing...")
sleep(5)
choice = driver.find_element_by_xpath('//*[@id="tile-big-dinner-box-with-wingstreet-eaded---boneout-wings"]/div/div[2]/div[3]/div[2]/div[1]')
choice.click()
print("Customizing pizza 1...")
sleep(3)
next1 = driver.find_element_by_xpath('//*[@id="steps"]/div[1]/div[6]/ul/li')
next1.click()
sauce1 = driver.find_element_by_css_selector('#option-2-HQ- > div > div.nopadding.text-center.pointer-cursor > div > img')
sauce1.click()
continueToToppings = driver.find_element_by_xpath('//*[@id="crustNextBtn"]')
continueToToppings.click()
continue1 = driver.find_element_by_css_selector('#pb-primary-cta-deal')
continue1.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[15]/div/div/div/div/div[3]/div[2]/a'))).click()
sleep(3)
print("Customizing pizza 2...")
next2 = driver.find_element_by_xpath('//*[@id="steps"]/div[1]/div[6]/ul/li')
next2.click()
sauce2 = driver.find_element_by_css_selector('#option-2-BS- > div > div.nopadding.text-center.pointer-cursor > div > img')
sauce2.click()
continueToToppings2 = driver.find_element_by_xpath('//*[@id="crustNextBtn"]')
continueToToppings2.click()
continue2 = driver.find_element_by_css_selector('#pb-primary-cta-deal')
continue2.click()
sleep(3)
print("Ordering breadsticks...")
breadSticks = driver.find_element_by_xpath('//*[@id="ato-breadsticks"]')
breadSticks.click()
sleep(3)
print("Ordering wings...")
wingFlavor = driver.find_element_by_xpath('//*[@id="prod-breaded-boneout-wings"]')
wingFlavor.click()
myWingFlavor = driver.find_element_by_css_selector('#prod-breaded-boneout-wings > option:nth-child(3)')
myWingFlavor.click()
addToOrder = driver.find_element_by_xpath('//*[@id="ato-breaded-boneout-wings"]')
addToOrder.click()
print("Proceeding to checkout...")
cart = driver.find_element_by_xpath('//*[@id="desktop-header"]/div/div[4]/div/div[2]')
cart.click()
viewOrder = driver.find_element_by_xpath('//*[@id="view-order-top-upsell"]')
viewOrder.click()
sleep(3)
checkOut = driver.find_element_by_xpath('/html/body/app-root/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div/div/div/div[3]/div[3]/div[2]/div')
checkOut.click()
sleep(3)
guestAccount = driver.find_element_by_css_selector('#co-guest-login')
guestAccount.click()
sleep(3)
print("Providing information...")
firstName = driver.find_element_by_css_selector('#firstName')
#Enter first name here
firstName.send_keys()
lastName = driver.find_element_by_css_selector('#lastName')
#Enter last name here
lastName.send_keys()
email = driver.find_element_by_css_selector('#emailAddress')
#Enter email here
email.send_keys()
phoneNum = driver.find_element_by_css_selector('#phoneNumber')
#Enter phone number
phoneNum.send_keys()
track = driver.find_element_by_xpath('//*[@id="acquisition-co"]/div/div/div[3]/div[4]/div[2]/label')
track.click()
continueToPay = driver.find_element_by_xpath('//*[@id="ph-co-2-continue"]')
continueToPay.click()
sleep(3)
print("Inserting payment information...")
creditName = driver.find_element_by_css_selector('#ccFullName')
#Enter credit card username
creditName.send_keys()
creditNum = driver.find_element_by_css_selector('#ccNumber')
#Enter credit card number
creditNum.send_keys()
expMonth = driver.find_element_by_xpath('//*[@id="acquisition-co"]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[3]/div/mat-form-field/div/div[1]')
expMonth.click()
myExpMonth = driver.find_element_by_xpath('//*[@id="mat-option-0"]')
myExpMonth.click()
expYear = driver.find_element_by_xpath('//*[@id="acquisition-co"]/div/div/div[2]/div[1]/div/div[1]/div/div[2]/div/div/div[4]/div/mat-form-field/div/div[1]')
expYear.click()
myExpYear = driver.find_element_by_xpath('//*[@id="mat-option-16"]')
myExpYear.click()
cvv = driver.find_element_by_css_selector('#ccCVVNumber')
#Enter CVV number
cvv.send_keys()
billingZip = driver.find_element_by_css_selector('#ccZip')
#Enter billing zipcode
billingZip.send_keys()
print("Tipping the driver...")
tip = driver.find_element_by_xpath('//*[@id="driverTipSection"]/div[2]/div/div[2]/label')
tip.click()
agreement = driver.find_element_by_xpath('//*[@id="acquisition-co"]/div/div/div[5]/div[2]/div')
agreement.click()
finish = driver.find_element_by_css_selector('#ph-co-2-continue')
finish.click()
print("Order completed!!!")







































