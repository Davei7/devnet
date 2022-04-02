![💻_Cisco_DEVNET_Associate_Guide](https://user-images.githubusercontent.com/49377281/161389787-3b43e062-e3e6-4095-b03c-6044477e731f.png)

* * *

## Theory Overview

Application Centric Infrastructure (ACI) is the Cisco solution to simplify the Datacenter. ACI gives us a single login to manage the network and it is aware of the applications in its network. ACI configures itself based on the desired state the user configures it to treat the applications.

ACI is aware because the user doesn't need to know the code inside the applications. The user will simply configure the Datacenter based on policies around the network. This is what is called Application-Centric Policy.

* * *

Construction

* * *

The Application Policy Infrastructure Controllers (APIC) is what provides the automation for all the Datacenter.

The APIC controllers are neither part of the data plane or the control plane. APIC controllers are part of the Management plane. When you log in to an ACI you will go log in into one of these APIC controllers because that is what provides the frontend GUI.

* * *

## ACI SDK Toolkit

SDK stands for Software Development Kit. It’s a set of software tools and programs used by developers to create applications for specific platforms. In our case the SDK is specific for the ACI.

Start for checking the ACI toolkit in the [ACI Toolkit Documentation URL](https://acitoolkit.readthedocs.io/en/latest/). This the official documentation for ACI Toolkit as well a lot of programmability for ACI.

After reading the documentation and became familiar with all the parameters and methods, it is recommended to go to [ACI Toolkit code](https://github.com/datacenter/acitoolkit). This URL is where Cisco posted the ACI Toolkit code.
