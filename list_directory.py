#function to take the filename
def CalculateIPHits(filename):
    # Make a dictionary to store IP addresses and their hit counts
    # and read the contents of the log file line by line
    IP_LIST = {}
    Contents = open(filename, "r").readlines(  )
    # Loop through each line of the logfile
    for line in Contents:
        # Split the string to isolate the IP address
        Ip = line.split(" ")[0]
        # To Ensure the length of IP Adress
        if 6 < len(Ip) <= 15:
            # Increase by 1 if IP exists; else set hit count = 1
            IP_LIST[Ip] = IP_LIST.get(Ip, 0) + 1

    # sorted function will sort IP in descending and then take first 10
    res = sorted(IP_LIST, key=IP_LIST.get, reverse=True)[:10]
    return res

filepath="C:/Users/Harry/PycharmProjects/hacker_Earth/access.log"
HitsDictionary = CalculateIPHits(filepath)
print (HitsDictionary)