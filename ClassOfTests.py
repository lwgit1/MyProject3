<<<<<<< HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, datetime, csv, logging
import unittest

#new comments abcde
#extr comment adfsdfdf

class AllTests(object):

    def __init__(self, driver):
        self.driver = driver

    def Test1(self):
        print ("Test1 running now")
        driver = webdriver.Chrome()

        from POM import PageObjects
        mytest = PageObjects(driver)

        PageObjects.FileToWriteTo = 'JobServeTest1'

        DateTime = datetime.datetime.now()
        line = str(DateTime)
        line1 = line.translate(None, ' :.')
        LOG_FILENAME = 'JobServeTest1_' + line1 + '.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

        with open('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test\users.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                username = (row[0])
                password = (row[1])

                logging.info("=====================================================================================")
                logging.info("TEST CASE FOR USER: " + username + "   Date: " + line)
                logging.info("=====================================================================================")

                mytest.WriteToFile(
                    '=====================================================================================' + '\n')
                mytest.WriteToFile('TEST CASE FOR USER: ' + username + '     Date: ' + line + '\n')
                mytest.WriteToFile(
                    '=====================================================================================' + '\n')

                mytest.HomePage_NavigateTo()

                mytest.HomePage_SignIn_Click()

                if (mytest.Check_For_Text_In_Page('Allow cookies')):
                    mytest.Login_Cookies_Click()

                mytest.Login_UserName_EnterText(username)

                mytest.Login_Password_EnterText(password)

                mytest.Login_Submit_Click()

                time.sleep(10)

                mytest.Check_For_Text_In_Page('xMy Profile')

                mytest.HomePage_WithinDaysDDL_Select('Within 4 days')

                mytest.HomePage_ViewProfile_Click()

                mytest.Check_For_Text_In_Page('xActively Seeking')

                mytest.MyProfile_HomeLocation_VerifyAttr('Woking, Surrey')

                mytest.MyProfile_PrintIcon_isElementPresent()

                mytest.MyProfile_PrintIcon_isElementVisible('True')

                mytest.MyProfile_Availablity_VerifyElementText('xxxImmediate')

                mytest.TopMenu_HomeIcon_Click()

                mytest.HomePage_CountriesCheckBox_isChecked('True')

                time.sleep(10)

                mytest.HomePage_LogOut_Click()

                time.sleep(10)

        driver.quit()


    def Test2(self):
        print ("Test2 running now")
        driver = webdriver.Chrome()

        from POM import PageObjects
        mytest = PageObjects(driver)

        PageObjects.FileToWriteTo = 'JobServeTest2'

        DateTime = datetime.datetime.now()
        line = str(DateTime)
        line1 = line.translate(None, ' :.')
        LOG_FILENAME = 'JobServeTest1_' + line1 + '.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

        with open('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test\users.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                username = (row[0])
                password = (row[1])

                logging.info("=====================================================================================")
                logging.info("TEST CASE FOR USER: " + username + "   Date: " + line)
                logging.info("=====================================================================================")

                mytest.WriteToFile(
                    '=====================================================================================' + '\n')
                mytest.WriteToFile('TEST CASE FOR USER: ' + username + '     Date: ' + line + '\n')
                mytest.WriteToFile(
                    '=====================================================================================' + '\n')

                mytest.HomePage_NavigateTo()

                mytest.HomePage_SignIn_Click()

                if (mytest.Check_For_Text_In_Page('Allow cookies')):
                    mytest.Login_Cookies_Click()

                mytest.Login_UserName_EnterText(username)

                mytest.Login_Password_EnterText(password)

                mytest.Login_Submit_Click()

                time.sleep(10)

                mytest.Check_For_Text_In_Page('xMy Profile')

                mytest.HomePage_WithinDaysDDL_Select('Within 4 days')

                mytest.HomePage_ViewProfile_Click()

                mytest.Check_For_Text_In_Page('xActively Seeking')

                mytest.MyProfile_HomeLocation_VerifyAttr('Woking, Surrey')

                mytest.MyProfile_PrintIcon_isElementPresent()

                mytest.MyProfile_PrintIcon_isElementVisible('True')

                mytest.MyProfile_Availablity_VerifyElementText('xxxImmediate')

                mytest.TopMenu_HomeIcon_Click()

                mytest.HomePage_CountriesCheckBox_isChecked('True')

                time.sleep(10)

                mytest.HomePage_LogOut_Click()

                time.sleep(10)

        driver.quit()

    def Test3(self):
        print ("Test3 running now")


=======
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time, datetime, csv, logging
import unittest



class AllTests(object):

    def __init__(self, driver):
        self.driver = driver

    def Test1(self):
        print ("Test1 running now")
        driver = webdriver.Chrome()

        from POM import PageObjects
        mytest = PageObjects(driver)

        PageObjects.FileToWriteTo = 'JobServeTest1'

        DateTime = datetime.datetime.now()
        line = str(DateTime)
        line1 = line.translate(None, ' :.')
        LOG_FILENAME = 'JobServeTest1_' + line1 + '.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

        with open('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test\users.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                username = (row[0])
                password = (row[1])

                logging.info("=====================================================================================")
                logging.info("TEST CASE FOR USER: " + username + "   Date: " + line)
                logging.info("=====================================================================================")

                mytest.WriteToFile(
                    '=====================================================================================' + '\n')
                mytest.WriteToFile('TEST CASE FOR USER: ' + username + '     Date: ' + line + '\n')
                mytest.WriteToFile(
                    '=====================================================================================' + '\n')

                mytest.HomePage_NavigateTo()

                mytest.HomePage_SignIn_Click()

                if (mytest.Check_For_Text_In_Page('Allow cookies')):
                    mytest.Login_Cookies_Click()

                mytest.Login_UserName_EnterText(username)

                mytest.Login_Password_EnterText(password)

                mytest.Login_Submit_Click()

                time.sleep(10)

                mytest.Check_For_Text_In_Page('xMy Profile')

                mytest.HomePage_WithinDaysDDL_Select('Within 4 days')

                mytest.HomePage_ViewProfile_Click()

                mytest.Check_For_Text_In_Page('xActively Seeking')

                mytest.MyProfile_HomeLocation_VerifyAttr('Woking, Surrey')

                mytest.MyProfile_PrintIcon_isElementPresent()

                mytest.MyProfile_PrintIcon_isElementVisible('True')

                mytest.MyProfile_Availablity_VerifyElementText('xxxImmediate')

                mytest.TopMenu_HomeIcon_Click()

                mytest.HomePage_CountriesCheckBox_isChecked('True')

                time.sleep(10)

                mytest.HomePage_LogOut_Click()

                time.sleep(10)

        driver.quit()


    def Test2(self):
        print ("Test2 running now")
        driver = webdriver.Chrome()

        from POM import PageObjects
        mytest = PageObjects(driver)

        PageObjects.FileToWriteTo = 'JobServeTest2'

        DateTime = datetime.datetime.now()
        line = str(DateTime)
        line1 = line.translate(None, ' :.')
        LOG_FILENAME = 'JobServeTest1_' + line1 + '.log'
        logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO)

        with open('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test\users.csv') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                print(row)
                username = (row[0])
                password = (row[1])

                logging.info("=====================================================================================")
                logging.info("TEST CASE FOR USER: " + username + "   Date: " + line)
                logging.info("=====================================================================================")

                mytest.WriteToFile(
                    '=====================================================================================' + '\n')
                mytest.WriteToFile('TEST CASE FOR USER: ' + username + '     Date: ' + line + '\n')
                mytest.WriteToFile(
                    '=====================================================================================' + '\n')

                mytest.HomePage_NavigateTo()

                mytest.HomePage_SignIn_Click()

                if (mytest.Check_For_Text_In_Page('Allow cookies')):
                    mytest.Login_Cookies_Click()

                mytest.Login_UserName_EnterText(username)

                mytest.Login_Password_EnterText(password)

                mytest.Login_Submit_Click()

                time.sleep(10)

                mytest.Check_For_Text_In_Page('xMy Profile')

                mytest.HomePage_WithinDaysDDL_Select('Within 4 days')

                mytest.HomePage_ViewProfile_Click()

                mytest.Check_For_Text_In_Page('xActively Seeking')

                mytest.MyProfile_HomeLocation_VerifyAttr('Woking, Surrey')

                mytest.MyProfile_PrintIcon_isElementPresent()

                mytest.MyProfile_PrintIcon_isElementVisible('True')

                mytest.MyProfile_Availablity_VerifyElementText('xxxImmediate')

                mytest.TopMenu_HomeIcon_Click()

                mytest.HomePage_CountriesCheckBox_isChecked('True')

                time.sleep(10)

                mytest.HomePage_LogOut_Click()

                time.sleep(10)

        driver.quit()

    def Test3(self):
        print ("Test3 running now")


>>>>>>> lwgit1/master
