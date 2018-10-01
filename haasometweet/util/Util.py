import os
import sys
import time
import config
import logging
import logging.handlers
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


class Util:

    banner = '''
  _    _                                        _______                _   
 | |  | |                                      |__   __|              | |  
 | |__| | __ _  __ _ ___  ___  _ __ ___   ___     | |_      _____  ___| |_ 
 |  __  |/ _` |/ _` / __|/ _ \\| '_ ` _ \\ / _ \\    | \\ \\ /\\ / / _ \\/ _ \\ __|
 | |  | | (_| | (_| \\__ \\ (_) | | | | | |  __/    | |\\ V  V /  __/  __/ |_ 
 |_|  |_|\\__,_|\\__,_|___/\\___/|_| |_| |_|\\___|    |_| \\_/\\_/ \\___|\\___|\\__|
                                                                           
                                                                           

'''

    firstRun = True

    logger = None

    @staticmethod
    def set_up_logging():
      file_path = sys.modules[__name__].__file__
      project_path = os.path.dirname(os.path.dirname(os.path.dirname(file_path)))
      log_location = project_path + '/logs/'
      if not os.path.exists(log_location):
          os.makedirs(log_location)

      current_time = datetime.now()
      current_date = current_time.strftime("%Y-%m-%d")
      file_name = current_date + '.log'
      file_location = log_location + file_name
      with open(file_location, 'a+'):
          pass

      logger = logging.getLogger(__name__)
      format = '[%(asctime)s] [%(levelname)s] [%(message)s] [--> %(pathname)s [%(process)d]:]'
      logging.basicConfig(format=format, level=logging.DEBUG)
      return logger

    @staticmethod
    def get_logger():
      if Util.firstRun:
        Util.firstRun = False
        Util.logger = Util.set_up_logging()
        return Util.logger
      else:
        return Util.logger

    @staticmethod
    def take_screenshot(savepath):

        Util.get_logger().debug('Capturing Screenshot')

        DRIVER = 'chromedriver'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options,executable_path='./chromedriver')
        driver.set_window_position(0, 0)
        driver.set_window_size(1920, 1080)

        Util.get_logger().debug('Logging Into Haas')
        driver.get(config.CONFIG['HAAS_MAIN_URL'])
        element = driver.find_element_by_name("username")
        element.send_keys(config.CONFIG['HAAS_USER'])
        element = driver.find_element_by_name("password")
        element.send_keys(config.CONFIG['HAAS_PASS'])
        element = driver.find_element_by_id("sendLogin")
        element.click()
        time.sleep(5)

        Util.get_logger().debug('Navigating To Page')
        driver.get("http://google.com")
        driver.get(config.CONFIG['HAAS_PAGE_TO_SHARE']);
        time.sleep(8)

        Util.get_logger().debug('Moving mouse cursor')
        actionChains = ActionChains(driver)
        actionChains.move_to_element(driver.find_element_by_id("botListViewSimple")).perform()
        time.sleep(2)


        Util.get_logger().debug('Taking screenshot')
        driver.save_screenshot(savepath)
        Util.get_logger().debug('Saved Screenshot')
        driver.quit()
