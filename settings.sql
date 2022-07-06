CREATE DATABASE planner_auth;
CREATE USER planner_user WITH PASSWORD 'password';
GRANT ALL PRIVILEGES ON DATABASE planner_auth TO planner_user;