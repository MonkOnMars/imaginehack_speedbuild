
-- somekind of bug on mysql, you need to use DROP
-- https://stackoverflow.com/questions/5555328/error-1396-hy000-operation-create-user-failed-for-jacklocalhost
drop user if exists "abc"@"localhost";

create user "abc"@"localhost" identified by "abc";
grant all privileges on game.* to "abc"@"localhost";
flush privileges;

drop database if exists game;

create database game;
use game;

create table user (
    `id` int not null auto_increment,
    `username` varchar(32) not null,
    `password` varchar(128) not null,
    primary key (`id`)
);

