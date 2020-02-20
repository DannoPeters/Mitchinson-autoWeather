import time
import sys
try:
	from selenium import webdriver
except ImportError:
    sys.exit("\tError1: Selenium is required. please install using 'pip install selenium' or download from https://pypi.org/project/selenium/")




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

#Combined GFA TIF
graphWX = "https://dannopeters.ca/graphical-weather/"

#Depart=CYXE&Location=F&EnRoute=CYYN&Location2=C&Destination=CYQR&Location3=P&Alternates=CYKY&Location4
#Chnage 4 letter airport acronyms to change dislayed METARs and TAFs 
southMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYYN&Location2=C&Destination=CYQR&Location3=P&Alternates=CYKY&Location4=T&SauveReq=actif&cw_metar=raw_metar"
northMETAR = "https://flightplanning.navcanada.ca/cgi-bin/route.cgi?Langue=anglais&TypeBrief=R&TypeTriage=R&NoSession=NS_Inconnu&Version=T&Corridor=50&Depart=CYXE&Location=F&EnRoute=CYLL&Location2=C&Destination=CYQW&Location3=P&Alternates=CYPA&Location4=T&SauveReq=actif&cw_metar=raw_metar"

#CHnage the times below to chnage the dwell time on each screen
dwellSchedule = 20
dwellRVR = 20
dwellGFA = 30
dwellMETAR = 30

#choose your favourite web browser

try:
	rvr = webdriver.firefox.webdriver.WebDriver()

	#gfa = [webdriver.firefox.webdriver.WebDriver(), webdriver.firefox.webdriver.WebDriver(), webdriver.firefox.webdriver.WebDriver()]
	wx = webdriver.firefox.webdriver.WebDriver()
	#tif = [webdriver.firefox.webdriver.WebDriver(), webdriver.firefox.webdriver.WebDriver(), webdriver.firefox.webdriver.WebDriver()]

	north = webdriver.firefox.webdriver.WebDriver()
	south = webdriver.firefox.webdriver.WebDriver()
except Exception as e:
	sys.exit('\tError: Firefox driver is required. Please install "geckodriver" from https://github.com/mozilla/geckodriver or "pip install webdriverdownloader" and run "webdriverdownloader firefox" and update PATH.\n\n' + str(e))

#open all web addresses
#loop = [0,1,2]
#for i in loop:
#	gfa[i].get(liveGFA[i])
wx.get(graphWX)
rvr.get(liveRVR)
north.get(northMETAR)
south.get(southMETAR)

while 1:
	#show RVR
	rvr.maximize_window()
	south.minimize_window()
	north.minimize_window()
	wx.minimize_window()
	#for i in loop:
	#	gfa[i].minimize_window()
	time.sleep(dwellRVR)

	#show GFA
	rvr.minimize_window()
	south.minimize_window()
	north.minimize_window()
	wx.maximize_window()
	#for i in loop:
		#Graphic Area Forecast
	#	gfa[i].get(liveGFA[i])
	#	gfa[i].maximize_window()
	#	gfa[i].set_window_size(680,550)
	#	gfa[i].set_window_position(0+i*640,0)

	#for i in loop:
	#	#Turbulance Icing and Freezing
	#	tif[i].get(liveTIF[i])
	#	tif[i].maximize_window()
	#	tif[i].set_window_size(680,550)
	#	tif[i].set_window_position(0+i*640,520)
		
	time.sleep(dwellGFA)

	#Show Schedule (background)
	rvr.minimize_window()
	south.minimize_window()
	north.minimize_window()
	wx.minimize_window()
	#for i in loop:
	#	gfa[i].minimize_window()
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
	wx.minimize_window()
	#for i in loop:
	#	gfa[i].minimize_window()
	time.sleep(dwellMETAR)


