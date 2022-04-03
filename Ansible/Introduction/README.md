![💻_Cisco_DEVNET_Associate_Guide](https://user-images.githubusercontent.com/49377281/161389787-3b43e062-e3e6-4095-b03c-6044477e731f.png)

* * *

## Configure Remote Devices

After installing Ansible, there is a requirement to configure the remote servers. Start by collecting the IP Addresses of your servers. In the machine where Ansible was installed, edit the file /etc/hosts with the command ```vim /etc/hosts```.

Inside the file /etc/hosts, add the line at the beginning with the IP Address and name of the host collected, for example, ```192.168.1.20 hostn1```. This file stores the entries for a local DNS that the machine uses.

Every time the user refers to another host by its name through a ping or ssh command or through any of the applications or tools within this system, it looks into the ```hosts``` file to find out the IP address of that host.

Test the connectivity by using ping with the command ```ping hostn1```.
