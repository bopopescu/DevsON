-- MySQL dump 10.16  Distrib 10.1.34-MariaDB, for Win32 (AMD64)
--
-- Host: localhost    Database: tg
-- ------------------------------------------------------
-- Server version	10.1.34-MariaDB

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
-- Current Database: `tg`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `tg` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tg`;

--
-- Table structure for table `atirador`
--

DROP TABLE IF EXISTS `atirador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atirador` (
  `ra` int(11) NOT NULL AUTO_INCREMENT,
  `nome` varchar(45) DEFAULT NULL,
  `cpf` varchar(45) DEFAULT NULL,
  `endereco` varchar(100) DEFAULT NULL,
  `nascimento` date DEFAULT NULL,
  `pontuacao` int(2) DEFAULT NULL,
  PRIMARY KEY (`ra`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atirador`
--

LOCK TABLES `atirador` WRITE;
/*!40000 ALTER TABLE `atirador` DISABLE KEYS */;
INSERT INTO `atirador` VALUES (1,'Leandro','42230201883','Santo Antonio, 388','1997-01-04',10),(2,'Leandro','42230201883','Santo Antonio, 388','1997-01-04',10),(3,'Leandro','42230201883','Santo Antonio, 388','1997-01-04',10),(4,'Carlos','42230201883','Santo Antonio, 388','1997-01-04',10),(6,'Josue ','42230201883','Santo Antonio, 388','2018-01-04',24),(9,'','','','0000-00-00',0),(10,'','','','0000-00-00',0),(11,'','','','0000-00-00',0),(12,'Divani','42230201883','Santo Antonio, 388','0000-00-00',450),(13,'Leandro','42230201883','Santo Antonio, 388','2018-04-01',15),(14,'teste','1111111111111','santo antonio, 388','1997-01-04',45),(15,'eeeee','11111','1111','0000-00-00',1111),(16,'wagner','111111111111','santo antonio','2018-11-06',33333);
/*!40000 ALTER TABLE `atirador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guarda`
--

DROP TABLE IF EXISTS `guarda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guarda` (
  `idguarda` int(11) NOT NULL,
  `idatirador` int(11) DEFAULT NULL,
  `ra` int(11) DEFAULT NULL,
  `nome` varchar(45) DEFAULT NULL,
  `data_guarda` date DEFAULT NULL,
  PRIMARY KEY (`idguarda`),
  KEY `fk_atirador` (`idatirador`),
  CONSTRAINT `fk_atirador` FOREIGN KEY (`idatirador`) REFERENCES `atirador` (`ra`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guarda`
--

LOCK TABLES `guarda` WRITE;
/*!40000 ALTER TABLE `guarda` DISABLE KEYS */;
INSERT INTO `guarda` VALUES (0,NULL,1,'Leandro','2222-02-22');
/*!40000 ALTER TABLE `guarda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user` varchar(15) DEFAULT NULL,
  `senha` int(4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'',1234),(2,'Alessandro',112);
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-11-07  0:13:48
