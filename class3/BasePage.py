class BasePage():
    def __init__(self,driver):
        self.driver=driver
    def open_url(self,url):
        self.driver.get(url)
    def find_element(self,*slo):
        self.driver.find_element(*slo)
