MySQL Configuration Project

This project involves tasks to learn how to set up MySQL for a production environment.

Tasks to Complete

Install MySQL

Install MySQL version 5.7.x on both the web-01 and web-02 servers.
Ensure that SSH task #3 has been completed on both servers. The checker will connect to these servers to verify MySQL status.
User Creation

Create a MySQL user named holberton_user on both web-01 and web-02 with localhost as the host and projectcorrection280hbtn as the password. This user will allow us to access replication status on both servers.
Verify that holberton_user has the necessary permissions to view the primary and replica status of the databases.
Database and Table Setup

Set up a database named tyrell_corp.
Within this database, create a table called nexus6 and insert at least one record. This setup is required for replication.
Ensure that holberton_user has SELECT permissions on this table so we can confirm that it exists and contains data.
Replication User Configuration

Create a MySQL user named replica_user with access from % and a password of your choice.
Grant replica_user the necessary permissions for replication from the primary MySQL server.
holberton_user will need SELECT access to the mysql.user table to confirm that replica_user has the correct permissions.
Primary-Replica Setup

Host MySQL as the primary server on web-01. Do not configure the bind-address; simply comment out this parameter.
Host MySQL as the replica server on web-02.
Configure replication for the tyrell_corp database.
Place the MySQL primary configuration file in 4-mysql_configuration_primary and the replica configuration file in 4-mysql_configuration_replica.
After setting up replication, add a record to the table on web-01 and verify its presence on web-02 to ensure replication is functioning.
Confirm that UFW is configured to allow connections on port 3306 to ensure replication works correctly.
Backup MySQL

The 5-mysql_backup script should:
Create a dump of all MySQL databases.
Save the dump file as backup.sql.
Compress the dump file into a tar.gz archive.
Name the archive with the format day-month-year.tar.gz.
Connect to the MySQL database as the root user.
Accept the database password as an argument.
