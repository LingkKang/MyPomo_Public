show databases;

show tables;

show databases;

create database if not exists all_users;

alter database default character set 'utf8mb4';

use all_users;

create table if not exists user_list(
    ID int auto_increment,
    User_Name varchar(16),
    Joined_Time datetime default current_timestamp,
    Total_Time float default 0,
    Last_Visit_Time datetime default current_timestamp on update current_timestamp,
    Comments tinytext,
    primary key (ID)
);
