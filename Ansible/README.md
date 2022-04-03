![💻_Cisco_DEVNET_Associate_Guide](https://user-images.githubusercontent.com/49377281/161389787-3b43e062-e3e6-4095-b03c-6044477e731f.png)

* * *

## Ansible

Ansible is the network automation tool of choice because it is pre-built automation and orchestration capabilities for almost every platform. The vendors don't matter because Ansible comes out of the box with numerous Automation and Orchestration tasks.

Ansible is the network Automator and Orchestrator. Ansible is what deploys your infrastructure from the base code, and Ansible checks, verify and maintains the code is in its desired state.

Network configuration comes from source code. We can create new networks with the same template and separate environments from the source code.

* * *

## CI/CD

CI/CD stands for Continuous Integration and Continuous Delivery/Deployment, and it is a set of practices for automating the delivery of our IT services in the software that we create, into the hands of our users and the deployment of software, deployment of IT services should be easy and routine and available on demand.

Where does Ansible come in this process? You deploy network change for source code. The next step is running and confirming tests, which verify that the network is not impacted. If everything is correct, the code can move into production. There Ansible reads the code and sees a new desired state as arrived. It automatically checks the network for compliance with the new desired state and updates the devices as necessary.

* * *

## Install Ansible

The list of commands to install Ansible (Ubuntu) is the following:
1. ```sudo apt update```
2. ```sudo apt install software-properties-common```
3. ```$sudo apt-add-repository --yes ppa:ansible/ansible```
4. ```$sudo apt install ansible -y```

If you are using a different Operative System (OS), follow the documentation in this [URL](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).

To learn fundamentals regarding Ansible begin by checking the folder Introduction where you can learn the following:
* Configure Remote Devices;
* Inventory File;
* Modules;
* Variables and Facts;
* Conditionals;
* Loops.
