-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jul 22, 2024 at 08:03 AM
-- Server version: 8.3.0
-- PHP Version: 8.2.18

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `airline`
--

-- --------------------------------------------------------

--
-- Table structure for table `airline_admins`
--

DROP TABLE IF EXISTS `airline_admins`;
CREATE TABLE IF NOT EXISTS `airline_admins` (
  `SNO` int NOT NULL,
  `admin_name` varchar(30) NOT NULL,
  `admin_pass` varchar(30) NOT NULL,
  PRIMARY KEY (`SNO`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `airline_admins`
--

INSERT INTO `airline_admins` (`SNO`, `admin_name`, `admin_pass`) VALUES
(100, 'sai', 'sai1'),
(101, 'saikiran', 'saikiran1'),
(102, 'vandana', 'vandana1'),
(103, 'ramesh', 'ramesh1'),
(104, 'rajitha', 'rajitha1');

-- --------------------------------------------------------

--
-- Table structure for table `airline_reservation`
--

DROP TABLE IF EXISTS `airline_reservation`;
CREATE TABLE IF NOT EXISTS `airline_reservation` (
  `PNR` int NOT NULL AUTO_INCREMENT,
  `flight_Number` varchar(11) NOT NULL,
  `flight_Name` varchar(100) DEFAULT NULL,
  `origin` varchar(100) DEFAULT NULL,
  `dest` varchar(100) DEFAULT NULL,
  `flight_class` varchar(100) DEFAULT NULL,
  `quota_type` varchar(100) DEFAULT NULL,
  `adult` int NOT NULL,
  `child` int DEFAULT NULL,
  `base_fare` int DEFAULT NULL,
  `class_fare` int DEFAULT NULL,
  `quota_fare` int DEFAULT NULL,
  `quota_discount` int DEFAULT NULL,
  `trip_mode` varchar(10) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `trip_discount` int DEFAULT NULL,
  `fare` int DEFAULT NULL,
  `Km` int DEFAULT NULL,
  `booked_on` varchar(100) DEFAULT NULL,
  `jd` varchar(100) DEFAULT NULL,
  `rd` varchar(100) DEFAULT NULL,
  `booked_by` varchar(100) DEFAULT NULL,
  `status` varchar(5) DEFAULT NULL,
  `can_on` varchar(40) DEFAULT NULL,
  `refund_Rs` int DEFAULT NULL,
  `pay_mode` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`PNR`),
  UNIQUE KEY `PNR` (`PNR`)
) ENGINE=MyISAM AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airline_reservation`
--

INSERT INTO `airline_reservation` (`PNR`, `flight_Number`, `flight_Name`, `origin`, `dest`, `flight_class`, `quota_type`, `adult`, `child`, `base_fare`, `class_fare`, `quota_fare`, `quota_discount`, `trip_mode`, `trip_discount`, `fare`, `Km`, `booked_on`, `jd`, `rd`, `booked_by`, `status`, `can_on`, `refund_Rs`, `pay_mode`) VALUES
(100, 'AA12AA', 'SKA AIRLINES', 'NEW DELHI-NDL', 'NEW YORK-NY', 'FIRST CLASS', 'DEFENCE', 4, 0, 240570, 6000, 0, -4000, 'ROUND TRIP', 9720, 962280, 11600, '22/Jul/2024 01:31:46 PM', '25/Jul/2024', '31/Jul/2024', 'sai', 'CNF', NULL, NULL, NULL);

--
-- Triggers `airline_reservation`
--
DROP TRIGGER IF EXISTS `increment_PNR_Number`;
DELIMITER $$
CREATE TRIGGER `increment_PNR_Number` BEFORE INSERT ON `airline_reservation` FOR EACH ROW BEGIN
    SET NEW.PNR = IFNULL((SELECT MAX(PNR) FROM airline_reservation), 99) + 1;
END
$$
DELIMITER ;
DROP TRIGGER IF EXISTS `update_tstatus`;
DELIMITER $$
CREATE TRIGGER `update_tstatus` BEFORE INSERT ON `airline_reservation` FOR EACH ROW BEGIN
    DECLARE new_status VARCHAR(10);
    IF NEW.status IS NULL THEN
        SET new_status = 'CNF';
    ELSE
        SET new_status = NEW.status;
    END IF;
    SET NEW.status = new_status;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `airline_sitting`
--

DROP TABLE IF EXISTS `airline_sitting`;
CREATE TABLE IF NOT EXISTS `airline_sitting` (
  `sno` int NOT NULL AUTO_INCREMENT,
  `PNR` int DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `age` varchar(10) DEFAULT NULL,
  `gender` varchar(30) DEFAULT NULL,
  `seat_number` varchar(10) DEFAULT NULL,
  `berth` varchar(20) DEFAULT NULL,
  `ausr` varchar(30) DEFAULT NULL,
  `aadm` varchar(30) DEFAULT NULL,
  `abd` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`sno`),
  KEY `PNR` (`PNR`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airline_sitting`
--

INSERT INTO `airline_sitting` (`sno`, `PNR`, `name`, `age`, `gender`, `seat_number`, `berth`, `ausr`, `aadm`, `abd`) VALUES
(1, 100, 'Adepu Sai Kiran', '24', 'Male', '1A', NULL, NULL, 'sai', NULL),
(2, 100, 'Panthakani Vandana', '24', 'Female', '1B', NULL, NULL, 'sai', NULL),
(3, 100, 'Adepu Ramesh', '45', 'Male', '1C', NULL, NULL, 'sai', NULL),
(4, 100, 'Adepu Rajitha', '44', 'Female', '1D', NULL, NULL, 'sai', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `airline_ufeedback`
--

DROP TABLE IF EXISTS `airline_ufeedback`;
CREATE TABLE IF NOT EXISTS `airline_ufeedback` (
  `Feedback_number` int NOT NULL AUTO_INCREMENT,
  `User_number` int DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `feedback` varchar(500) DEFAULT NULL,
  `dateofeed` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`Feedback_number`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airline_ufeedback`
--

INSERT INTO `airline_ufeedback` (`Feedback_number`, `User_number`, `name`, `feedback`, `dateofeed`) VALUES
(1, NULL, 'sai', 'Good SKA AIRLINE Services', '13:33:31 2024-07-16'),
(2, NULL, 'Adepu Sai Kiran', 'Good Service', '16/Jul/2024 03:40:32 PM'),
(10, NULL, 'Vandana', 'Good Airline Service ', '16/Jul/2024 03:53:10 PM'),
(9, NULL, 'Vandana', 'Good Service by SKA Airlines', '16/Jul/2024 03:50:57 PM'),
(8, NULL, 'Sai Kiran', 'Rapidly Developing Airline Services', '16/Jul/2024 03:48:16 PM'),
(11, NULL, 'Vandana', 'Excellent Services offered by SKA', '16/Jul/2024 03:54:23 PM'),
(12, NULL, 'Vandana', 'Excellent Services offered by SKA AIRLINES', '16/Jul/2024 03:56:18 PM');

-- --------------------------------------------------------

--
-- Table structure for table `airline_users`
--

DROP TABLE IF EXISTS `airline_users`;
CREATE TABLE IF NOT EXISTS `airline_users` (
  `User_no` int NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `gender` varchar(15) NOT NULL,
  `address` varchar(400) NOT NULL,
  `mobile_number` varchar(20) NOT NULL,
  `DOB` varchar(20) DEFAULT NULL,
  `IDT` varchar(20) NOT NULL,
  `IDN` varchar(20) NOT NULL,
  `DOR` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`User_no`)
) ENGINE=MyISAM AUTO_INCREMENT=1004 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airline_users`
--

INSERT INTO `airline_users` (`User_no`, `username`, `password`, `gender`, `address`, `mobile_number`, `DOB`, `IDT`, `IDN`, `DOR`) VALUES
(1000, 'sai', 'sai1', 'Male', 'gpl', '703216', '1999-07-15', 'Aadhar', '5379315370', '19:51:12 2023-3-20'),
(1002, 'vandana', 'vandana1', 'Female', '7-26 Mahadevporam', '09949', '1999-05-12', 'Aadhar Card', '45457858', '9/Jul/2024 12:22:49 PM'),
(1003, 'Vignesh', 'vi1', 'Male', '1-54 Hyd', '98989898', '2001-10-17', 'Aadhar Card', '545454', '19/Jul/2024 11:04:03 AM');

-- --------------------------------------------------------

--
-- Table structure for table `airplane_fare`
--

DROP TABLE IF EXISTS `airplane_fare`;
CREATE TABLE IF NOT EXISTS `airplane_fare` (
  `route_id` int NOT NULL AUTO_INCREMENT,
  `Airport` varchar(100) NOT NULL,
  `Fare` int DEFAULT NULL,
  `KM` int DEFAULT NULL,
  `AAD` varchar(30) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  PRIMARY KEY (`route_id`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airplane_fare`
--

INSERT INTO `airplane_fare` (`route_id`, `Airport`, `Fare`, `KM`, `AAD`) VALUES
(1, 'NEW DELHI-NDL,NEW YORK-NY', 121000, 11600, 'sai'),
(2, 'NEW DELHI-NDL,WASHINGTON-DC', 123000, 12100, 'sai'),
(3, 'NEW DELHI-NDL,CALIFORNIA-CF', 190000, 21100, 'sai');

-- --------------------------------------------------------

--
-- Table structure for table `airports`
--

DROP TABLE IF EXISTS `airports`;
CREATE TABLE IF NOT EXISTS `airports` (
  `airport_id` int NOT NULL AUTO_INCREMENT,
  `airport_name` varchar(80) DEFAULT NULL,
  PRIMARY KEY (`airport_id`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

--
-- Dumping data for table `airports`
--

INSERT INTO `airports` (`airport_id`, `airport_name`) VALUES
(1, 'NEW DELHI-NDL'),
(2, 'NEW YORK-NY'),
(3, 'HYDERABAD-HYD'),
(4, 'CHENNAI-CHN'),
(5, 'WASHINGTON-DC'),
(6, 'MUMBAI-MBI'),
(7, 'CALIFORNIA-CF'),
(8, 'CHICAGO-CG'),
(9, 'SANFRANSISCO-SF');

-- --------------------------------------------------------

--
-- Table structure for table `flights`
--

DROP TABLE IF EXISTS `flights`;
CREATE TABLE IF NOT EXISTS `flights` (
  `flight_number` varchar(10) NOT NULL,
  `flight_Name` varchar(55) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `Airports` varchar(5555) DEFAULT NULL,
  `Base_Fare` int DEFAULT NULL,
  `CLASS` varchar(100) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `ticket_type` varchar(60) DEFAULT NULL,
  `Flight_Addedon` varchar(60) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `Flight_Admin` varchar(60) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  PRIMARY KEY (`flight_number`),
  UNIQUE KEY `Flight_number` (`flight_number`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `flights`
--

INSERT INTO `flights` (`flight_number`, `flight_Name`, `Airports`, `Base_Fare`, `CLASS`, `ticket_type`, `Flight_Addedon`, `Flight_Admin`) VALUES
('AA12AA', 'SKA AIRLINES', 'NEW DELHI-NDL,NEW YORK-NY,HYDERABAD-HYD', 95000, 'FIRST CLASS,BUSINESS CLASS,PREMIUM ECONOMY,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:23:02 PM', 'SAI'),
('AA12BB', 'SKA AIRLINES', 'HYDERABAD-HYD,WASHINGTON-DC', 101000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:24:01 PM', 'SAI'),
('AA12CC', 'VANDANA AIRLINES', 'NEW DELHI-NDL,WASHINGTON-DC', 100000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:27:31 PM', 'SAI'),
('AA12DD', 'RAJITHA AIRLINES', 'HYDERABAD-HYD,WASHINGTON-DC', 101000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:28:43 PM', 'SAI'),
('AA12EE', 'RAMESH AIRLINES', 'NEW DELHI-NDL,WASHINGTON-DC', 120000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:30:43 PM', 'SAI'),
('AA12FF', 'SINDHU AIRLINES', 'NEW DELHI-NDL,NEW YORK-NY', 92000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '7/Jul/2024 04:50:47 PM', 'SAI'),
('AA12GG', 'SKA AIRLINES', 'NEW DELHI-NDL,NEW YORK-NY', 125000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,TATKAL,SENIOR CITIZEN,', '8/Jul/2024 12:03:45 PM', 'SAI'),
('AA12HH', 'VANDANA AIRLINES', 'NEW DELHI-NDL,NEW YORK-NY', 125000, 'FIRST CLASS,BUSINESS CLASS,PREMIUM ECONOMY,ECONOMY,', 'GENERAL,DEFENCE,GOVT EMPLOYEE,SENIOR CITIZEN,STUDENT,', '8/Jul/2024 12:14:45 PM', 'SAI'),
('AA12II', 'SKA AIRLINES', 'NEW DELHI-NDL,NEW YORK-NY,HYDERABAD-HYD,CHENNAI-CHN,WASHINGTON-DC,MUMBAI-MBI,CALIFORNIA-CF,CHICAGO-CG,SANFRANSISCO-SF', 210000, 'FIRST CLASS,BUSINESS CLASS,', 'GENERAL,', '14/Jul/2024 08:54:34 PM', 'SAI');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
