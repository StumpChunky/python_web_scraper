import time
from selenium import webdriver

url = "https://makershare.com/projects/makevember"

#choose browser (Firefox/Chrome) and import url (change url link above)
driver = webdriver.Firefox()
driver.get(url)

#delay - since Maker Share has multi-stage JS loading
print("start")
time.sleep(10)

#grab source data and close browser
content = driver.page_source #save page content
driver.quit() #close browser

#print html to a file
with open("output.html", "w") as text_file:
    print(content, file=text_file)

#a heads up to let me know the code is finished running
print("done")
