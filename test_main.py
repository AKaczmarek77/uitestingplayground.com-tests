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


def test_check_progress_bar_speed():
    acceptable_time = 7000

    print('Step 1: Open subpage Progress Bar')
    driver.get('http://uitestingplayground.com/progressbar')

    print('Step 2: Click start button')
    driver.find_element('xpath', '/html/body/section/div/button[1]').click()

    print('Step 3: Wait until the bar is finished loading')
    while True:
        progress_status = driver.find_element('xpath', '/html/body/section/div/div[1]/div').text
        print('progress_status: ', progress_status)
        time.sleep(1)
        if progress_status == '100%':
            break

    print('Step 4: Click stop button')
    driver.find_element('xpath', '/html/body/section/div/button[2]').click()

    print('Step 5: Write out the result')
    result = driver.find_element('xpath', '/html/body/section/div/div[2]/p').text
    duration = result[22:]
    execution_time = int(duration)

    print('Step 6: Check if the loading time has exceeded the allowed time')
    if execution_time <= acceptable_time:
        assert True
        print('Passed. The loading time was', execution_time)
    else:
        print('Failed. The loading time exceeded the allowed time by: ', execution_time-acceptable_time)
        driver.close()
        assert False

    print('Step 7: Close driver')
    driver.close()
