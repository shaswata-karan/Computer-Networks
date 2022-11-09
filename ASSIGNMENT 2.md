# Cisco Packet Tracer Lab - Basic Switch Configuration | Hostname | Password

## 1) Configure the hostname of thr switch as SW1

Switch>enable

Switch#config t

Enter configuration commands,one per line. End with CNTL/Z

Switch(config)#hostname SW1

SW1(config)#

Exit 2 times.

## 2) Set a message of the day (MOTD) banner for the switch

  *****************************  Only Authorized Users Allowed  *****************************
  
SW1#config t

SW1(config)#banner ?

SW1(config)#banner motd ?

SW1(config)#banner motd $

  *****************************  Only Authorized Users Allowed  *****************************

$

SW1(config)#exit

exit

  
## 3.i) Configure a line console password - India@123
## 3.ii) Configure a enable secret paswword - uem@123

SW1>en

SW1#sh run

SW1#config t

SW1(config)#line con 0

SW1(config-line)#password India@123

SW1(config-line)#exit

SW1(config)#enable secret Uem@123

SW1(config)#line con 0

SW1(config-line)#login

SW1(config-line)#

SW1(config-line)#exit

SW1(config)#exit

SW1#

Exit
