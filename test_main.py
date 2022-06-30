from selenium import webdriver
import time

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
