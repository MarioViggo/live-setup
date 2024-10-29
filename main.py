import os

def clone_repos():
    print("[Cloning repos...]")
    os.system("git clone https://github.com/Barionix/Trovilo")
    os.system("git clone https://github.com/Barionix/gogram")
    os.system("git clone https://github.com/Barionix/live-setup")
    os.system("git clone https://github.com/Barionix/WildNetwork")
    os.system("git config --global user.email \"mariojuniorsoaresdev@gmail.com\"")

def set_folders():
    print("[Setting folders...]")
    os.mkdir("Office")
    os.mkdir("Office/Projects") 
    os.chdir("Office/Projects")
    clone_repos()

def set_up_compose():
    print("[Installing compose...]")
    os.system("sudo curl -L \"https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)\" -o /usr/local/bin/docker-compose")
    os.system("sudo chmod +x /usr/local/bin/docker-compose")

def set_up_docker():
    print("[Installing docker...")
    os.system("sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release")
    os.system("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
    os.system("echo \
  \"deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable\" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null")
    os.system("sudo apt-get update -y && sudo apt-get install -y docker-ce docker-ce-cli containerd.io")
    os.system("echo '{ \"storage-driver\": \"devicemapper\" }' | sudo tee -a /etc/docker/daemon.json > /dev/null")

def install_dev_tools():
    print("[Installing git...]")
    os.system("sudo apt-get install -y git")
    print("[Installing Go...]")
    os.system("sudo snap install --classic go")
    print("[Installing VSCode...]")
    os.system("sudo snap install --classic code")  
    print("[Installing Insomnia...]")
    os.system("sudo snap install --classic insomnia")    

def start():
    install_dev_tools()
    set_folders()
start()
