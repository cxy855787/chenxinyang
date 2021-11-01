import unittest,HTMLTestRunner_PY3,yagmail
suite=unittest.defaultTestLoader.discover(start_dir='./',pattern='test_case.py')
jingdong=HTMLTestRunner_PY3.HTMLTestRunner(open('jingdong.html','wb'),title='京东测试用例的报告',description='京东测试报告')
jingdong.run(suite)
jingdong=yagmail.SMTP(user='1547786171@qq.com',password='mprlkszenhiyhead',host='smtp.qq.com',port=465)
jingdong.send(to='1547786171@qq.com',subject='京东测试用例',contents=['jingdong.html','geckodriver.log'])