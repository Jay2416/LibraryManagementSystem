-- MySQL dump 10.13  Distrib 5.1.33, for Win32 (ia32)
--
-- Host: localhost    Database: library
-- ------------------------------------------------------
-- Server version	5.1.33-community

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `Cus_Id` int(4) NOT NULL,
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Username` varchar(50) NOT NULL,
  `Cus_Password` varchar(50) NOT NULL,
  `Cus_Age` int(4) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  PRIMARY KEY (`Cus_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (122,'Dev','Kakkad','dev128','dev@k',18,'8744521000'),(445,'John','Desai','john545','john%d1',32,'8966523014'),(455,'Siya','Nayak','snayak4','siya8',36,'8520014932'),(657,'Ramesh','Thakur','ramdt88','ramesh&2416',28,'9630014852'),(985,'Purvi','Patil','purvip321','pp#pp',16,'9856330145');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer_details`
--

DROP TABLE IF EXISTS `customer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer_details` (
  `Cus_Id` int(4) DEFAULT NULL,
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  `Book_Id` varchar(10) NOT NULL,
  `Book_Name` varchar(100) DEFAULT NULL,
  `Issue_Date` date DEFAULT NULL,
  `Due_Date` date DEFAULT NULL,
  `Fine` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer_details`
--

LOCK TABLES `customer_details` WRITE;
/*!40000 ALTER TABLE `customer_details` DISABLE KEYS */;
INSERT INTO `customer_details` VALUES (182,'Jay','Patel','9885412021','BKID642','Python Programming (Class 12)','2021-12-15','2021-12-26','Rs. 90'),(248,'Harsh','Parmar','6544854558','BKID905','All about CALCULUS','2021-03-03','2021-03-14','Rs. 40'),(184,'Jay','Rana','9885412020','BKID512','Gulliver Travels','2021-01-11','2021-01-23','Rs. 40'),(256,'Kirti','Prajapati','9885445120','BKID321','Mysteries of Universe','2021-06-04','2021-06-18','Rs. 80'),(248,'Harsh','Parmar','6544854558','BKID905','All about CALCULUS','2021-03-03','2021-03-14','Rs. 40');
/*!40000 ALTER TABLE `customer_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delete_cus_details`
--

DROP TABLE IF EXISTS `delete_cus_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delete_cus_details` (
  `Cus_Id` int(4) DEFAULT NULL,
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  `Book_Id` varchar(10) NOT NULL,
  `Book_Name` varchar(64) NOT NULL,
  `Issue_Date` date DEFAULT NULL,
  `Due_Date` date DEFAULT NULL,
  `Fine` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delete_cus_details`
--

LOCK TABLES `delete_cus_details` WRITE;
/*!40000 ALTER TABLE `delete_cus_details` DISABLE KEYS */;
INSERT INTO `delete_cus_details` VALUES (700,'Ramesh','Tandel','6655411028','BKID973','General Knowledge','2021-05-03','2021-05-12','');
/*!40000 ALTER TABLE `delete_cus_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `delete_stud_login`
--

DROP TABLE IF EXISTS `delete_stud_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `delete_stud_login` (
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  `Cus_Age` int(4) DEFAULT NULL,
  `Book_Id` varchar(12) NOT NULL,
  `Book_Name` varchar(64) NOT NULL,
  `Issue_date` date DEFAULT NULL,
  `Due_Date` date DEFAULT NULL,
  `Price` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delete_stud_login`
--

LOCK TABLES `delete_stud_login` WRITE;
/*!40000 ALTER TABLE `delete_stud_login` DISABLE KEYS */;
INSERT INTO `delete_stud_login` VALUES ('Kirti','Khanna','9985400157',42,'BKID973','General Knowledge','2021-05-03','2021-05-11','Rs. 549');
/*!40000 ALTER TABLE `delete_stud_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee` (
  `Emp_Id` int(4) NOT NULL,
  `Emp_Name` varchar(64) NOT NULL,
  `Emp_Surname` varchar(20) DEFAULT NULL,
  `Emp_Username` varchar(50) NOT NULL,
  `Emp_Password` varchar(50) NOT NULL,
  `Emp_Age` int(4) DEFAULT NULL,
  `Emp_Mob` varchar(12) NOT NULL,
  PRIMARY KEY (`Emp_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (415,'Komal','Modi','komalmodi123','#komal64',16,'9755463120'),(442,'Hardik','Thakur','hardik28','dik88',18,'7885441025'),(745,'Karan','Patel','karanpatel84','k&p88',28,'9005467244'),(754,'Ram','Parmar','rampatel55','rp%24',32,'9776452120'),(985,'Daya','Tandel','daya@2416','daya$tandel',36,'8452213021');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `left_customer`
--

DROP TABLE IF EXISTS `left_customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `left_customer` (
  `Cus_Id` int(4) NOT NULL,
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Username` varchar(50) NOT NULL,
  `Cus_Password` varchar(50) NOT NULL,
  `Cus_Age` int(4) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  PRIMARY KEY (`Cus_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `left_customer`
--

LOCK TABLES `left_customer` WRITE;
/*!40000 ALTER TABLE `left_customer` DISABLE KEYS */;
/*!40000 ALTER TABLE `left_customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `left_employee`
--

DROP TABLE IF EXISTS `left_employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `left_employee` (
  `Cus_Id` int(4) NOT NULL,
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Username` varchar(50) NOT NULL,
  `Cus_Password` varchar(50) NOT NULL,
  `Cus_Age` int(4) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  PRIMARY KEY (`Cus_Id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `left_employee`
--

LOCK TABLES `left_employee` WRITE;
/*!40000 ALTER TABLE `left_employee` DISABLE KEYS */;
/*!40000 ALTER TABLE `left_employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_login`
--

DROP TABLE IF EXISTS `student_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student_login` (
  `Cus_Name` varchar(64) NOT NULL,
  `Cus_Surname` varchar(20) DEFAULT NULL,
  `Cus_Mob` varchar(12) NOT NULL,
  `Cus_Age` int(4) DEFAULT NULL,
  `Book_Id` varchar(12) NOT NULL,
  `Book_Name` varchar(100) DEFAULT NULL,
  `Issue_date` date DEFAULT NULL,
  `Due_Date` date DEFAULT NULL,
  `Price` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_login`
--

LOCK TABLES `student_login` WRITE;
/*!40000 ALTER TABLE `student_login` DISABLE KEYS */;
INSERT INTO `student_login` VALUES ('Vipul','Shah','995441202',24,'BKID862','Guiness World Records','2021-05-03','2021-05-16','Rs. 699'),('Jiten','Patel','2553321886',21,'BKID512','Gulliver Travels','2021-05-06','2021-05-19','Rs. 649');
/*!40000 ALTER TABLE `student_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-07 16:22:58
