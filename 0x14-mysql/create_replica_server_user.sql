-- Create the replica_user with appropriate permissions for replication
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replicauserpassword';
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';

-- Grant SELECT privilege on mysql.user to holberton_user
GRANT SELECT ON mysql.user TO 'holberton_user'@'localhost';

-- mysql -u root -p < create_replica_user.sql
