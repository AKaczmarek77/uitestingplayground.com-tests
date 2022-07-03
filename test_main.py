from selenium import webdriver
import time
from selenium.webdriver.common.alert import Alert
import random
import string
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(executable_path='chromedriver.exe')


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
        print('Failed. The loading time exceeded the allowed time by: ', execution_time - acceptable_time)
        driver.close()
        assert False

    print('Step 7: Close driver')
    driver.close()


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

    print('Step 2: Check if the alert is open after click a blue button')
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


def test_successful_login():
    username = 'User'
    password = 'pwd'

    print('Step 1: Open subpage Sample App')
    driver.get('http://uitestingplayground.com/sampleapp')

    print('Step 2: Enter a valid login and password')
    driver.find_element('xpath', '/html/body/section/div/div[2]/div/input').send_keys(username)
    driver.find_element('xpath', '/html/body/section/div/div[3]/div/input').send_keys(password)

    print('Step 3: Click log in button')
    driver.find_element('xpath', '/html/body/section/div/div[4]/div/button').click()

    print('Step 4: Check if the user logged in')
    login_status = driver.find_element('xpath', '/html/body/section/div/div[1]/div/label').text
    acceptable_login_status = 'Welcome, User!'
    if login_status == acceptable_login_status:
        print('Passed. Successful login')
        assert True
    else:
        print('Failed. Unsuccessful login')
        assert False

    print('Step 5: Close driver')
    driver.close()


def test_unsuccessful_login():
    username = 'UserName'
    password = 'pxf'

    print('Step 1: Open subpage Sample App')
    driver.get('http://uitestingplayground.com/sampleapp')

    print('Step 2: Enter an invalid login and password')
    driver.find_element('xpath', '/html/body/section/div/div[2]/div/input').send_keys(username)
    driver.find_element('xpath', '/html/body/section/div/div[3]/div/input').send_keys(password)

    print('Step 3: Click log in button')
    driver.find_element('xpath', '/html/body/section/div/div[4]/div/button').click()

    print('Step 4: Check if the user logged in')
    login_status = driver.find_element('xpath', '/html/body/section/div/div[1]/div/label').text
    acceptable_login_status = 'Invalid username/password'
    if login_status == acceptable_login_status:
        print('Passed. Unsuccessful login')
        assert True
    else:
        print('Failed. Successful login')
        assert False

    print('Step 5: Close driver')
    driver.close()


def test_name_button():
    letters = string.ascii_letters
    text = ''.join(random.choice(letters) for i in range(10))

    print('Step 1: Open subpage Text input')
    driver.get('http://uitestingplayground.com/textinput')

    print('Step 2: Enter a randomly generated button name')
    driver.find_element('xpath', '/html/body/section/div/form/div/input').send_keys(text)

    print('Step 3: Click button')
    driver.find_element('xpath', '/html/body/section/div/form/div/button').click()

    print('Step 4: Check if the button name has changed')
    new_button_name = driver.find_element('xpath', '/html/body/section/div/form/div/button').text
    if text == new_button_name:
        print('Passed. The button name has changed')
        assert True
    else:
        print('Failed. The button name has not changed')
        assert False

    print('Step 5: Close driver')
    driver.close()


def test_check_if_the_color_of_the_button_changes_only_once():

    print('Step 1: Open subpage Hidden Layers')
    driver.get('http://uitestingplayground.com/hiddenlayers')

    print('Step 2: Click and check if the color of the button changes once and can only be clicked once')
    before_click = driver.find_element('xpath', '/html/body/section/div/div[1]/div/button')
    driver.find_element('xpath', '/html/body/section/div/div[1]/div/button').click()
    after_click = driver.find_element('xpath', '/html/body/section/div/div[1]/div[2]/button')
    if before_click != after_click:
        print('Successfully clicked')
    else:
        assert False
    try:
        driver.find_element('xpath', '/html/body/section/div/div[1]/div/button').click()
        assert False
    except:
        assert True

    print('Step 3: Close driver')
    driver.close()


def test_request_processing_verify():
    # unfinished
    current_attempts = 0

    print('Step 1: Open subpage Client Side Delay')
    driver.get('http://uitestingplayground.com/ajax')

    print('Step 2: Click button triggering client side logic')
    driver.find_element('xpath', '/html/body/section/div/button').click()

    print('Step 3: Wait until request is finished')
    while True:
        time.sleep(1)
        try:
            request = driver.find_element('xpath', '/html/body/section/div/div/p').text
            print('Request: ', request)
            if request == 'Data loaded with AJAX get request.':
                break
        except NoSuchElementException:
            current_attempts = current_attempts + 1
            print('Current attempts: ', current_attempts)
            print('not loaded yet')
            if current_attempts == 2:
                break

