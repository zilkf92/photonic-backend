# sn = "1907988" # Power meter's serial number
# sn = '201117311' # new usb powermeter
# in the CDLAB PC the serial motors are COM4
com1 = 'COM4'
com2 = ''
# in Windows: Find COM port in device manager
com_list = ['COM4', 'COM7', 'COM6']


# pm = open_powermeter(sn,2)# 1: usb pm, other number, non-usb powermeter

# All possible addresses for motos to communicate #
address_list = ['0', '1', '2', '3', '4', '5', '6',
                '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
