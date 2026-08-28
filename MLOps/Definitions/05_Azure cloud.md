<div align='center'>

# <img src="https://tse4.mm.bing.net/th/id/OIP.BMo2U7wms5PQ3NcZ5-hpiQAAAA?r=0&w=300&h=169&rs=1&pid=ImgDetMain&o=7&rm=3" alt="Logo" width="80" height="50"/> Azure Cloud

</div>

## 1. Regions🟦

An **Azure Region** is a set of data centers deployed within a specific geographic location (for example, East US, West Europe, or Southeast Asia).

### Key points:
- Each region is made up of one or more data centers that are connected through a dedicated regional low-latency network.
- Microsoft operates dozens of regions worldwide to help customers meet data residency, compliance, and performance requirements.
- When you create most Azure resources, you must choose a region. Choosing a region close to your users usually reduces latency.
- Some regions offer Availability Zones (physically separate locations within the same region) for higher resilience.
- Not every Azure service is available in every region.

**Why regions matter**: They determine where your data physically lives, affect performance, and influence pricing and compliance.

---

## 2. Resource Groups🟦

A **Resource Group** is a logical container that holds related Azure resources for a solution.

### Key points:
- Every resource you create in Azure (virtual machines, storage accounts, networks, databases, etc.) must belong to exactly one resource group.
- Resource groups help you organize, manage, and monitor resources as a single unit.
- You can apply tags, access control (RBAC), policies, and locks at the resource-group level.
- Deleting a resource group deletes all the resources it contains (be careful!).
- Resource groups themselves exist in a specific region, but the resources inside them can be located in different regions.

**Best practice**: Group resources that share the same lifecycle (for example, all resources for a single application or environment) into the same resource group.

---

## 3. Virtual Machines (VMs)🟦

An **Azure Virtual Machine** is an on-demand, scalable computing resource that provides the functionality of a physical computer in the cloud.

### Key points:
- You can run Windows or Linux operating systems.
- You choose the size (CPU, memory, storage, and network capacity) according to your needs.
- VMs are highly flexible: you can start, stop, resize, or delete them at any time.
- They support a wide range of workloads — from simple web servers to high-performance computing and databases.
- Azure offers several ways to create and manage VMs (Azure Portal, Azure CLI, PowerShell, ARM/Bicep templates, Terraform, etc.).
- You are responsible for the operating system, applications, and data (Infrastructure as a Service model).

**Common use cases**:
- Lift-and-shift of existing applications
- Development and testing environments
- Running custom software that cannot easily be containerized or moved to Platform-as-a-Service offerings

---

## 4. Storage Accounts🟦

An **Azure Storage Account** is a fundamental resource that provides a unique namespace for storing and accessing data in Azure.

### Key points:
- It acts as a container for different types of storage services:
  - **Blob Storage** – for unstructured data (files, images, videos, backups, logs).
  - **File Storage** – fully managed file shares accessible via SMB or NFS.
  - **Queue Storage** – for reliable messaging between application components.
  - **Table Storage** – a NoSQL key-value store for structured data.
  - **Disk Storage** – persistent disks used by virtual machines.
- Every storage account has a globally unique name and is accessible via a REST API or SDKs.
- You choose a performance tier (Standard or Premium) and a redundancy option (LRS, ZRS, GRS, RA-GRS, etc.).
- Data is encrypted at rest by default.
- Access is controlled through access keys, shared access signatures (SAS), or Azure Active Directory (Microsoft Entra ID).

**Why it matters**: Almost every Azure solution needs somewhere to store data. The Storage Account is the starting point for most data-related services.

---

## 5. Networking Basics🟦

Azure networking lets you securely connect resources, control traffic, and integrate with on-premises networks.

### Core components:
- **Virtual Network (VNet)**  
  A private, isolated network in Azure. Resources inside a VNet can communicate securely with each other.

- **Subnets**  
  Subdivisions of a VNet. You place resources (VMs, App Services, etc.) into specific subnets and can apply different security rules to each.

- **Network Security Groups (NSGs)**  
  Act like a firewall. They allow or deny inbound and outbound traffic based on rules (source/destination IP, port, protocol).

- **Public IP Addresses**  
  Make resources reachable from the internet.

- **Azure Load Balancer / Application Gateway**  
  Distribute traffic across multiple resources for high availability and performance.

- **VPN Gateway / ExpressRoute**  
  Securely connect your on-premises network to Azure (hybrid connectivity).

- **Azure Firewall / Azure Bastion**  
  Advanced security and secure remote access options.

**Key idea**: Networking in Azure is software-defined. You design the network topology first, then place compute and other resources inside it.

---

## 6. Azure Portal🟦

The **Azure Portal** is the web-based graphical interface for managing all Azure resources.

### Key points:
- Accessible at [https://portal.azure.com](https://portal.azure.com).
- Provides a visual way to create, configure, monitor, and delete resources.
- Features a customizable dashboard, search, and a rich set of blades (panels) for each service.
- Includes built-in tools such as:
  - Resource Explorer
  - Metrics and logs
  - Cost analysis
  - Azure Cloud Shell (browser-based Bash or PowerShell)
- Supports role-based access control (RBAC) so different users see only what they are allowed to manage.
- While the portal is excellent for learning and day-to-day management, production environments often use Infrastructure as Code (ARM, Bicep, Terraform) for consistency and automation.

**Tip**: Everything you do in the portal can also be done via Azure CLI, PowerShell, or REST APIs. The portal is the easiest way to start exploring Azure.