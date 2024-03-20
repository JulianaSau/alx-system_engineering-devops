-- create_mysql_user.sql

-- Create MySQL user holberton_user on web-01 and web-02
CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';
GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost';
FLUSH PRIVILEGES;

-- Optionally, you may also reload the SSH service to apply changes (Assuming SSH service is being used)
-- sudo systemctl reload ssh

-- Optionally, you may also restart MySQL service to apply changes (Assuming MySQL service is being used)
-- sudo systemctl restart mysql
