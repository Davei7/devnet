![💻_Cisco_DEVNET_Associate_Guide](https://user-images.githubusercontent.com/49377281/161389787-3b43e062-e3e6-4095-b03c-6044477e731f.png)

* * *

## Theory Overview

Application Centric Infrastructure (ACI) is the Cisco solution to simplify the Datacenter. ACI gives us a single login to manage the network, and it is aware of the applications in its network. ACI configures itself based on the desired state that the user configures to treat the applications.

ACI is aware because the user doesn't need to know the code that runs inside each application. The user will only configure the Datacenter based on policies around the network, which is called Application-Centric Policy.

Application-Centric Policy is one of three pillars of ACI. Another pillar of ACI is the IS-IS (Intermediate-System Intermediate-System), which is called the underlay protocol and to complete, there is also VXLAN (Virtual Extensible LAN), which is the overlay protocol.

However, how does the ACI configures itself? The last pillar of it is the APIC Controller. The Application Policy Infrastructure Controller (APIC) provides the automation for all the Datacenter.

The APIC controllers are neither part of the data plane nor the control plane. APIC controllers are part of the Management plane. When you log in to an ACI, you will log in to one of these APIC controllers because those provide the frontend GUI.

* * *

## ACI SDK Toolkit

SDK stands for Software Development Kit. SDK is a set of software tools operated to create applications for specific platforms. In our case, this SDK is for the ACI.

To know more about the ACI toolkit, begin by checking the [ACI Toolkit Documentation URL](https://acitoolkit.readthedocs.io/en/latest/). This URL opens the official documentation for the ACI Toolkit.

After reading the documentation and becoming familiar with all the parameters and methods, it is recommended to go to the [ACI Toolkit code](https://github.com/datacenter/acitoolkit). This URL is where Cisco posted the ACI Toolkit code.
