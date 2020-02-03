#! /usr/bin/env python3
import subprocess
import re
import argparse

def username_parsing(file, output):
    fd = open(file)
    log = fd.read()

    username_list_all = re.findall("(.*) ssh:notty", log)

    print("Total number of request: ", len(username_list_all), '\n', file=open(output.name, 'a')) if output else print("Total number of request: ", len(username_list_all), '\n')

    return(nbr_username(username_list_all))

def nbr_username(username_list_all):
    scoreboard = {}

    for username in username_list_all:
        if username not in scoreboard:
            scoreboard[username] = 1
        else:
            scoreboard[username] = scoreboard[username] + 1

    return(scoreboard)

def ip_parsing(file, arg, output):
    fd = open(file)
    log = fd.read()
    ip_list = []

    ip_list_all = re.findall(r"[0-9]+(?:\.[0-9]+){3}", log)

    if arg == "ip":
        for ip in ip_list_all:
            if ip not in ip_list:
                ip_list.append(ip)
        print("Total number of ip: ", len(ip_list), '\n', file=open(output.name, 'a')) if output else print("Total number of ip: ", len(ip_list), '\n')
        return(ip_lookup(ip_list))
    elif arg == "req":
        print("Total number of request: ", len(ip_list_all), '\n', file=open(output.name, 'a')) if output else print("Total number of request: ", len(ip_list_all), '\n')
        return(ip_lookup(ip_list_all))

def ip_lookup(ip_list):
    scoreboard = {}

    for ip in ip_list:
        country = subprocess.check_output(["geoiplookup", ip], encoding="utf-8")
        # Change this value if you get a different output from geoiplookup
        country = country[23:]
        country_clean = country.rstrip()
        if country_clean not in scoreboard:
            scoreboard[country_clean] = 1
        else:
            scoreboard[country_clean] = scoreboard[country_clean] + 1

    return(scoreboard)

def scoreboard_printing(scoreboard, top, output):
    i = 1

    sorted_scoreboard = ({k: v for k, v in sorted(scoreboard.items(), key=lambda item: item[1], reverse=True)})

    if output:
        f = open(output.name, 'a')

    for x in sorted_scoreboard:
        print(i,'#',x, ':', sorted_scoreboard[x], file=f) if output else print(i,'#',x, ':', sorted_scoreboard[x])
        if top and i == top:
            break
        i += 1

def main(args):
    if args.mode == "user":
        scoreboard = username_parsing(args.file, args.output)
    else:
        scoreboard = ip_parsing(args.file, args.mode, args.output)
    
    scoreboard_printing(scoreboard, args.top, args.output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="report_of_the_week", description="Get some idea of where the \"threat\" come from.")
    parser.add_argument("file", help="input file to parse data from")
    parser.add_argument("mode", choices=["req", "ip", "user"], help="select the scoreboard mode (req, ip, user)")
    parser.add_argument("-o", "--output", help="Add an output file, by default will print result in the terminal window", type=argparse.FileType('a'))
    parser.add_argument("-t", "--top", help="Select the number of entry to be displayed on the scoreboard", type=int)

    args = parser.parse_args()

    main(args)