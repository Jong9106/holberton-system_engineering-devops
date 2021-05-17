![enter image description here](https://i.imgur.com/VhsBY7O.png)
# 0x19. Postmortem
![enter image description here](https://i.imgur.com/0rRhQfr.jpg)

## Issue Summary

### Resume of problem

Unable to establish a connection to the MySQL database hosted on server 1

### Duration

From 04/27/2021 6:00 p.m. to 04/27/2021 11:00 p.m. (GMT-5)

### Impact

No new data could be stored on server 1, there is only one copy left on server 2 which is a replica of the main one.

### Root cause

The Ubuntu version did not allow the correct installation of MySQL and the service had to be restarted several times for its correct operation and sometimes it did not host the information.

## Timeline

The problem was detected in a third attempt to host information, and it did not reach the database on server 2 with the replica, once the service was restarted it worked but it is not the proper way.

### Action taken

It was changed to a newer version that contains more updated repositories and the MySQL service was re-listed and the data from server 2 was copied and it became the master database again.

### Misleading investigation

They proceeded to revoke the permissions from the master database to the slave, thinking that they were poorly implemented.

### How the incident was resolved

The incident was resolved on 04/15/2021 at 11 p.m. When updating the Ubuntu version to 20.04, then the MySQL service was reinstalled on server one and the backup was uploaded, after several tests there was no need to restart the service.


## Corrective and preventative measures

Review the series of the tasks, if these tend to turn off during the activities they must be reinstalled, although version 14 and 16 are more complete, the most recent versions dream of solving some bugs more efficiently.

## Author
 
 - **Juan Carlos Hernández** : Twitter - [@luigi_jong](https://twitter.com/luigi_jong)
 
##  info

 - Date 16/05/2021
 - Holberton school Colombia 
 - Cohort #13 BOG0920