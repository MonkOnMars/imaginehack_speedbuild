-- somekind of bug on mysql, you need to use DROP
-- https://stackoverflow.com/questions/5555328/error-1396-hy000-operation-create-user-failed-for-jacklocalhost
drop user if exists "abc"@"localhost";


--- creation of a user
create user "abc"@"localhost" identified by "abc";
grant all privileges on game.* to "abc"@"localhost";
flush privileges;

--- creation of database
drop database if exists game;

create database game;
use game;


--- creation of tables

drop table if exists user;
create table user (
    `id` int not null auto_increment,
    `username` varchar(32) not null,
    `email` varchar(128) not null,
    `password` varchar(128) not null,
    primary key (`id`)
);



drop table if exists user_data;
create table user_data (
    `id` int not null auto_increment,
    `username` varchar(32) not null,
    `email` varchar(128) not null,
    `available_coins` int not null,
    `highest_level` int default 0,
    `funding_count` int default 0,
    primary key (`id`)
);

drop table if exists market_data;
-- create table market_data (
--     `id` int not null auto_increment,
--     `course_name` varchar(32) not null,
--     `start_date` int not null, 
--     `end_date` int not null,
--     `currency` varchar(3) not null default "MYR",
--     `cost` decimal(9,2) not null, 
--     `current_available_funds` decimal(9,2) not null,
--     `funding_people_count` int default 0,
--     primary key (`id`)
-- );
create table market_data (
    `id` int not null auto_increment,
    `course_name` varchar(32) not null,
    `currency` varchar(3) not null default "MYR",
    `current_available_funds` decimal(9,2) not null,
    `funding_people_count` int default 0,
    primary key (`id`)
);