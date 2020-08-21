DROP DATABASE IF EXISTS `DungeonTrekker`;
CREATE DATABASE `DungeonTrekker`;
USE `DungeonTrekker`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `Tweet_dump` (
  `tweet_id` varchar(25) NOT NULL,
  `user_id` varchar(25) NOT NULL,
  PRIMARY KEY (`tweet_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Tweet_dump VALUES(1296760058089541637, 1277941458813812737);

CREATE TABLE `Users` (
  `user_id` varchar(25) NOT NULL,
  `name` varchar(50),
  `username` varchar(16),
  PRIMARY KEY (`user_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Users VALUES(1277941458813812737, 'Max Culley', '@MaxCulleyDev');