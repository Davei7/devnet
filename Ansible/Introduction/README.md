![💻_Cisco_DEVNET_Associate_Guide](https://user-images.githubusercontent.com/49377281/161389787-3b43e062-e3e6-4095-b03c-6044477e731f.png)

* * *

## Configure Remote Devices

After installing Ansible, there is a requirement to configure the remote servers. Start by collecting the IP Addresses of your servers. In the machine where Ansible was installed, edit the file /etc/hosts with the command ```vim /etc/hosts```.

Inside the file /etc/hosts, add the line at the beginning with the IP Address and name of the host collected, for example, ```192.168.1.20 hostn1```. This file stores the entries for a local DNS that the machine uses.

Every time the user refers to another host by its name through a ping or ssh command or through any of the applications or tools within this system, it looks into the ```hosts``` file to find out the IP address of that host.

Test the connectivity by using ping with the command ```ping hostn1```.

The next step is to create an SSH key on the Ansible server. To accomplish this, use the command ```ssh-keygen```. Press enter in all answers to the defaults questions. If you want to verify the list of keys, use the command ```ls .ssh```.

To check if the SSH service is running in our hostn1, on a terminal of hostn1, do the command ```service ssh status```. If the service is inactive, to start the SSH service, use the command ```service ssh start```.

The user needs to create a user in our remote machine. The username of this new user should be the same as the one in our Ansible machine to match everything with the SSH sessions. Follow the steps specified [here](https://humanwhocodes.com/snippets/2021/03/create-user-linux-ssh-key/).

If the command ```ssh``` is not recognized in the hostn1, you first need to install the SSH service. To install the SSH service, use the command (Ubuntu OS) ```apt-get install openssh-server```. 

In the Ansible machine, after completing the previous steps, use the command ``` ssh-copy-id -i .ssh/id_rsa.pub <user_created_hostn1>```. In the field ```<user_created_hostn1>```, substitute this with the user created in the hostn1.

Ansible should execute commands with privileges without being prompted for a password.

In the Ansible machine, use the command ```sudo visudo```. At the end of the file, add the following line ```<machine-ansible-username> ALL=(ALL) NOPASSWD: ALL```. In the field ```<machine-ansible-username>```, substitute this with the user on the Ansible machine.

To test if it is working, do any command such ```sudo visudo``` again, and check if it prompts a password. If nothing prompts, this means that it is working!

In the hosts, you need to do the same procedure seen above. However, in the hosts, instead of using the ```<machine-ansible-username>```, use the ```<user_created_hostn1> as seen before```.

* * *

## Inventory File

![transferir](https://user-images.githubusercontent.com/49377281/161392185-fc44009c-f0d2-49d7-bb3f-8efb01fb36d3.jpg)
