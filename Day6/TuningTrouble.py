def marker(file):
    packet_marker = 0
    packet_found = False
    message_marker = 0
    message_found = False
    with open(file) as datastreamBuffer:
        for datastream in datastreamBuffer:
            packet_initial = 0
            packet_last = 3
            message_initial = 0
            message_last = 13
            for i in range(len(datastream)):
                packet_check = set(datastream[packet_initial+i:packet_last+i+1])
                message_check = set(datastream[message_initial+i:message_last+i+1])
                if len(packet_check) == 4 and packet_found != True:
                    packet_marker = packet_last+i+1
                    packet_found = True
                if len(message_check) == 14 and message_found != True:
                    message_marker = message_last+i+1
                    message_found = True
    return packet_marker, message_marker


print(marker("DataStreamBuffer"))