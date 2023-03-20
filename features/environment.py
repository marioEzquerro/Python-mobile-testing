from appium import webdriver
from app.application import Application
from features.variables import CAPABILITIES
import os
import time
from datetime import datetime


def before_scenario(context, scenario):
    desired_capabilities = {}
    desired_capabilities['port'] = CAPABILITIES['port']
    desired_capabilities['ipAddress'] = CAPABILITIES['ipAddress']
    desired_capabilities['platformName'] = CAPABILITIES['platformName']
    desired_capabilities['diviceName'] = CAPABILITIES['diviceName']
    desired_capabilities['appPackage'] = CAPABILITIES['appPackage']
    desired_capabilities['appActivity'] = CAPABILITIES['appActivity']
    desired_capabilities['platformVersion'] = CAPABILITIES['platformVersion']
    desired_capabilities['uuid'] = CAPABILITIES['uuid']

    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    context.driver.implicitly_wait(30)

    context.app = Application(context.driver)


def after_scenario(context, scenario):
    if scenario.status == "failed":
        timestamp = datetime.now().strftime("%d-%m-%Y_%H_%M")
        screenshot_name = f"{scenario.name}({timestamp}).png"

        time.sleep(1.5)
        context.driver.get_screenshot_as_file(
            os.path.join('screens', screenshot_name))

    context.driver.quit()
