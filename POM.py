from selenium import webdriver
from selenium.webdriver.support.ui import Select
import datetime, logging, time, random

#abcd
# DateTime = datetime.datetime.now()
# line = str(DateTime)
# line = line.translate(None, ' :.')
# LOG_FILENAME = 'Execution_' + line + '.log'
# logging.basicConfig(filename=LOG_FILENAME,level=logging.INFO)

from selenium.common.exceptions import NoSuchElementException



class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class PageObjects(object):

    fncount=1
    FileToWriteTo=''  #variable set in relevant test case currently running so output of each test case is written to a different file

    def __init__(self, driver):
        self.driver = driver

    #Generic methods

    def WriteToFile(self, text):

        #If this file doesn't already exist it will be created. If it does exist, it will just be appended to.
        file = open('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test2\OutputFor_' + PageObjects.FileToWriteTo, 'a')
        file.write(text + '\n')

    def Check_For_Text_In_Page(self, text):
        if (text in self.driver.page_source):
            print (color.GREEN +  "PASS: " + text + " found on page." + color.END)
            logging.info ("PASS: " + text + " found on page.")
            self.WriteToFile("PASS: " + text + " found on page.")

            return True
        else:
            print (color.BOLD + color.RED +  "#####FAILURE: Check_For_Text_In_Page##### " + text + " not found on page." + color.END)
            logging.info ("#####FAILURE: Check_For_Text_In_Page##### " + text + " not found on page.")
            self.WriteToFile("#####FAILURE: Check_For_Text_In_Page##### " + text + " not found on page.")
            self.Take_Screen_Shot(self.driver.current_url)
            return False

    def Take_Screen_Shot(self, url):    #this is called by other methods in this class where the verification has failed
        #self.driver.get(url)
        time.sleep (5)
        #rng=random.random()
        DateTime = datetime.datetime.now()
        line = str(DateTime)
        line = line.translate(None, ' :.')
        print (color.BOLD + color.RED +  "#####Failed Screenshot taken of url: " + url + " -Saved to C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test2\screenshot_" + str(PageObjects.fncount) + "_" + str(line) + '.png' + color.END)
        logging.info ("Error: " + str(PageObjects.fncount) + " #####Failed Screenshot taken of url: " + url + " -Saved to C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test2\screenshot_" + str(PageObjects.fncount)+ "_" + str(line)  + '.png')
        self.WriteToFile("Error: " + str(PageObjects.fncount) + " #####Failed Screenshot taken of url: " + url + " -Saved to C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test2\screenshot_" + str(PageObjects.fncount)+ "_" + str(line)  + '.png')

        self.driver.save_screenshot('C:\Users\lw\PycharmProjects\FirstSeleniumTest\Test2\screenshot_' + str(PageObjects.fncount)+ "_" + str(line) + '.png')
        PageObjects.fncount +=1



    #Specific pages (objects\methods)

    #Home Page (General public facing)
    ####################################################################################################################

    #Navigation methods
    def HomePage_NavigateTo (self):
        self.driver.get("https://www.jobserve.com/gb/en/Job-Search/")

    def HomePage_SignIn_Click (self):
        self.driver.find_element_by_link_text("Sign In/Register").click()
        self.driver.find_element_by_xpath("//*[@id='mnuouter']/ul[2]/li/ul/li[1]/a").click()

    # LOGIN
    ####################################################################################################################

    #Navigation methods
    def Login_Cookies_Click(self):
        self.driver.find_element_by_xpath("//*[@id='PolicyOptInLink']").click()

    def Login_UserName_EnterText(self, user_name):
        self.driver.find_element_by_id("txbEmail").click()  # Enter login details (email\password)
        self.driver.find_element_by_id("txbEmail").clear()
        self.driver.find_element_by_id("txbEmail").send_keys(user_name)  # Enter text into text box

    def Login_Password_EnterText(self, password):
        self.driver.find_element_by_id("txbPassword").click()
        self.driver.find_element_by_id("txbPassword").clear()
        self.driver.find_element_by_id("txbPassword").send_keys(password)

    def Login_Submit_Click(self):
        self.driver.find_element_by_id("btnlogin").click()  # press log in button

    #My Home Page (after logging in)
    ####################################################################################################################

    #Navigation methods
    def TopMenu_HomeIcon_Click(self):
        self.driver.find_element_by_xpath("//*[@id='mnuouter']/ul[1]/li[1]/a").click()

    def HomePage_ViewProfile_Click(self):
        self.driver.find_element_by_xpath("//*[@id='ProfileTab']/div[1]/h2/a").click()

    def HomePage_WithinDaysDDL_Select(self,item):
        select = Select(self.driver.find_element_by_id("selAge"))
        select.select_by_visible_text(item)

    def HomePage_LogOut_Click(self):
        self.driver.find_element_by_id ("signout").click()


    #Verifcation methods
    def HomePage_CountriesCheckBox_isChecked(self, value):
        checkbox = self.driver.find_element_by_id("UseMyCountries")
        result = str(checkbox.is_selected())
        if (result == value):
            print (color.GREEN +  "PASS: Include countries checkbox set correctly" + color.END)
            logging.info("PASS: Include countries checkbox set correctly")
            self.WriteToFile("PASS: Include countries checkbox set correctly")
        else:
            print (color.BOLD + color.RED +  "#####FAILURE: HomePage_CountriesCheckBox_isChecked##### Checkbox set to " + str(checkbox.is_selected()) + " not " + value + color.END)
            logging.info("#####FAILURE: HomePage_CountriesCheckBox_isChecked##### Checkbox set to " + str(checkbox.is_selected()) + " not " + value)
            self.WriteToFile("#####FAILURE: HomePage_CountriesCheckBox_isChecked##### Checkbox set to " + str(checkbox.is_selected()) + " not " + value)
            self.Take_Screen_Shot(self.driver.current_url)

    # My Profile Page
    ####################################################################################################################

    # Verifcation methods
    def MyProfile_HomeLocation_VerifyAttr (self, text):
        if (self.driver.find_element_by_id("homeLoc").get_attribute("value") == text):
            print (color.GREEN +  "PASS: Home Location Correct" + color.END)
            logging.info("PASS: Home Location Correct")
            self.WriteToFile("PASS: Home Location Correct")
        else:
            print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_HomeLocation_VerifyAttr##### - Home Location wrong on Profile: " + (self.driver.find_element_by_id("homeLoc").get_attribute("value")) + " != " + text + color.END)
            logging.info("#####FAILURE: MyProfile_HomeLocation_VerifyAttr##### - Home Location wrong on Profile: " + (self.driver.find_element_by_id("homeLoc").get_attribute("value")) + " != " + text)
            self.WriteToFile("#####FAILURE: MyProfile_HomeLocation_VerifyAttr##### - Home Location wrong on Profile: " + (self.driver.find_element_by_id("homeLoc").get_attribute("value")) + " != " + text)
            self.Take_Screen_Shot(self.driver.current_url)

    def MyProfile_PrintIcon_isElementPresent(self):
        try:
            self.driver.find_element_by_xpath("//*[@id='printprofile']")
        except NoSuchElementException:
            print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing." + color.END)
            logging.info("#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing.")
            self.WriteToFile("#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing.")
            self.Take_Screen_Shot(self.driver.current_url)
        return True

    def MyProfile_PrintIcon_isElementVisible(self, value):
        try:
            self.driver.find_element_by_xpath("//*[@id='printprofile']")  #check element exists first
            result = str(self.driver.find_element_by_xpath("//*[@id='printprofile']").is_displayed())
            if ( result != value):   #now check if element should or should not be displayed
                if (result == 'True'):
                    print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should not be visible." + color.END)
                    logging.info("#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should not be visible.")
                    self.WriteToFile("#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should not be visible.")
                else:
                    print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should be visible." + color.END)
                    logging.info("#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should be visible.")
                    self.WriteToFile("#####FAILURE: MyProfile_PrintIcon_isElementVisible##### - Print icon should be visible.")
                self.Take_Screen_Shot(self.driver.current_url)
            else:
                print (color.GREEN +  "PASS: Print icon visibility status is correct" + color.END)
                logging.info("PASS: Print icon visibility status is correct")
                self.WriteToFile("PASS: Print icon visibility status is correct")
        except NoSuchElementException:
            print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing." + color.END)
            logging.info("#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing.")
            self.WriteToFile("#####FAILURE: MyProfile_PrintIcon_isElementPresent##### - Print icon missing.")
            self.Take_Screen_Shot(self.driver.current_url)

    def MyProfile_Availablity_VerifyElementText(self,text):
        if (self.driver.find_element_by_xpath("//*[@id='availability']/option[1]").text == text):
            print (color.GREEN +  "PASS: " + text + " found in Availability element." + color.END)
            logging.info("PASS: " + text + " found in Availability element.")
            self.WriteToFile("PASS: " + text + " found in Availability element.")
        else:
            print (color.BOLD + color.RED +  "#####FAILURE: MyProfile_Availablity_VerifyElementText##### " + (self.driver.find_element_by_xpath("//*[@id='availability']/option[1]").text) + " != " + text + color.END)
            logging.info ("#####FAILURE: MyProfile_Availablity_VerifyElementText##### " + (self.driver.find_element_by_xpath("//*[@id='availability']/option[1]").text) + " != " + text)
            self.WriteToFile("#####FAILURE: MyProfile_Availablity_VerifyElementText##### " + (self.driver.find_element_by_xpath("//*[@id='availability']/option[1]").text) + " != " + text)
            self.Take_Screen_Shot(self.driver.current_url)








