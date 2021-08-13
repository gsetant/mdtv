from selenium import webdriver

BROWSER_DRIVE = 'chrome'


class BrowserTools:
    browser = None
    display = None

    def get_browser(self):

        if BROWSER_DRIVE is 'chrome':
            from selenium.webdriver.firefox.options import Options
            firefox_opt = Options()
            firefox_opt.headless = True
            self.browser = webdriver.Firefox(options=firefox_opt)
        if BROWSER_DRIVE is 'chrome':
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-setuid-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            self.browser = webdriver.Chrome(chrome_options=chrome_options)

        return self.browser

    def close_browser(self):
        self.browser.close()
