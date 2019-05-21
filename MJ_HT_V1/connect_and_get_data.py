import bluepy

mt = bluepy.btle.Peripheral("58:2D:34:30:BD:44")
z = mt.getServices()
for x in z:
    cha = x.getCharacteristics()
    for b in cha:
        if b.supportsRead():
            print(b.read().hex())
'''
ser = mt.getServiceByUUID("0000fe95-0000-1000-8000-00805f9b34fb")
print(ser)
cha = ser.getCharacteristics()

for x in cha:
    print(x.read().hex())
'''