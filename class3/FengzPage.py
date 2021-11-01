from class3.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack
from excle_py import ParaExcle
wjname='zoukao.xlsx'
sheetname='zhmm'
pe=ParaExcle(wjname,sheetname)
@ddt()
class FengzPage(BasePage):
    aldl_clo=(By.CLASS_NAME,'link-login')
    dl_clo=(By.XPATH,'/html/body/div[2]/div[2]/div[1]/div/div[6]/ul/li[1]/a')
    dl1_clo=(By.ID,'ptlogin_iframe')
    aldl1_clo=(By.XPATH,'//*[@id="switcher_plogin"]')
    aldl2_clo = (By.XPATH, '//*[@id="u"]')
    aldl3_clo=(By.XPATH,'//*[@id="p"]')
    aldl4_clo=(By.ID,'login_button')

    def dengl(self):
        self.driver.find_element(*self.aldl_clo).click()
        sleep(2)
    def dengl2(self):
        self.driver.find_element(*self.dl_clo).click()
        sleep(2)
    def frame(self):
        self.driver.switch_to.frame(self.driver.find_element(*self.dl1_clo))
        self.driver.implicitly_wait(2)
    def zhanghaomimadl(self):
        self.driver.find_element(*self.aldl1_clo).click()
        sleep(2)
    def zhmm(self,zh,mm):
        self.driver.find_element(*self.aldl2_clo).send_keys(zh)
        sleep(2)
        self.driver.find_element(*self.aldl3_clo).send_keys(mm)
        sleep(2)
    def djdl(self):
        self.driver.find_element(*self.aldl4_clo).click()
        sleep(2)

    def aldel(self,zh,mm):
        self.driver.get('https://www.jd.com/')
        sleep(2)
        self.driver.maximize_window()
        sleep(2)
        self.dengl()
        sleep(2)
        self.dengl2()
        sleep(2)
        self.frame()
        sleep(2)
        self.zhanghaomimadl()
        sleep(2)
        self.zhmm(zh,mm)
        sleep(2)
        self.djdl()
