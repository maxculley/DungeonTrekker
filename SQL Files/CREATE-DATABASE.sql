DROP DATABASE IF EXISTS `DungeonTrekker`;
CREATE DATABASE `DungeonTrekker`;
USE `DungeonTrekker`;

SET NAMES utf8 ;
SET character_set_client = utf8mb4 ;

CREATE TABLE `General` (
  `latest_mention_id` varchar(25) NOT NULL,
  PRIMARY KEY (`latest_mention_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
  INSERT INTO `General` VALUES(0);

CREATE TABLE `Users` (
  `user_id` varchar(25) NOT NULL,
  PRIMARY KEY (`user_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;