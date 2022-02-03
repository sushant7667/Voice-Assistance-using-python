
from selenium import webdriver


class infow():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

    def get_info(self,query):
        self.query = query
        self.driver.get(url='https://www.google.co.in/')
        search = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(query)
        enter = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        enter.click()
        # enter1 = self.driver.find_element_by_xpath('//*[@id="kp-wp-tab-overview"]/div[2]/div/div/div/div/div[1]/div/div/div/span[2]/a')
        # enter1.click()
        # speak('Shah Rukh Khan (pronounced [ˈʃaːɦrʊx xaːn]; born 2 November 1965), also known by the initialism SRK, is an Indian actor, film producer, and television personality who works in Hindi films')


#'https://www.google.co.in/'

