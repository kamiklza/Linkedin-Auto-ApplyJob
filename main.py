from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

latpop_driver = "/Users/Kamiklza/PycharmProjects/chromedriver"
url = "https://linkedin.com"
user_name = "Testing"
user_psw = "Testing"

#-----------Testing---------#

driver = webdriver.Chrome(executable_path=latpop_driver)
driver.get(url)

sign_in_btn = driver.find_element_by_css_selector(".nav__cta-container .nav__button-secondary")
sign_in_btn.click()

email_input = driver.find_element_by_id("username")
email_input.send_keys(user_name)

password_input = driver.find_element_by_id("password")
password_input.send_keys(user_psw)

login_confirm = driver.find_element_by_class_name("btn__primary--large")
login_confirm.click()


go_to_job = driver.find_elements_by_css_selector(".global-nav__primary-items li")
go_to_job[2].click()
sleep(2)

search_job = driver.find_element_by_xpath('//*[@id="global-nav-search"]/div/div[2]/div[1]')
search_job.click()
sleep(2)

# job_type = driver.find_element_by_xpath('//*[@id="jobs-search-box-keyword-id-ember240"]')
# job_type.send_keys("Web Developer")
#
# submit = driver.find_element_by_xpath('//*[@id="global-nav-search"]/div/div[2]/button[1]')
# submit.click()
# sleep(2)
#
# jobs = driver.find_element_by_class_name("jobs-search-results__list list-style-none")
# print(jobs)

def testing():
    pass

