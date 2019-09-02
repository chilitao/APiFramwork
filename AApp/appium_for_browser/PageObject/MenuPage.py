#coding=gbk
from appium import webdriver
from selenium.webdriver.common.by import By
from AApp.appium_for_browser.PageObject.BasePage import Base
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.capabilities)
class Menu(Base):
    menu_icon=(By.NAME,"菜单")
    night=(By.ID,"com.quqi.browser:id/qk")
    private_tab=(By.ID,"com.quqi.browser:id/ql")
    def test_menu_click(self):
        menu_page=Menu(driver)
        menu_page.find_element(Menu.menu_icon)

Menu(driver).test_menu_click()