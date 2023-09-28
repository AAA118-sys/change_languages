from selenium.webdriver.common.by import By
import pytest
import time


class TestItems:
    def test_items(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        # browser.implicitly_wait(20)
        time.sleep(5)
        button_find = browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
        assert button_find.is_displayed(), "element is absent"


if __name__ == "__main__":
    pytest.main()
