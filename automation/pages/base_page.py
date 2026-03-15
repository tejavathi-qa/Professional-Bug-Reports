from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://automationexercise.com/"

    def navigate(self, path=""):
        self.page.goto(f"{self.url}{path}")

    def get_element_text(self, selector):
        return self.page.inner_text(selector)
