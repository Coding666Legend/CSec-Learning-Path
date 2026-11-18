#### Active Directory Lab Details
> Setting up Machines....

**Windows Server 2k22 (Domain Controller - DC) :**

| PC name:                 | EvilCorp-DC (HYDRA-DC)     |
| ------------------------ | -------------------------- |
| **NetBIOS domain name:** | ECORP (MARVEL)             |
| **Sys Pass:**            | Pass123!                   |
| **root domain name:**    | ECorp.local (MARVEL.local) |
| **DSRM pass:**           | Pass123!                   |
**Windows 10 Clients (DUs) :**

| User PC 1      |                                   | User PC 2      |                  |
| -------------- | --------------------------------- | -------------- | ---------------- |
| **Full Name:** | Elliot Alderson<br>(Frank Castle) | **Full Name:** | Darlene Alderson |
| **PC Name:**   | ElliotA                           | **PC Name:**   | DarleneA         |
| **pass:**      | Elliot@443                        | **pass:**      | Darlene@80       |

> setting up users, groups and polices...

**Domain Users (DUs) :**

| User 1      |                 | User 2      |                  |
| ----------- | --------------- | ----------- | ---------------- |
| Full Name:  | Elliot Alderson | Full Name:  | Darlene Alderson |
| login name: | EAlderson       | login name: | DAlderson        |
| pass:       | EA@DU443        | pass:       | DA@DU80          |
**Domain Admin (DA) :**

| DA          |                |
| ----------- | -------------- |
| Full Name:  | Tyrell Wellick |
| login name: | TWellick       |
| pass:       | TW@DA2022      |

**Fake Domain Admin - (A service account) :**

| Fake DA     |             |
| ----------- | ----------- |
| Full name:  | SQL Service |
| login name: | SQLService  |
| pass:       | SS@DA2022   |
