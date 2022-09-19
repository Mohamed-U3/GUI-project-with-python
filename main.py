import serial.tools.list_ports

while True:
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []

    # passing through all the ports that is connected to the computer then printing them
    for port in ports:
        portList.append(str(port))
        print(str(port))
    #input selected port
    val = input("select port: COM")
    print("\n")
    #insure you selected one of the existed port then printing the selected one
    for x in range(0,len(portList)):
        if portList[x].startswith("COM" + str(val)):
            portvar = "COM" + str(val)
            print("\nYou selected")
            print(portList[x])

    try:
        portvar
    except NameError:
        print("You selected wrong Port it Seems")
        print("The available Ports are :")
    else:   #initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

while True:
    if serialInst.in_waiting:
        packet = serialInst.readline()
        print(packet.decode("utf").rstrip('\n'))