#!/usr/bin/env python

import dbus
import dbus.service

from PyQt4.QtCore import QCoreApplication,QTimer
from dbus.mainloop.qt import DBusQtMainLoop
from subprocess import call

class SleepCtl(dbus.service.Object):
    def __init__(self):
        name = dbus.service.BusName('com.dbsleep.SleepCtl', bus=dbus.SessionBus())
        dbus.service.Object.__init__(self, name, '/SleepCtl')

    @dbus.service.method('com.dbsleep.SleepCtl', in_signature='', out_signature='')
    def Sleep(self):
        call(["/usr/bin/systemctl", "suspend"])

def loop():
    DBusQtMainLoop(set_as_default=True)
    app = QCoreApplication([])
    ctl = SleepCtl()
    app.exec_()

loop()
