import sys
import urllib2

# Lists the domains currently being resolved to localhost
def blockList(filename):
    try:
        f = open(filename, 'r')
        for line in f:
            if line[0] != "#" and line[0] != "\n":
                line = line.replace("\n", "")
                print(line)
        f.close()
    except IOError as e: fileError(e)

# Forces a new domain to resolve to localhost
def blockAdd(webAddress, filename):
    try:
        f = open(filename, 'a+')
        lineToWrite = "127.0.0.1 www." + webAddress + " " + webAddress
        duplicate = False

        for line in f:
            duplicate = duplicate or (lineToWrite == line.replace("\n",""))

        if not duplicate:
            f.write("\n" + lineToWrite)
            print("SUCCESS\nAdded entry 127.0.0.1 www." + webAddress + " " + webAddress)
        else:
            print("FAILED\nWebsite " + webAddress + " is already blocked")
        f.close()
    except IOError as e: fileError(e)

# Stops a domain from being resolved to localhost
def blockRem(webAddress, filename):
    try:
        lineToFind = "127.0.0.1 www." + webAddress + " " + webAddress + "\n"
        f = open(filename, 'r')
        lines = []
        found = False

        for line in f:
            lines.append(line)
            if line[0] != '#' and line[0] != '\n':
                if line[-1] != '\n':
                    line += "\n"
                if line == lineToFind:
                    found = True
                    lines.pop()

        f.close()

        if found:
            f = open(filename, 'w')
            i = 1
            for line in lines:
                if i == len(lines) and line[-1] == "\n":
                    line = line[:-1]
                f.write(line)
                i += 1
            f.close()
            print("SUCCESS\nRemoved " + webAddress + " from list")
        else:
            print("FAILED\nWebsite " + webAddress + " is not currently blocked")
    except IOError as e: fileError(e)

def fileError(e):
    print("Hosts file might not exist, or you're not an admin")
    print("Error: " + str(e))
    sys.exit(1)

def invalid():
    print("|  Invalid command. Use:\n|\n|  COMMAND ARGS\n|\n|  Where COMMAND = list | auto | add <webaddress.com> | remove <webaddress.com>")
    print("|  AUTO pulls a list of domains from my github. You can review them before the sites are blocked")
    print("|  CAUTION: Adding a webaddress will block access to it by making the local DNS to resolve to 127.0.0.1")

# Pull a list of annoying websites to block, blocks them
def serverPull(filename):
    try:
        print("Reading from remote file...")
        data = urllib2.urlopen("https://raw.githubusercontent.com/IwanCole/AdBlock/master/blocklist.txt").read(20000)
        sites = data.split("\n")
        print("\nThe following webaddresses will be blocked:\n" + str(data))

        invalid = True
        while invalid:
            conf = raw_input("Are you sure you would like to continue? Y/N\n")
            if str(conf).lower() == "y" or str(conf).lower() == "n": invalid = False

        if str(conf).lower() == "y":
            for line in sites[:-1]:
                blockAdd(line, filename)
        else: print("Never mind")

    except IOError as e:
        print("Something went wrong :(\n" + str(e))

# Selects correct hosts file depending on OS
def pickFilename():
    if sys.platform.startswith('win32'):
        return "C:\Windows\System32\drivers\etc\hosts"
    elif sys.platform.startswith('darwin') or sys.platform.startswith('linux'):
        return "/etc/hosts"
    else: return 1

def main(args):
    filename = pickFilename()
    if filename == 1:
        print("Error selecting platform")
    else:
        if len(args) == 4 or len(args) == 3 or len(args) == 2:
            if args[-1] == "list":
                if len(args) == 3 or len(args) == 2:
                    blockList(filename)
                else:
                    invalid()
            elif args[-1] == "auto":
                if len(args) == 3 or len(args) == 2:
                    serverPull(filename)
                else:
                    invalid()
            elif args[-2] == "add":
                if len(args) == 4 or len(args) == 3:
                    blockAdd(args[-1], filename)
                else:
                    invalid()
            elif args[-2] == "remove":
                if len(args) == 4 or len(args) == 3:
                    blockRem(args[-1], filename)
                else:
                    invalid()
            else:
                invalid()
        else:
            invalid()

if __name__ == "__main__":
    main(sys.argv)
