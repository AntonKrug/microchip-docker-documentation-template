# Documentation template

This is empty barebone example project how to make sphinx based HTML documents with the *antonkrug/documentation-builders-ng* container

# Dependencies

Docker needs to be installed to run docker containers (skip if you have already working docker environment).

## Installation of Docker on Ubuntu


```
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common gnupg-utils 
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

version_name=$(lsb_release -cs)
sudo add-apt-repository  "deb [arch=amd64] https://download.docker.com/linux/ubuntu  ${version_name} stable"
sudo apt-get update
sudo apt-get -y install docker-ce

sudo groupadd docker
sudo gpasswd -a ${USER} docker
sudo service docker restart

systemctl restart docker

docker run hello-world
```

## Installation of Docker on Debian

If installing on a Debian OS, then just change each mention of ```ubuntu``` to ```debian``` in the script above

## Windows 10 WSL1 

If using Windows subsystem for Linux then follow the instruction on this webpage:

https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly

Pay attention on the volume sharing section and comment or uncomment the following line in the **build_html**:
```
current_dir=${current_dir#/mnt} # uncomment when using WSL1 with Docker on Windows 10
```
This is due differences how WSL1 mounts Windows volumes (/mnt/c/) compared to how Docker for Windows mounts Windwos volumes (/c/), passing to docker a path which was working in WSL1 will not work.

If set incorrectly then error message like this might be displayed:
```
bash: line 0: cd: /project/source/main: No such file or directory
```

# Build the documentation


Adjust the script depending if it's running on a native machine or in a Windows 10 WSL1 (see above)
Run:

```./build_html.sh```

Check **build** folder for built HTML.
