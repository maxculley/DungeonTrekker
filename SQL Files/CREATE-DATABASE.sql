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

CREATE TABLE `Rooms` (
  `room_id` varchar(3),
  `forward` varchar(2),
  `back` varchar(2),
  `left` varchar(2),
  `right` varchar(2),
  `up` varchar(2),
  `down` varchar(2),
  PRIMARY KEY (`room_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO Rooms VALUES(1, 2, 0, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(2, 3, 0, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(3, 0, 0, 4, 5, 0, 0); # WORKS
INSERT INTO Rooms VALUES(4, 0, 0, 0, 6, 0, 0); # WORKS
INSERT INTO Rooms VALUES(5, 0, 0, 6, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(6, 7, 0, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(7, 0, 0, 0, 0, 0, 8); # WORKS
INSERT INTO Rooms VALUES(8, 9, 0, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(9, 11, 0, 10, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(10, 0, 0, 0, 13, 0, 12); # WORKS
INSERT INTO Rooms VALUES(11, 14, 90, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(12, 16, 0, 15, 17, 0, 0); # WORKS
INSERT INTO Rooms VALUES(13, 19, 0, 0, 0, 18, 0); # WORKS
INSERT INTO Rooms VALUES(14, 0, 90, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(15, 21, 0, 0, 0, 20, 0); # WORKS
INSERT INTO Rooms VALUES(16, 0, 0, 22, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(17, 0, 0, 23, 23, 0, 0);
INSERT INTO Rooms VALUES(18, 0, 0, 24, 24, 0, 0); # WORKS
INSERT INTO Rooms VALUES(19, 0, 0, 0, 0, 25, 0); # WORKS
INSERT INTO Rooms VALUES(20, 0, 0, 0, 0, 0, 27); # WORKS
INSERT INTO Rooms VALUES(21, 0, 0, 0, 0, 0, 26); # WORKS
INSERT INTO Rooms VALUES(22, 0, 0, 27, 27, 0, 0); # WORKS
INSERT INTO Rooms VALUES(23, 27, 0, 27, 27, 0, 27);
INSERT INTO Rooms VALUES(24, 0, 0, 27, 27, 27, 0); # WORKS
INSERT INTO Rooms VALUES(25, 0, 91, 0, 0, 0, 0); # WORKS
INSERT INTO Rooms VALUES(26, 0, 0, 27, 27, 0, 26); # WORKS
INSERT INTO Rooms VALUES(27, 0, 0, 0, 0, 28, 0); # WORKS
INSERT INTO Rooms VALUES(91, 0, 0, 0, 0, 18, 0); # WORKS
INSERT INTO Rooms VALUES(90, 25, 0, 0, 0, 0, 0); # WORKS

CREATE TABLE `User_games` (
  `user_id` varchar(25) NOT NULL,
  `current_room_id` varchar(3),
  `current_code` varchar(9),
  `current_riddle` varchar(15),
  PRIMARY KEY (`user_id`)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO User_games VALUES(1277941458813812737, 12, 0, 0);