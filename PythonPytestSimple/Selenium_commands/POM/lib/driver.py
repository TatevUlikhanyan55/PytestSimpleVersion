from selenium import webdriver
from selenium.webdriver.safari.options import Options as Option
from selenium.webdriver.chrome.options import Options


def get_driver_by_name(driver_name="chrome"):
    if driver_name == "chrome":
        return webdriver.Chrome()
    elif driver_name == "edge":
        return webdriver.ChromiumEdge()
    elif driver_name == "firefox":
        return webdriver.Firefox()
    elif driver_name == "safari":
        options = Option()
        return webdriver.Safari(options=options)
    elif driver_name == "headless":
        options = Options()
        options.add_argument("--headless")
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) " \
                         "Chrome/103.0.5060.114 Safari/537.36"
        options.add_argument(f'user-agent={user_agent}')
        return webdriver.Chrome(options=options)
    else:
        print("Driver name is missing")
