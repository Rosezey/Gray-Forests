import math

health = 1.0
battery = 1.0
phyarmor = 1
ammoarmor = 1
elecarmor = 1
wifiarmor = 1
pierce = 1
dmgelec = 1
dmgphys = 1
dmgammo = 1
dmgwifi = 1
reload = 1
dex = 1
accuracy = random.randint(0,100) += dex
dodge = (dex *= 3)
alive = True
mobile = False
turnres = 1.0
turn = 1
exp = 0.0
level = 1
if exp == 50 * level;
 level += 1


robotype = hound

# Selectable robotypes (enemies can have these robotypes)

if robotype == hound;
 pierce *= 2.0
 health /= 1.5
 dex *= 1.5
 turnres += 1.0
 armor /= 2.0
 dmgphys *= 2.0
 dmgelec *= 2.0
 dmgammo /= 2.0
 reload *= 2
 phyarmor /= 2.0
 ammoarmor /= 2.0
 elecarmor /= 2.0
 wifiarmor /= 2.0
 mobile == True
if robotype == cyborg;
 battery *= 1.5
 phyarmor *= 1.0
 pierce *= 1.2
 dmgammo *=1.5
 dmgwifi *= 2.0
 dmgelec *=1.2
 reload /= 1.5
 dex *= 2.0
 mobile == True
if robotype == drone;
 health /= 2.0
 phyarmor /= 2.0
 elecarmor /= 2.0
 wifiarmor /= 2.0
 ammoarmor /= 2.0
 dmgphys /= 2.0
 dmgelec /= 2.0
 dmgammo *= 3.0
 dmgwifi *= 3.0
 dex *= 2.0
 turnres *= 2.0
 mobile == True

# Enemy only robot types

if robotype == turret;
 dmgammo *= 1.5
 ammoarmor *= 1.2
 mobile == False

# Enemy boss only robot types

if robotype == arachnoid;
 dmgphys *= 2
 health *= 3
 dex *= 1.5
 mobile == True
