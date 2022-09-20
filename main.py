import serial.tools.list_ports

while True:
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()

    portList = []

    # passing through all the ports that is connected to the computer
    for port in ports:
        portList.append(str(port))
    # automatic Select Arduino if found
    for x in range(0,len(portList)):
        if "Arduino Uno" in portList[x]:
            portvar = portList[x].split(' ', 1)[0]
            print("\nComputer selected")
            print(portList[x])
    
    # check if Computer Select port or not
    try:
        portvar
    except NameError: # If not selected
        print("Computer did not select port\n")
        print("The available Ports are :")
        # passing through all the ports that is connected to the computer then printing them
        for port in portList:
            print(port)
        #input selected port
        val = input("\nselect port: COM")
        #insure you selected one of the existed port then printing the selected one
        for x in range(0,len(portList)):
            if portList[x].startswith("COM" + str(val)):
                portvar = "COM" + str(val)
                print("\nYou selected")
                print(portList[x])
    else:   #If Selected Then initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

    # insure user Selected the port manually
    try:
        portvar
    except NameError:
        print("You selected non existing Port it Seems")
    else:   #initializing serial port
        serialInst.baudrate = 9600
        serialInst.port = portvar
        serialInst.open()
        break

while True:
    d = input("Enter the Value: ")
    if(d == 'H'):
        serialInst.write(d.encode())
    elif(d == 'L'):
        serialInst.write(d.encode())
    # if serialInst.in_waiting:
    #     packet = serialInst.readline()
    #     print(packet.decode("utf").rstrip('\n'))