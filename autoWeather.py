import time
import sys
try:
	from selenium import webdriver
except ImportError:
    sys.exit("\tError: Selenium is required. please install using 'pip install selenium' or download from https://pypi.org/project/selenium/")




#Change the web adresses below to change where the browser will go to
liveRVR = "https://atm.navcanada.ca/atm/iwv/CYXE"

#GFA 0, 6, and 12 hour
liveGFA = ["","",""]
liveGFA[0] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_cldwx_000.png"
liveGFA[1] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_cldwx_006.png"
liveGFA[2] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_cldwx_012.png"

#TIF 0, 6, and 12 hour
liveTIF = ["","",""]
liveTIF[0] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_turbc_000.png"
liveTIF[1] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_turbc_006.png"
liveTIF[2] = "https://flightplanning.navcanada.ca/Latest/gfa/anglais/produits/uprair/gfa/gfacn32/Latest-gfacn32_turbc_012.png"

#Depart=CYXE&Location=F&EnRoute=CYYN&Location2=C&Destination=CYQR&Location3=P&Alternates=CYKY&Location4
#Chnage 4 letter airport acronyms to change dislayed METARs and TAFs 
southMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYYN&Location2=C&Destination=CYQR&Location3=P&Alternates=CYKY&Location4=T&SauveReq=actif&cw_metar=raw_metar"
northMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYLL&Location2=C&Destination=CYQW&Location3=P&Alternates=CYPA&Location4=T&SauveReq=actif&cw_metar=raw_metar"

#CHnage the times below to chnage the dwell time on each screen
dwellSchedule = 1
dwellRVR = 1
dwellGFA = 20
dwellMETAR = 1

#choose your favourite web browser

try:
	rvr = webdriver.firefox.webdriver.WebDriver()

	gfa[0] = webdriver.firefox.webdriver.WebDriver()
	gfa[1] = webdriver.firefox.webdriver.WebDriver()
	gfa[2] = webdriver.firefox.webdriver.WebDriver()

	tif[0] = webdriver.firefox.webdriver.WebDriver()
	tif[1] = webdriver.firefox.webdriver.WebDriver()
	tif[2] = webdriver.firefox.webdriver.WebDriver()

	north = webdriver.firefox.webdriver.WebDriver()
	south = webdriver.firefox.webdriver.WebDriver()
except:
	sys.exit("\tError: Firefox driver is required. Please install 'geckodriver' from https://github.com/mozilla/geckodriver or download pip install webdriverdownloader and run 'webdriverdownloader firefox' and update PATH.")

#open all web addresses
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
	rvr.minimize_window()
	south.minimize_window()
	north.minimize_window()
	loop = [0,1,2]
	for i in loop:
		#Graphic Area Forecast
		gfa[i].get(liveGFA[i])
		gfa[i].maximize_window()
		gfa[i].set_window_size(640,520)
		gfa[i].set_window_position(0,0+i*640)

		#Turbulance Icing and Freezing
		tif[i].get(liveTIF[i])
		tif[i].maximize_window()
		tif[i].set_window_size(640,520)
		tif[i].set_window_position(520,0+i*640)
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


