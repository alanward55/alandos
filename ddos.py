import os, sys, time, urllib2, threading, random, re

run = os.system
run('clear')
print '------------[Welcome to AlanDoS]------------\n'
print"  \'========================================.  "
print"  |Pembuat: Alan Ward    |Asli indonesia   | "
print"  |IG     : uli_karaba   |+62-853-2672-8933| "
print"  \'========================================.  "
link = raw_input('\nMasukkan link dengan http/https: ')
print '\n[Ctrl+z untuk menghentikan]\n'
animasi = ["L","Lo","Loa", "Load", "Loadi", "Loadin", "Loading", "Loading.", "Loading..", "Loading...", "Loading...."]
for i in range(len(animasi)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animasi[i % len(animasi)])
    sys.stdout.flush()
print'\033[1;31m\n_______________________\n'
run('python2 attack.py '+link)
