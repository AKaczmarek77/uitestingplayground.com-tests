from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome(executable_path='chromedriver.exe')


def test_check_if_id_is_dynamic():
    print('Step 1: Open subpage dynamic id')
    driver.get("http://uitestingplayground.com/dynamicid")
    time.sleep(2)

    print('Step 2: Find and save id of button')
    element_with_the_dynamic_id_1 = driver.find_element('xpath', '//html/body/section/div/button')
    dynamic_id_1 = element_with_the_dynamic_id_1.get_attribute('id')
    print(dynamic_id_1)

    print('Step 3: Refresh the page')
    driver.refresh()

    print('Step 4: Find and save id of button')
    element_with_the_dynamic_id_2 = driver.find_element('xpath', '//html/body/section/div/button')
    dynamic_id_2 = element_with_the_dynamic_id_2.get_attribute('id')
    print(dynamic_id_2)

    print('Step 5: Check if IDs are different')
    if dynamic_id_1 != dynamic_id_2:
        assert True
    else:
        assert False

    print('Step 6: Close driver')
    driver.close()


def test_check_popup():
    print('Step 1: Open subpage Class Attribute')
    driver.get('http://uitestingplayground.com/classattr')

    print('Step 2: Check if the alert is open')
    try:
        driver.find_element('xpath',
                            "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]").click()
    except:
        assert False

    print('Step 3: Close the alert')
    alert = Alert(driver)
    alert.accept()

    print('Step 4: Close driver')
    driver.close()