from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from app.application import Application
from selenium.webdriver.chrome.options import Options


def browser_init(context):
    """
    :param context: Behave context
    """
    # context.browser = webdriver.Chrome()
    # options = Options()
    # options.add_argument("--incognito")
    # options.add_argument("--disable-notifications")
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument("--disable-notifications")
    context.driver = webdriver.Chrome(chrome_options=chrome_options)
    # context.driver = webdriver.Chrome(chrome_options=options)

    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)
    context.wait = WebDriverWait(context.driver, 15)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()