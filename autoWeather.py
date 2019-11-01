import time
import sys
try:
	from selenium import webdriver
except ImportError:
    sys.exit("\tError: Selenium is required. please install using 'pip install selenium' or download from https://pypi.org/project/selenium/")




#Change the web adresses below to change where the browser will go to
liveRVR = "https://atm.navcanada.ca/atm/iwv/CYXE"
liveGFA = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_cldwx_000.png"
southMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYYN&Location2=C&Destination=CYQR&Location3=P&Alternates=CYKY&Location4=T&SauveReq=actif&cw_metar=raw_metar"
northMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYLL&Location2=C&Destination=CYQW&Location3=P&Alternates=CYPA&Location4=T&SauveReq=actif&cw_metar=raw_metar"

#CHnage the times below to chnage the dwell time
dwellSchedule = 20
dwellRVR = 20
dwellGFA = 20
dwellMETAR = 30

#choose your favourite web browser

try:
	rvr = webdriver.firefox.webdriver.WebDriver()
	gfa = webdriver.firefox.webdriver.WebDriver()
	north = webdriver.firefox.webdriver.WebDriver()
	south = webdriver.firefox.webdriver.WebDriver()
except:
	sys.exit("\tError: Firefox driver is required. Please install 'geckodriver' from https://github.com/mozilla/geckodriver or download pip install webdriverdownloader and run 'webdriverdownloader firefox' and update PATH.")

rvr.get(liveRVR)
gfa.get(liveGFA)
north.get(northMETAR)
south.get(southMETAR)

while 1:
	#show RVR
	rvr.maximize_window()
	gfa.minimize_window()
	south.minimize_window()
	north.minimize_window()
	time.sleep(dwellRVR)

	#show GFA
	gfa.get(liveGFA) 
	rvr.minimize_window()
	gfa.maximize_window()
	south.minimize_window()
	north.minimize_window()
	time.sleep(dwellGFA)

	#Show Schedule (background)
	rvr.minimize_window()
	gfa.minimize_window()
	south.minimize_window()
	north.minimize_window()
	time.sleep(dwellSchedule)

	#Show Metars
	north.get(northMETAR)
	south.get(southMETAR)
	south.maximize_window()
	south.set_window_size(960,1040)
	south.set_window_position(0,0)
	south.execute_script("window.scrollTo(0, 1000)")
	north.maximize_window()
	north.set_window_size(960,1040)
	north.set_window_position(960,0)
	north.execute_script("window.scrollTo(0, 1000)")
	rvr.minimize_window()
	gfa.minimize_window()
	time.sleep(dwellMETAR)


