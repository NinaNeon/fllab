
chmod +x ./install_docker.sh
./install_docker.sh




Calculating upgrade... Done
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
nina@ninapi:~ $ sudo apt install git -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
git is already the newest version (1:2.39.5-0+deb12u2).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
nina@ninapi:~ $ git clone https://github.com/MichaelLee-ceo/fllab.git
Cloning into 'fllab'...
fatal: unable to access 'https://github.com/MichaelLee-ceo/fllab.git/': Could not resolve host: github.com
nina@ninapi:~ $ ifconfig wlan0
wlan0: flags=4098<BROADCAST,MULTICAST>  mtu 1500
        ether 2c:cf:67:8a:b1:b4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

nina@ninapi:~ $ ^C
nina@ninapi:~ $ git clone https://github.com/MichaelLee-ceo/fllab.git
Cloning into 'fllab'...
fatal: unable to access 'https://github.com/MichaelLee-ceo/fllab.git/': Could not resolve host: github.com
nina@ninapi:~ $ iconfig wlan0
bash: iconfig: command not found
nina@ninapi:~ $ ifconfig wlan0
wlan0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
        ether 2c:cf:67:8a:b1:b4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

nina@ninapi:~ $ ifconfig wlan0
wlan0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.75.81  netmask 255.255.255.0  broadcast 192.168.75.255
        inet6 fe80::568d:4393:8baf:ed1e  prefixlen 64  scopeid 0x20<link>
        inet6 2402:7500:46a:8908:d13a:cee:10be:cac4  prefixlen 64  scopeid 0x0<global>
        ether 2c:cf:67:8a:b1:b4  txqueuelen 1000  (Ethernet)
        RX packets 17951  bytes 26725522 (25.4 MiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 7051  bytes 614308 (599.9 KiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

nina@ninapi:~ $ git clone https://github.com/MichaelLee-ceo/fllab.git
Cloning into 'fllab'...
Username for 'https://github.com': 
Password for 'https://github.com': 
remote: Repository not found.
fatal: Authentication failed for 'https://github.com/MichaelLee-ceo/fllab.git/'
nina@ninapi:~ $ ssh-keygen -t ed25519 -C "caijingnina@gmail.com"
Generating public/private ed25519 key pair.
Enter file in which to save the key (/home/nina/.ssh/id_ed25519): 
Created directory '/home/nina/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/nina/.ssh/id_ed25519
Your public key has been saved in /home/nina/.ssh/id_ed25519.pub
The key fingerprint is:
SHA256:ojIZtYMtQWXyDHYcNQD72aDaS3PBqPFTh9gEs29wIwM caijingnina@gmail.com
The key's randomart image is:
+--[ED25519 256]--+
|E O+*+o          |
| + %.  .         |
|  B O            |
|   ^ B           |
|. B # + S        |
| * * = .         |
|o X o            |
| . B             |
|  .              |
+----[SHA256]-----+
nina@ninapi:~ $ cat ¬/.ssh/id_ed25519.pub
cat: ¬/.ssh/id_ed25519.pub: No such file or directory
nina@ninapi:~ $ cat /home/nina/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOfVMPGK0baKTbo4zPjbY+kj84fzp3lk8OsvpAAXg1fn caijingnina@gmail.com
nina@ninapi:~ $ git clone https://github.com/MichaelLee-ceo/fllab.git
Cloning into 'fllab'...
Username for 'https://github.com': 
Password for 'https://github.com': 
remote: Repository not found.
fatal: Authentication failed for 'https://github.com/MichaelLee-ceo/fllab.git/'
nina@ninapi:~ $ git clone git@github.com:MichaelLee-ceo/fllab.git
Cloning into 'fllab'...
The authenticity of host 'github.com (20.27.177.113)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
ERROR: Repository not found.
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.
nina@ninapi:~ $ git remote -v
fatal: not a git repository (or any of the parent directories): .git
nina@ninapi:~ $ git clone git@github.com:NinaNeon/fllab.git
Cloning into 'fllab'...
remote: Enumerating objects: 96, done.
remote: Counting objects: 100% (96/96), done.
remote: Compressing objects: 100% (72/72), done.
remote: Total 96 (delta 29), reused 90 (delta 23), pack-reused 0 (from 0)
Receiving objects: 100% (96/96), 113.82 KiB | 658.00 KiB/s, done.
Resolving deltas: 100% (29/29), done.
nina@ninapi:~ $ chmod +x ./install_docker.sh 
chmod: cannot access './install_docker.sh': No such file or directory
nina@ninapi:~ $ cd fllab
nina@ninapi:~/fllab $ chmod +x ./install_docker.sh 
nina@ninapi:~/fllab $ ./install_docker.sh
🚀 Updating system...
Hit:1 http://deb.debian.org/debian bookworm InRelease                          
Hit:2 http://deb.debian.org/debian-security bookworm-security InRelease        
Hit:3 http://deb.debian.org/debian bookworm-updates InRelease   
Get:4 http://archive.raspberrypi.com/debian bookworm InRelease [55.0 kB]
Get:5 http://archive.raspberrypi.com/debian bookworm/main arm64 Packages [538 kB]
Get:6 http://archive.raspberrypi.com/debian bookworm/main armhf Packages [539 kB]
Fetched 1,132 kB in 9s (132 kB/s) 
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
106 packages can be upgraded. Run 'apt list --upgradable' to see them.
🐳 Installing Docker...
# Executing docker install script, commit: 53a22f61c0628e58e1d6680b49e82993d304b449
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install ca-certificates curl >/dev/null
+ sh -c install -m 0755 -d /etc/apt/keyrings
+ sh -c curl -fsSL "https://download.docker.com/linux/debian/gpg" -o /etc/apt/keyrings/docker.asc
+ sh -c chmod a+r /etc/apt/keyrings/docker.asc
+ sh -c echo "deb [arch=arm64 signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian bookworm stable" > /etc/apt/sources.list.d/docker.list
+ sh -c apt-get -qq update >/dev/null
+ sh -c DEBIAN_FRONTEND=noninteractive apt-get -y -qq install docker-ce docker-ce-cli containerd.io docker-compose-plugin docker-ce-rootless-extras docker-buildx-plugin >/dev/null
+ sh -c docker version
Client: Docker Engine - Community
 Version:           28.2.2
 API version:       1.50
 Go version:        go1.24.3
 Git commit:        e6534b4
 Built:             Fri May 30 12:07:27 2025
 OS/Arch:           linux/arm64
 Context:           default

Server: Docker Engine - Community
 Engine:
  Version:          28.2.2
  API version:      1.50 (minimum version 1.24)
  Go version:       go1.24.3
  Git commit:       45873be
  Built:            Fri May 30 12:07:27 2025
  OS/Arch:          linux/arm64
  Experimental:     false
 containerd:
  Version:          1.7.27
  GitCommit:        05044ec0a9a75232cad458027ca83437aae3f4da
 runc:
  Version:          1.2.5
  GitCommit:        v1.2.5-0-g59923ef
 docker-init:
  Version:          0.19.0
  GitCommit:        de40ad0

================================================================================

To run Docker as a non-privileged user, consider setting up the
Docker daemon in rootless mode for your user:

    dockerd-rootless-setuptool.sh install

Visit https://docs.docker.com/go/rootless/ to learn about rootless mode.


To run the Docker daemon as a fully privileged service, but granting non-root
users access, refer to https://docs.docker.com/go/daemon-access/

WARNING: Access to the remote API on a privileged Docker daemon is equivalent
         to root access on the host. Refer to the 'Docker daemon attack surface'
         documentation for details: https://docs.docker.com/go/attack-surface/

================================================================================

👤 Adding user to docker group...
🧩 Installing Docker Compose plugin...
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
docker-compose-plugin is already the newest version (2.36.2-1~debian.12~bookworm).
0 upgraded, 0 newly installed, 0 to remove and 106 not upgraded.
✅ Verifying installation...
Docker version 28.2.2, build e6534b4
Docker Compose version v2.36.2
🎉 Done! Please logout and log back in or run: newgrp docker
nina@ninapi:~/fllab $ newgrp docker
nina@ninapi:~/fllab $ docker --version
Docker version 28.2.2, build e6534b4
nina@ninapi:~/fllab $ docker images
REPOSITORY   TAG       IMAGE ID   CREATED   SIZE
nina@ninapi:~/fllab $ docker ps
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
nina@ninapi:~/fllab $ make build
docker build -f Dockerfile -t fl .
[+] Building 450.3s (13/13) FINISHED                             docker:default
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 514B                                       0.0s
 => [internal] load metadata for docker.io/arm64v8/python:3.10-slim        4.1s
 => [internal] load .dockerignore                                          0.1s
 => => transferring context: 2B                                            0.0s
 => [1/8] FROM docker.io/arm64v8/python:3.10-slim@sha256:38a704244a4d64f  25.4s
 => => resolve docker.io/arm64v8/python:3.10-slim@sha256:38a704244a4d64f3  0.1s
 => => sha256:38a704244a4d64f3b3cd5b7a13032df09e283f8c011 1.68kB / 1.68kB  0.0s
 => => sha256:1997942f7885d52ce70f388f91f894b53e517aed4c0 1.75kB / 1.75kB  0.0s
 => => sha256:2aaea8d72e5197479cd13cfd1970f972e407cf51c69 5.39kB / 5.39kB  0.0s
 => => sha256:b16f1b16678093d11ecfece1004207a40f9bc1b7 28.07MB / 28.07MB  23.3s
 => => sha256:7840cd825272881c40e91120a55b4d26f7e5829aa53 3.33MB / 3.33MB  2.1s
 => => sha256:33253a649f6a2e427162291b01ea5697cbf4c334 15.58MB / 15.58MB  17.1s
 => => sha256:f75bd2352d8f1aa2499f23554f0a8c45f78efca1004601d 249B / 249B  4.0s
 => => extracting sha256:b16f1b16678093d11ecfece1004207a40f9bc1b7d9d1d16a  0.8s
 => => extracting sha256:7840cd825272881c40e91120a55b4d26f7e5829aa530409b  0.1s
 => => extracting sha256:33253a649f6a2e427162291b01ea5697cbf4c334322f1250  0.4s
 => => extracting sha256:f75bd2352d8f1aa2499f23554f0a8c45f78efca1004601df  0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 210B                                          0.0s
 => [2/8] RUN apt-get update && apt-get install -y     build-essential l  99.4s
 => [3/8] WORKDIR /app                                                     0.1s 
 => [4/8] RUN pip install --upgrade pip                                    7.1s
 => [5/8] RUN pip install torch==2.2.2 torchvision torchaudio --index-u  135.0s
 => [6/8] RUN git config --global --add safe.directory /app                0.4s
 => [7/8] COPY requirements.txt .                                          0.1s
 => [8/8] RUN pip install --no-cache-dir -r requirements.txt             173.4s
 => exporting to image                                                     4.8s
 => => exporting layers                                                    4.8s
 => => writing image sha256:5155dd35b11c6af84331213e73e2b671992fe7215300f  0.0s
 => => naming to docker.io/library/fl                                      0.0s
nina@ninapi:~/fllab $ make run
docker run -it --rm \
	--network host \
	-v /home/nina/fllab:/app \
	-w /app \
	fl /bin/bash
root@ninapi:/app# python3 main.py
TensorFlow installation not found - running with reduced feature set.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.19.0 at http://localhost:6006/ (Press CTRL+C to quit)
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://60345a1908d1b4369f.gradio.live

This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)
Using device: `cpu`, seed: `42`
-- Save figure: ./distributions/bubble_plot/label/label_100_42.png
[*] Using `label` skewness
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 404: Not Found

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-images-idx3-ubyte.gz to ./data/digit/MNIST/raw/train-images-idx3-ubyte.gz
100%|█████████████████████████| 9912422/9912422 [00:07<00:00, 1295221.30steps/s]
Extracting ./data/digit/MNIST/raw/train-images-idx3-ubyte.gz to ./data/digit/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 404: Not Found

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/train-labels-idx1-ubyte.gz to ./data/digit/MNIST/raw/train-labels-idx1-ubyte.gz
100%|██████████████████████████████| 28881/28881 [00:00<00:00, 120155.47steps/s]
Extracting ./data/digit/MNIST/raw/train-labels-idx1-ubyte.gz to ./data/digit/MNIST/raw

Downloading http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
Failed to download (trying next):
HTTP Error 404: Not Found

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-images-idx3-ubyte.gz to ./data/digit/MNIST/raw/t10k-images-idx3-ubyte.gz
100%|██████████████████████████| 1648877/1648877 [00:02<00:00, 766769.76steps/s]
Extracting ./data/digit/MNIST/raw/t10k-images-idx3-ubyte.gz to ./data/digit/MNIST/raw


[Client 8] loss: 0.0131, acc: 0.9973
[Client 9] loss: 0.0149, acc: 0.9979
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.1168, test_acc_all: 0.9633
[Server] Total_loss_all: 0.1168, Total_acc_all: 0.9633
Total time: 2975.6493s

----------- Training complete! 🎉 -----------
^CKeyboard interruption in main thread... closing server.
Killing tunnel 127.0.0.1:7860 <> https://766b62793672d31d41.gradio.live
root@ninapi:/app# git checkout comm
error: pathspec 'comm' did not match any file(s) known to git
root@ninapi:/app# git branch -a
* main
  remotes/origin/HEAD -> origin/main
  remotes/origin/main
root@ninapi:/app# 






Downloading http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
Failed to download (trying next):
HTTP Error 404: Not Found

Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz
Downloading https://ossci-datasets.s3.amazonaws.com/mnist/t10k-labels-idx1-ubyte.gz to ./data/digit/MNIST/raw/t10k-labels-idx1-ubyte.gz
100%|███████████████████████████████| 4542/4542 [00:00<00:00, 1197092.42steps/s]
Extracting ./data/digit/MNIST/raw/t10k-labels-idx1-ubyte.gz to ./data/digit/MNIST/raw

Loading MNIST to memory: 100%|███████| 60000/60000 [00:34<00:00, 1748.32steps/s]
Loading MNIST to memory: 100%|███████| 10000/10000 [00:05<00:00, 1908.89steps/s]

----------------------- Dataset statistics: -----------------------
           0     1     2     3     4     5     6     7     8     9
MNIST  5923  6742  5958  6131  5842  5421  5918  6265  5851  5949

----------------------- Testset statistics: -----------------------
          0     1     2     3    4    5    6     7    8     9
MNIST  980  1135  1032  1010  982  892  958  1028  974  1009

---------------------------------------- [MNIST] partition: ----------------------------------------
          label_0  label_1  label_2  ...  label_7  label_8  label_9
client_0     1153     1396     1121  ...     1257     1238     1385
client_1     1416     1170     1294  ...     1259     1148     1059
client_2     1070     1402     1239  ...     1180     1188     1010
client_3     1043     1466     1095  ...     1332     1135     1315
client_4     1238     1305     1206  ...     1234     1139     1177

[5 rows x 10 columns]

######### Client datasets #########
          MNIST
client_0  12270
client_1  11748
client_2  11637
client_3  12004
client_4  12313
###################################

Optimized parameters: {} 

[+] Add client, cid:0
[+] Add client, cid:1
[+] Add client, cid:2
[+] Add client, cid:3
[+] Add client, cid:4

[Server] `FedAvg` initialization done

----------- Round 1/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0482, acc: 0.9839
[Client 1] loss: 0.0489, acc: 0.9856
[Client 2] loss: 0.0445, acc: 0.9880
[Client 3] loss: 0.0529, acc: 0.9844
[Client 4] loss: 0.0475, acc: 0.9850
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0518, test_acc_all: 0.9833
[Server] Total_loss_all: 0.0518, Total_acc_all: 0.9833

----------- Round 2/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0206, acc: 0.9946
[Client 1] loss: 0.0255, acc: 0.9930
[Client 2] loss: 0.0210, acc: 0.9945
[Client 3] loss: 0.0246, acc: 0.9930
[Client 4] loss: 0.0231, acc: 0.9939
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0362, test_acc_all: 0.9877
[Server] Total_loss_all: 0.0362, Total_acc_all: 0.9877

----------- Round 3/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0118, acc: 0.9971
[Client 1] loss: 0.0153, acc: 0.9958
[Client 2] loss: 0.0129, acc: 0.9971
[Client 3] loss: 0.0160, acc: 0.9958
[Client 4] loss: 0.0157, acc: 0.9957
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0329, test_acc_all: 0.9892
[Server] Total_loss_all: 0.0329, Total_acc_all: 0.9892

----------- Round 4/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0093, acc: 0.9977
[Client 1] loss: 0.0097, acc: 0.9976
[Client 2] loss: 0.0090, acc: 0.9974
[Client 3] loss: 0.0095, acc: 0.9976
[Client 4] loss: 0.0128, acc: 0.9967
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0301, test_acc_all: 0.9901
[Server] Total_loss_all: 0.0301, Total_acc_all: 0.9901

----------- Round 5/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0063, acc: 0.9988
[Client 1] loss: 0.0053, acc: 0.9989
[Client 2] loss: 0.0054, acc: 0.9990
[Client 3] loss: 0.0066, acc: 0.9985
[Client 4] loss: 0.0080, acc: 0.9985
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0304, test_acc_all: 0.9908
[Server] Total_loss_all: 0.0304, Total_acc_all: 0.9908

----------- Round 6/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0037, acc: 0.9995
[Client 1] loss: 0.0036, acc: 0.9995
[Client 2] loss: 0.0043, acc: 0.9995
[Client 3] loss: 0.0025, acc: 0.9999
[Client 4] loss: 0.0069, acc: 0.9983
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0288, test_acc_all: 0.9916
[Server] Total_loss_all: 0.0288, Total_acc_all: 0.9916

----------- Round 7/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0031, acc: 0.9997
[Client 1] loss: 0.0019, acc: 1.0000
[Client 2] loss: 0.0025, acc: 0.9999
[Client 3] loss: 0.0049, acc: 0.9991
[Client 4] loss: 0.0043, acc: 0.9993
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0295, test_acc_all: 0.9912
[Server] Total_loss_all: 0.0295, Total_acc_all: 0.9912

----------- Round 8/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0023, acc: 0.9999
[Client 1] loss: 0.0018, acc: 0.9999
[Client 2] loss: 0.0022, acc: 0.9997
[Client 3] loss: 0.0022, acc: 0.9998
[Client 4] loss: 0.0049, acc: 0.9992
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0290, test_acc_all: 0.9914
[Server] Total_loss_all: 0.0290, Total_acc_all: 0.9914

----------- Round 9/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0016, acc: 0.9998
[Client 1] loss: 0.0016, acc: 0.9998
[Client 2] loss: 0.0015, acc: 0.9999
[Client 3] loss: 0.0019, acc: 0.9999
[Client 4] loss: 0.0023, acc: 0.9999
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0295, test_acc_all: 0.9914
[Server] Total_loss_all: 0.0295, Total_acc_all: 0.9914

----------- Round 10/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0014, acc: 0.9999
[Client 1] loss: 0.0009, acc: 1.0000
[Client 2] loss: 0.0013, acc: 0.9998
[Client 3] loss: 0.0018, acc: 1.0000
[Client 4] loss: 0.0015, acc: 0.9999
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.0302, test_acc_all: 0.9915
[Server] Total_loss_all: 0.0302, Total_acc_all: 0.9915
Total time: 5791.7208s

----------- Training complete! 🎉 -----------
Using device: `cpu`, seed: `42`
-- Save figure: ./distributions/bubble_plot/label/label_0.1_42.png
[*] Using `label` skewness
Loading MNIST to memory: 100%|███████| 60000/60000 [00:34<00:00, 1748.75steps/s]
Loading MNIST to memory: 100%|███████| 10000/10000 [00:05<00:00, 1829.75steps/s]

----------------------- Dataset statistics: -----------------------
           0     1     2     3     4     5     6     7     8     9
MNIST  5923  6742  5958  6131  5842  5421  5918  6265  5851  5949

----------------------- Testset statistics: -----------------------
          0     1     2     3    4    5    6     7    8     9
MNIST  980  1135  1032  1010  982  892  958  1028  974  1009

---------------------------------------- [MNIST] partition: ----------------------------------------
          label_0  label_1  label_2  ...  label_7  label_8  label_9
client_0      315        2      680  ...     2836       12     2762
client_1        0        0        2  ...        0        2        0
client_2        0     6500     5275  ...        0        0     3184
client_3        7      128        0  ...        0     5835        1
client_4     5600      110        0  ...     3428        0        1

[5 rows x 10 columns]

######### Client datasets #########
          MNIST
client_0  12743
client_1   2179
client_2  15175
client_3  11584
client_4  18305
###################################

Optimized parameters: {} 

[+] Add client, cid:0
[+] Add client, cid:1
[+] Add client, cid:2
[+] Add client, cid:3
[+] Add client, cid:4

[Server] `FedAvg` initialization done

----------- Round 1/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0396, acc: 0.9878
[Client 1] loss: 0.0337, acc: 0.9916
[Client 2] loss: 0.0166, acc: 0.9951
[Client 3] loss: 0.0157, acc: 0.9949
[Client 4] loss: 0.0206, acc: 0.9934
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 1.2493, test_acc_all: 0.5836
[Server] Total_loss_all: 1.2493, Total_acc_all: 0.5836

----------- Round 2/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0261, acc: 0.9922
[Client 1] loss: 0.0122, acc: 0.9972
[Client 2] loss: 0.0084, acc: 0.9977
[Client 3] loss: 0.0084, acc: 0.9978
[Client 4] loss: 0.0107, acc: 0.9971
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.3516, test_acc_all: 0.8985
[Server] Total_loss_all: 0.3516, Total_acc_all: 0.8985

----------- Round 3/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0195, acc: 0.9948
[Client 1] loss: 0.0033, acc: 0.9989
[Client 2] loss: 0.0036, acc: 0.9992
[Client 3] loss: 0.0045, acc: 0.9990
[Client 4] loss: 0.0061, acc: 0.9987
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.2328, test_acc_all: 0.9225
[Server] Total_loss_all: 0.2328, Total_acc_all: 0.9225

----------- Round 4/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0133, acc: 0.9966
[Client 1] loss: 0.0009, acc: 1.0000
[Client 2] loss: 0.0031, acc: 0.9995
[Client 3] loss: 0.0037, acc: 0.9991
[Client 4] loss: 0.0044, acc: 0.9990
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.1387, test_acc_all: 0.9531
[Server] Total_loss_all: 0.1387, Total_acc_all: 0.9531

----------- Round 5/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0096, acc: 0.9978
[Client 1] loss: 0.0005, acc: 1.0000
[Client 2] loss: 0.0029, acc: 0.9990
[Client 3] loss: 0.0017, acc: 0.9999
[Client 4] loss: 0.0045, acc: 0.9986
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.1057, test_acc_all: 0.9636
[Server] Total_loss_all: 0.1057, Total_acc_all: 0.9636

----------- Round 6/10 -----------
[+] set active: [0 1 2 3 4]
[-] set inactive: []
-----------------------------
Client | 0 | 1 | 2 | 3 | 4 |
-----------------------------
Status | O | O | O | O | O |
-----------------------------

[Server] Start training client
[Client 0] loss: 0.0074, acc: 0.9981
[Client 1] loss: 0.0003, acc: 1.0000
[Client 2] loss: 0.0018, acc: 0.9995
[Client 3] loss: 0.0014, acc: 0.9998
^CKeyboard interruption in main thread... closing server.
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1133, in _try_get_data
    data = self._data_queue.get(timeout=timeout)
  File "/usr/local/lib/python3.10/multiprocessing/queues.py", line 122, in get
    return _ForkingPickler.loads(res)
  File "/usr/local/lib/python3.10/site-packages/torch/multiprocessing/reductions.py", line 495, in rebuild_storage_fd
    fd = df.detach()
  File "/usr/local/lib/python3.10/multiprocessing/resource_sharer.py", line 57, in detach
    with _resource_sharer.get_connection(self._id) as conn:
  File "/usr/local/lib/python3.10/multiprocessing/resource_sharer.py", line 86, in get_connection
    c = Client(address, authkey=process.current_process().authkey)
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 502, in Client
    c = SocketClient(address)
  File "/usr/local/lib/python3.10/multiprocessing/connection.py", line 630, in SocketClient
    s.connect(address)
FileNotFoundError: [Errno 2] No such file or directory

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/site-packages/gradio/queueing.py", line 625, in process_events
    response = await route_utils.call_process_api(
  File "/usr/local/lib/python3.10/site-packages/gradio/route_utils.py", line 322, in call_process_api
    output = await app.get_blocks().process_api(
  File "/usr/local/lib/python3.10/site-packages/gradio/blocks.py", line 2220, in process_api
    result = await self.call_function(
  File "/usr/local/lib/python3.10/site-packages/gradio/blocks.py", line 1731, in call_function
    prediction = await anyio.to_thread.run_sync(  # type: ignore
  File "/usr/local/lib/python3.10/site-packages/anyio/to_thread.py", line 56, in run_sync
    return await get_async_backend().run_sync_in_worker_thread(
  File "/usr/local/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 2470, in run_sync_in_worker_thread
    return await future
  File "/usr/local/lib/python3.10/site-packages/anyio/_backends/_asyncio.py", line 967, in run
    result = context.run(func, *args)
  File "/usr/local/lib/python3.10/site-packages/gradio/utils.py", line 894, in wrapper
    response = f(*args, **kwargs)
  File "/app/gradio_ui.py", line 96, in gradio_interface
    main_function(args)
  File "/app/main.py", line 172, in main
    server.train_clients(rounds=i)
  File "/app/server.py", line 158, in train_clients
    self.strategy._server_train_func(cid=i, rounds=rounds, client_list=self.client_list, global_model=self.model, global_info=self.global_info)
  File "/app/strategies/fedavg.py", line 21, in _server_train_func
    result = client_list[cid].train()
  File "/app/client.py", line 137, in train
    result = self.strategy._train(self.model, self.trainLoader, self.optimizer, self.args.num_epochs, **kwargs)
  File "/app/strategies/fedavg.py", line 37, in _train
    for x, label in trainLoader:
  File "/usr/local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 631, in __next__
    data = self._next_data()
  File "/usr/local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1329, in _next_data
    idx, data = self._get_data()
  File "/usr/local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1295, in _get_data
    success, data = self._try_get_data()
  File "/usr/local/lib/python3.10/site-packages/torch/utils/data/dataloader.py", line 1146, in _try_get_data
    raise RuntimeError(f'DataLoader worker (pid(s) {pids_str}) exited unexpectedly') from e
RuntimeError: DataLoader worker (pid(s) 4218, 4220) exited unexpectedly
Killing tunnel 127.0.0.1:7860 <> https://60345a1908d1b4369f.gradio.live
root@ninapi:/app# python3 main.py
TensorFlow installation not found - running with reduced feature set.
Serving TensorBoard on localhost; to expose to the network, use a proxy or pass --bind_all
TensorBoard 2.19.0 at http://localhost:6006/ (Press CTRL+C to quit)
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://766b62793672d31d41.gradio.live

This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)
Using device: `cpu`, seed: `42`
-- Save figure: ./distributions/bubble_plot/label/label_0.1_42.png
[*] Using `label` skewness
Loading MNIST to memory: 100%|███████| 60000/60000 [00:34<00:00, 1718.48steps/s]
Loading MNIST to memory: 100%|███████| 10000/10000 [00:05<00:00, 1878.81steps/s]

----------------------- Dataset statistics: -----------------------
           0     1     2     3     4     5     6     7     8     9
MNIST  5923  6742  5958  6131  5842  5421  5918  6265  5851  5949

----------------------- Testset statistics: -----------------------
          0     1     2     3    4    5    6     7    8     9
MNIST  980  1135  1032  1010  982  892  958  1028  974  1009

---------------------------------------- [MNIST] partition: ----------------------------------------
          label_0  label_1  label_2  ...  label_7  label_8  label_9
client_0      187        5     2438  ...     4358       36      437
client_1        0        0      410  ...        0     2261        0
client_2        0       39        5  ...      199        0        0
client_3        4        0        0  ...       19       72        0
client_4     3339        0        0  ...        0        0        0
client_5        0     1253        0  ...      122     2149      899
client_6        0     1428        0  ...      116        0     2219
client_7     2305       16        0  ...        0        0        4
client_8       45      413        0  ...     1441     1328        0
client_9       39     3585     3102  ...        5        1     2387

[10 rows x 10 columns]

######### Client datasets #########
          MNIST
client_0   7463
client_1   2702
client_2    438
client_3   6602
client_4   4676
client_5   6631
client_6   9209
client_7   4865
client_8   7895
client_9   9483
###################################

Optimized parameters: {'mu': 0.01} 

[+] Add client, cid:0
[+] Add client, cid:1
[+] Add client, cid:2
[+] Add client, cid:3
[+] Add client, cid:4
[+] Add client, cid:5
[+] Add client, cid:6
[+] Add client, cid:7
[+] Add client, cid:8
[+] Add client, cid:9

[Server] `FedProx` initialization done

----------- Round 1/5 -----------
[+] set active: [0 1 2 3 4 5 6 7 8 9]
[-] set inactive: []
-------------------------------------------------
Client | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
-------------------------------------------------
Status | O | O | O | O | O | O | O | O | O | O |
-------------------------------------------------

[Server] Start training client
[Client 0] loss: 0.0624, acc: 0.9885
[Client 1] loss: 0.0896, acc: 0.9816
[Client 2] loss: 0.3322, acc: 0.8851
[Client 3] loss: 0.0456, acc: 0.9909
[Client 4] loss: 0.0429, acc: 0.9932
[Client 5] loss: 0.0595, acc: 0.9890
[Client 6] loss: 0.0321, acc: 0.9962
[Client 7] loss: 0.0415, acc: 0.9950
[Client 8] loss: 0.0521, acc: 0.9888
[Client 9] loss: 0.0519, acc: 0.9919
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 1.2349, test_acc_all: 0.6995
[Server] Total_loss_all: 1.2349, Total_acc_all: 0.6995

----------- Round 2/5 -----------
[+] set active: [0 1 2 3 4 5 6 7 8 9]
[-] set inactive: []
-------------------------------------------------
Client | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
-------------------------------------------------
Status | O | O | O | O | O | O | O | O | O | O |
-------------------------------------------------

[Server] Start training client
[Client 0] loss: 0.0353, acc: 0.9934
[Client 1] loss: 0.0448, acc: 0.9903
[Client 2] loss: 0.1250, acc: 0.9688
[Client 3] loss: 0.0230, acc: 0.9978
[Client 4] loss: 0.0262, acc: 0.9971
[Client 5] loss: 0.0367, acc: 0.9946
[Client 6] loss: 0.0173, acc: 0.9984
[Client 7] loss: 0.0293, acc: 0.9962
[Client 8] loss: 0.0239, acc: 0.9981
[Client 9] loss: 0.0308, acc: 0.9952
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.4887, test_acc_all: 0.8705
[Server] Total_loss_all: 0.4887, Total_acc_all: 0.8705

----------- Round 3/5 -----------
[+] set active: [0 1 2 3 4 5 6 7 8 9]
[-] set inactive: []
-------------------------------------------------
Client | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
-------------------------------------------------
Status | O | O | O | O | O | O | O | O | O | O |
-------------------------------------------------

[Server] Start training client
[Client 0] loss: 0.0263, acc: 0.9955
[Client 1] loss: 0.0326, acc: 0.9939
[Client 2] loss: 0.0581, acc: 0.9791
[Client 3] loss: 0.0158, acc: 0.9985
[Client 4] loss: 0.0199, acc: 0.9971
[Client 5] loss: 0.0304, acc: 0.9944
[Client 6] loss: 0.0112, acc: 0.9987
[Client 7] loss: 0.0130, acc: 0.9982
[Client 8] loss: 0.0151, acc: 0.9986
[Client 9] loss: 0.0238, acc: 0.9969
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.2707, test_acc_all: 0.9148
[Server] Total_loss_all: 0.2707, Total_acc_all: 0.9148

----------- Round 4/5 -----------
[+] set active: [0 1 2 3 4 5 6 7 8 9]
[-] set inactive: []
-------------------------------------------------
Client | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
-------------------------------------------------
Status | O | O | O | O | O | O | O | O | O | O |
-------------------------------------------------

[Server] Start training client
[Client 0] loss: 0.0167, acc: 0.9981
[Client 1] loss: 0.0228, acc: 0.9968
[Client 2] loss: 0.0330, acc: 0.9904
[Client 3] loss: 0.0121, acc: 0.9993
[Client 4] loss: 0.0166, acc: 0.9979
[Client 5] loss: 0.0223, acc: 0.9961
[Client 6] loss: 0.0074, acc: 0.9999
[Client 7] loss: 0.0167, acc: 0.9980
[Client 8] loss: 0.0146, acc: 0.9989
[Client 9] loss: 0.0193, acc: 0.9966
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.1696, test_acc_all: 0.9480
[Server] Total_loss_all: 0.1696, Total_acc_all: 0.9480

----------- Round 5/5 -----------
[+] set active: [0 1 2 3 4 5 6 7 8 9]
[-] set inactive: []
-------------------------------------------------
Client | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
-------------------------------------------------
Status | O | O | O | O | O | O | O | O | O | O |
-------------------------------------------------

[Server] Start training client
[Client 0] loss: 0.0159, acc: 0.9975
[Client 1] loss: 0.0153, acc: 0.9972
[Client 2] loss: 0.0102, acc: 1.0000
[Client 3] loss: 0.0092, acc: 0.9998
[Client 4] loss: 0.0129, acc: 0.9987
[Client 5] loss: 0.0164, acc: 0.9976
[Client 6] loss: 0.0063, acc: 0.9999
[Client 7] loss: 0.0089, acc: 0.9982
[Client 8] loss: 0.0131, acc: 0.9973
[Client 9] loss: 0.0149, acc: 0.9979
[Server] Done aggregating client models
===== Evaluate each domain
[Server, MNIST] test_loss_all: 0.1168, test_acc_all: 0.9633
[Server] Total_loss_all: 0.1168, Total_acc_all: 0.9633
Total time: 2975.6493s

----------- Training complete! 🎉 -----------
