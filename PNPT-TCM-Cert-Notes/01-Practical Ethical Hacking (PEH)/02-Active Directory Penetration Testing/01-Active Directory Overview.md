# Introduction
A Microsoft directory service used to centrally manage **users, computers, printers, groups, authentication, and access permissions** within a Windows domain. It relies on components like **Domain Controllers, LDAP, Kerberos, and Group Policy** to manage domain resources and security. It is a major target during internal penetration tests due to potential privilege escalation and lateral movement paths.

> P.S. 
> Now we are inside the Network. And would be Following Internal Penetration Testing Methodologies

**Active Directory is the most commonly used identity management service in the world**
It can be exploited without ever attacking patchable exploits
- Instead, we abuse features, trusts, components, tickets, hashes, etc.
# Active Directory Components

| PHYSICAL                           | LOGICAL                  |
| ---------------------------------- | ------------------------ |
| Data Store                         | Partitions               |
| Domain Controllers                 | Schema                   |
| Global catalog server              | Domains                  |
| Read-only Domain Controller (RODC) | Domain trees             |
|                                    | Forests                  |
|                                    | Sites                    |
|                                    | Organization Units (OUs) |
## Physical AD Components
#### Domain Controllers
DC is a server with the AD DS (domain services) server role installed, that has specifically been promoted to a domain controller
- Host a Copy of the AD DS (domain services) directory store
- Provide authentication and authorization services
- Replicate updates to other domain controllers in the domain and forest
- Allow administrative access to manage user accounts and network resources
#### AD DS Data Store
This contains the database files and processes that store and manage directory information for users, services, and applications
- Consists of the Ntds.dit file
- Is stored by default in the %SystemRoot%\NTDS folder on all domain controllers
- Is accessible only through the domain controller processes and protocol
## Logical AD Components
#### AD DS Schema
- Defines every type of object that can be stored in the directory
- Enforces rules regarding object creation and configuration


| Object Types         | Function                                      | Example                            |
| -------------------- | --------------------------------------------- | ---------------------------------- |
| **Class Object**     | What objects can be created in the directory  | - User<br>- Computer<br>- Printers |
| **Attribute Object** | Information that can be attached to an object | - Display name                     |
#### Domains
Domains are used to group and manage objects in an organization
- An administrative boundary for applying policies to groups of objects
- A replication boundary for replicating data between domain controllers
- An Authentication and authorization boundary that provides a way to limit the scope of the access to the resources
#### Trees
A domain tree is a hierarchy of domains in AD DS
All domains in the tree:
- Share a contiguous namespace with the parent domain
- Can have additional child domains
- By default create a two-way transitive trust with other domains
#### Forests
A Forest in a collection of one or more domain trees
- Share a common schema
- Share a common configuration partition
- Share a common global catalog to enable searching
- Enable trusts between all domains in the forest
- Share the Enterprise Admins and Schema Admins groups
#### Organizational Units (OUs)
OUs are Active Directory containers that can contain users, groups, computers, printers, and other OUs
OUs are used to:
- Represent your organization hierarchically and logically
- Manage a collection of objects in a consistent way
- Delegate permissions to administer groups of objects
- Apply policies
#### Trusts
Trusts provide a mechanism for users to gain access to resources in another domain


| Types of Trusts | Description                                                                                   |
| --------------- | --------------------------------------------------------------------------------------------- |
| Directional     | The Trust direction flows from trusting domain to the trusted domain                          |
| Transitive      | The Trust relationship is extended beyond a two-domain trust to include other trusted domains |
> - All Domains in a forest trust all other domains in the forest
> - Trusts can extend outside the forest

#### Objects

| Object         | Description                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------ |
| User           | - Enables network resource access for a user                                                     |
| InetOrgPerson  | - Similar to a use account<br>- Used for compatibility with other directory services             |
| Contacts       | - Used primarily to assign email addresses to external users<br>- Does not enable network access |
| Groups         | - Used to simplify the administration of access control                                          |
| Computers      | - Enables authentication and auditing of computer access to resources                            |
| Printers       | - Used to simplify the process of locating and connecting to printers                            |
| Shared Folders | - Enables users to search for shared folders based on properties                                 |
























