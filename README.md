# Report of the week

The goal of this simple script is to parse the output of the the ```lastb``` command and dress a scoreboard of, unique IP by country or number of request by country or the most tried username, in order to get some insight on the "threat" against your ssh service (it can also work with the fail2ban jail status output or other file containing IP address)

## Requirement

The script use the ```geoiplookup``` command in order to check IP location<br>
```sudo apt-get install geoiplookup```

(if you use a different database file for ```geoiplookup``` you might need to change some value in the ```ip_lookup()``` function to get the proper output)

## Usage
```
usage: report_of_the_week [-h] [-o OUTPUT] [-t TOP] file {req,ip,user}

Get some idea of where the "threat" come from.

positional arguments:
  file                  input file to parse data from
  {req,ip,user}         select the scoreboard mode (req, ip, user)

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Add an output file, by default will print result in
                        the terminal window
  -t TOP, --top TOP     Select the number of entry to be displayed on the
                        scoreboard
```

## Example

Command output in ```req``` mode

```
./report_of_the_week.py lastb.log req

Total number of request:  498 

1 # CN, China : 432
2 # BE, Belgium : 17
3 # KR, Korea, Republic of : 13
4 # IP Address not found : 7
5 # FR, France : 6
6 # NL, Netherlands : 4
7 # CA, Canada : 2
8 # US, United States : 2
9 # GB, United Kingdom : 2
10 # ES, Spain : 2
11 # IN, India : 2
12 # SG, Singapore : 2
13 # PE, Peru : 2
14 # ID, Indonesia : 2
15 # IQ, Iraq : 1
16 # PL, Poland : 1
17 # DK, Denmark : 1
```

Command output in ```ip``` mode

```
./report_of_the_week.py lastb.log ip

Total number of ip:  59 

1 # CN, China : 37
2 # FR, France : 4
3 # KR, Korea, Republic of : 2
4 # NL, Netherlands : 2
5 # IP Address not found : 2
6 # BE, Belgium : 1
7 # CA, Canada : 1
8 # IQ, Iraq : 1
9 # PL, Poland : 1
10 # DK, Denmark : 1
11 # US, United States : 1
12 # GB, United Kingdom : 1
13 # ES, Spain : 1
14 # IN, India : 1
15 # SG, Singapore : 1
16 # PE, Peru : 1
17 # ID, Indonesia : 1
```
Command output in ```user``` mode

```
./report_of_the_week.py lastb.log user

Total number of request:  498 

1 # root     : 431
2 # admin    : 6
3 # guest    : 4
4 # Lyyli    : 2
5 # rpc      : 2
6 # backup   : 2
7 # herbert  : 2
8 # mennella : 2
9 # urena    : 2
10 # mysql    : 2
11 # myroon   : 2
12 # loevaas  : 2
13 # apache   : 2
14 # amenta   : 2
15 # limido   : 2
16 # eminem   : 2
17 # komrij   : 2
18 # force    : 2
19 # cav      : 2
20 # pywang   : 2
21 # guilhem  : 2
22 # pharmer  : 2
23 # beatton  : 2
24 # maio     : 2
25 # frangia  : 2
26 # password : 2
27 # ubnt     : 2
28 # phpmy    : 2
29 # arnal    : 2
30 # julia    : 2
31 # mail     : 1
32 # bin      : 1
33 # www-data : 1
```

## TODO

- The possibility to take input from the standard output in order to do ``` lastb | ./the_report_of_the_week.py req``` for example (but on a low capacities server you might prefer to ```scp``` the file to your computer and run the script there)

- See for any optimization in order to decrease process time