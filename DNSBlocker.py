import sys

filename = "C:\Windows\System32\drivers\etc\hosts"

def blockList():
    f = open(filename, 'r')
    for line in f:
        if line[0] != "#" and line[0] != "\n":
            line = line.replace("\n", "")
            print(line)
    f.close()

def blockAdd(webAddress):
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

def blockRem(webAddress):
    lineToFind = "127.0.0.1 www." + webAddress + " " + webAddress + "\n"
    f = open(filename, 'r')
    lines = []
    found = False

    for line in f:
        lines.append(line)
        # line = line.replace"
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

def invalid():
    print("|  Invalid command. Use:\n|\n|  COMMAND ARGS\n|\n|  Where COMMAND = list | add <webaddress.com> | remove <webaddress.com>")
    print("|  CAUTION: Adding a webaddress will block access to it by making the local DNS to resolve to 127.0.0.1")


def main(args):
    if len(args) == 4 or len(args) == 3:
        if args[2] == "list":
            if len(args) == 3:
                blockList()
            else:
                invalid()
        elif args[2] == "add":
            if len(args) == 4:
                blockAdd(args[3])
            else:
                invalid()
        elif args[2] == "remove":
            if len(args) == 4:
                blockRem(args[3])
            else:
                invalid()
        else:
            invalid()
    else:
        invalid()

if __name__ == "__main__":
    main(sys.argv)
