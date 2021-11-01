from class3.FengzPage import FengzPage
from class3.FengzPage1 import FengzPage1
from class3.FengzPage2 import FengzPage2
from class3.FengzPage3 import FengzPage3
from class3.FengzPage4 import FengzPage4
import unittest
from selenium import webdriver
from ddt import ddt,data,unpack
from excle_py import ParaExcle
wjname='zoukao.xlsx'
sheetname='zhmm'
pe=ParaExcle(wjname,sheetname)
@ddt()
class alibaba(unittest.TestCase):
    def setUp(self) -> None:
        self.driver=webdriver.Firefox()
    def tearDown(self) -> None:
        pass
    @data(*pe.getDataFromsheet_mul())
    @unpack
    def test_alibaba_01(self,zh,mm):
        po= FengzPage(self.driver)
        po.aldel(zh,mm)

    @data(*pe.getDataFromsheet_mul())
    @unpack
    def test_alibaba_02(self, zh, mm):
        po = FengzPage1(self.driver)
        po.aldel(zh, mm)

    @data(*pe.getDataFromsheet_mul())
    @unpack
    def test_alibaba_03(self, zh, mm):
        po = FengzPage2(self.driver)
        po.aldel(zh, mm)

    @data(*pe.getDataFromsheet_mul())
    @unpack
    def test_alibaba_04(self, zh, mm):
        po = FengzPage3(self.driver)
        po.aldel(zh, mm)

    @data(*pe.getDataFromsheet_mul())
    @unpack
    def test_alibaba_05(self, zh, mm):
        po = FengzPage4(self.driver)
        po.aldel(zh, mm)
if __name__ == '__main__':
    unittest.main()