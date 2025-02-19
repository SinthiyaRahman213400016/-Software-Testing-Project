# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Test213400016():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_213400016(self):
    self.driver.get("https://computer-database.gatling.io/computers/new")
    self.driver.find_element(By.ID, "name").click()
    self.driver.find_element(By.ID, "name").send_keys("test computer")
    element = self.driver.find_element(By.ID, "introduced")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.ID, "introduced")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.ID, "introduced")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.ID, "introduced").click()
    self.driver.find_element(By.ID, "introduced").send_keys("1958-01-01")
    self.driver.find_element(By.ID, "company").click()
    dropdown = self.driver.find_element(By.ID, "company")
    dropdown.find_element(By.XPATH, "//option[. = 'Thinking Machines']").click()
    element = self.driver.find_element(By.CSS_SELECTOR, ".primary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".primary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, ".primary")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()
    self.driver.find_element(By.CSS_SELECTOR, ".primary").click()
    self.driver.find_element(By.LINK_TEXT, "Next →").click()
    self.driver.find_element(By.LINK_TEXT, "Computer database").click()
  
