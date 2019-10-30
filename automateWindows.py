import time
import sys
try:
	from selenium import webdriver
except ImportError:
    sys.exit("\tError: Selenium is required. please install using 'pip install selenium' or download from https://pypi.org/project/selenium/")




#Change the web adresses below to change where the browser will go to
liveRVR = "https://atm.navcanada.ca/atm/iwv/CYXE"
#liveGFA = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/Latest-gfacn32_cldwx_000-e.html?Produit=GFA&Region=32&Langue=anglais&NoSession=NS_Inconnu&Mode=graph"

#CHnage the times below to chnage the dwell time
dwellSchedule = 10
dwellRVR = 10
dwellGFA = 10

#choose your favourite web browser

while 1:
	try:
		driver = webdriver.firefox.webdriver.WebDriver()
	except:
		sys.exit("\tError: Firefox driver is required. Please install 'geckodriver' from https://github.com/mozilla/geckodriver or download pip install webdriverdownloader and run 'webdriverdownloader firefox' and update PATH.")

	driver.get(liveRVR)
	driver.maximize_window()
	time.sleep(dwellRVR)

	#driver.quit()
	#driver.get(liveGFA)
	#driver.maximize_window()
	#time.sleep(dwellGFA)

	driver.quit()
	#dwell on the schedule in the background
	time.sleep(dwellSchedule)

