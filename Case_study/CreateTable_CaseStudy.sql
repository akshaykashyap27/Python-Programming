CREATE TABLE `task` (
  `taskid` int NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `description` varchar(45) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `priority` int DEFAULT NULL,
  `notes` varchar(45) DEFAULT NULL,
  `bookmark` varchar(45) DEFAULT NULL,
  `ownerid` int DEFAULT NULL,
  `createrid` int DEFAULT NULL,
  `modifiedon` datetime DEFAULT NULL,
  `createdon` datetime DEFAULT NULL
) ;

CREATE TABLE `user` (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `contactno` bigint DEFAULT NULL,
  `role` varchar(45) DEFAULT NULL,
  `dob` datetime DEFAULT NULL,
  `createdon` datetime DEFAULT NULL,
  `modifiedon` datetime DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ;
