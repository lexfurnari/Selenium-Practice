# Practice Selenium
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHFSUFc5cjVtOXBCTFAwb1VUeUhmbVR1bC0tZ3xBQ3Jtc0ttZk1qR29YR2JaZFdrNk80aUEwQ3F4RmNjM1VVMmh0SlFydHlaZUF0dHJQaGxVYnBlUER6UGY0MUF3M2Q2OWlva3VLSFFZa2dVMUI4WENmOHRrQ3JXTTIydUx3Y0NGb3RDNkZhMW9BeW9GdFNXQnc2aw&q=https%3A%2F%2Fsites.google.com%2Fa%2Fchromium.org%2Fchromedriver%2Fdownloads
from selenium import webdriver

#give access to enter and escape key
from selenium.webdriver.common.keys import Keys
import time

PATH = "/Users/alexafurnari/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)

#websiteName = input("Enter website name here: ")
#driver.get(websiteName)

driver.get("techwithtim.net")


print(driver.title)

#Find search box on website
search = driver.find_element_by_class_name("s")
#send "test" into the search box input field
search.send_keys("test")
#hits enter
search.send_keys(Keys.RETURN)

# can access entire source code of the entire website
print(driver.page_source)

#delay actions so you can see them 
time.sleep(5)

#quitReq = 'none'
#while quitReq == "quit":
    #driver.quit()
    #print("bye bye")






