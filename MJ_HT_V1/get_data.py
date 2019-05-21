import bluepy
import datetime

# Klasa do obsługi callbacków:
class CallMaster(bluepy.btle.DefaultDelegate):
    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        print("O ja cię, coś tu przylazło!")
        print(scanEntry.addr, isNewDev, isNewData)
        if scanEntry.addr == "58:2d:34:30:bd:44":
            print(datetime.datetime.now())
            gsd = scanEntry.getScanData()
            print(type(gsd))
            print("Ej! To nasz czujnik!", gsd)
            uuid = bluepy.btle.UUID("0000fe95-0000-1000-8000-00805f9b34fb")
            print(uuid.binVal)

# Obiekt delegacyjny:
deleg = CallMaster()

# Weź sobie poskanuj:
s = bluepy.btle.Scanner()
s.withDelegate(deleg)
#z = s.scan(60)
s.start()
s.process(60)
s.stop()
