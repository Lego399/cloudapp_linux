import pygtk
pygtk.require('2.0')
import gtk
import appindicator
import sys
import pynotify
from pycloudapp.cloud import Cloud
import os
from datetime import datetime
import time
import re
mycloud = Cloud()
mycloud.auth('lego399@gmail.com', 'CdE33345tG')

# mycloud.list_items()
# for arg in sys.argv[1:]:
#	mycloud.upload_file(arg)

class AppIndicatorExample:
    def __init__(self):
        self.ind = appindicator.Indicator("cloudapp", "cloudapp-idle-black", appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status (appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("cloudapp-uploading-black")
        self.ind.set_icon("cloudapp-idle-black")

	# define functions

	def matchRegex(rawdata):
		txt = rawdata
		re1='.*?'	# Non-greedy match on filler
		re2='(http)'	# Word 1
		re3='(:)'	# Any Single Character 1
		re4='(\\/)'	# Any Single Character 2
		re5='((?:\\/[\\w\\.\\-]+)+)'	# Unix Path 1
		rg = re.compile(re1+re2+re3+re4+re5,re.IGNORECASE|re.DOTALL)
		m = rg.search(txt)
		if m:
			word1=m.group(1)
			c1=m.group(2)
			c2=m.group(3)
			unixpath1=m.group(4)
			url = word1+c1+c2+unixpath1
			print url
	def upload(filename):
		self.ind.set_icon("cloudapp-uploading-black")
		print 'Uploading!'
		mycloud.upload_file(filename)
		matchRegex(str(mycloud.list_items(page=1, per_page=1)))
		os.system("""notify-send 'CloudApp' 'File has been uploaded'""")
		self.ind.set_icon("cloudapp-success-black")
		print 'Success!'
		time.sleep(5)
		self.ind.set_icon("cloudapp-idle-black")
		os.system("rm " + filename)
		print 'Back to idle'
		
	def uploadSelective():
		t = datetime.now().strftime("%H_%M_%S_%d-%m-%Y")
		os.system("scrot -s " + t + ".png")
		upload(t + ".png")

	def uploadScreenshot():
		t = datetime.now().strftime("%H_%M_%S_%d-%m-%Y")
		time.sleep(2)
		os.system("scrot " + t + ".png")
		upload(t + ".png")

	def uploadselective_callback(widget=None, data=None):
		uploadSelective()
		
	def uploadscreenshot_callback(widget=None, data=None):
		uploadScreenshot()

        # create a menu
        self.menu = gtk.Menu()

        # create items for the menu - labels, checkboxes, radio buttons and images are supported:
        
        screenshot = gtk.MenuItem("Upload Screenshot")
        screenshot.connect("activate", uploadscreenshot_callback)
        screenshot.show()
        self.menu.append(screenshot)

        selectivescreenshot = gtk.MenuItem("Upload Selective Screenshot")
        selectivescreenshot.connect("activate", uploadselective_callback)
        selectivescreenshot.show()
        self.menu.append(selectivescreenshot)

        radio = gtk.RadioMenuItem(None, "Radio Menu Item")
        radio.show()
        self.menu.append(radio)

        image = gtk.ImageMenuItem(gtk.STOCK_QUIT)
        image.connect("activate", self.quit)
        image.show()
        self.menu.append(image)
                    
        self.menu.show()

        self.ind.set_menu(self.menu)

    def quit(self, widget, data=None):
        gtk.main_quit()


def main():
    gtk.main()
    return 0

if __name__ == "__main__":
    indicator = AppIndicatorExample()
    main()
