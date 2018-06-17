#Written by Ann Mauck
#A simple application that resides in the system tray and allows for ejecting one's optical drive tray by clicking or right clicking on the icon

import appindicator #appindicators are what Mint calls system tray icons
import gtk, sys, os
from subprocess import call #needed for bash commands

path = os.path.abspath(os.path.dirname(sys.argv[0]))
ai = appindicator.Indicator('tray_ejector', path + '/icon.png', appindicator.CATEGORY_APPLICATION_STATUS)
ai.set_status(appindicator.STATUS_ACTIVE)
m = gtk.Menu()
tt = gtk.MenuItem( 'Toggle Tray' )
qi = gtk.MenuItem( 'Quit' )

m.append(tt)
m.append(qi)

ai.set_menu(m)
tt.show()
qi.show()

def eject(item):
        call(['eject', '-T']) #calls bash's eject function with the toggle switch

tt.connect('activate', eject)

def quit(item):
        gtk.main_quit()

qi.connect('activate', quit)
gtk.main()

