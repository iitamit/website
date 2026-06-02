-- Run this while connected as the PostgreSQL superuser.
-- Replace the password before executing the script.
CREATE USER ik_seoul_user WITH PASSWORD 'replace-with-a-strong-password';
CREATE DATABASE ik_seoul_db OWNER ik_seoul_user;
