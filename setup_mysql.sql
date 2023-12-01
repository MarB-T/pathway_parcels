-- Create database for pathway_parcels

CREATE DATABASE IF NOT EXISTS pathway_db;
CREATE USER IF NOT EXISTS 'pathway_admin'@'localhost' IDENTIFIED BY 'Pathway_admin_0';
GRANT ALL PRIVILEGES ON `pathway_db`.* TO 'pathway_admin'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'pathway_admin'@'localhost';
FLUSH PRIVILEGES;
