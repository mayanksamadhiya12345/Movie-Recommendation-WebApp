-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.2:3307
-- Generation Time: May 29, 2022 at 08:22 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `moviedata`
--

-- --------------------------------------------------------

--
-- Table structure for table `likemovie`
--

CREATE TABLE `likemovie` (
  `userid` int(11) NOT NULL,
  `movieid` int(11) NOT NULL,
  `sn` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `likemovie`
--

INSERT INTO `likemovie` (`userid`, `movieid`, `sn`) VALUES
(12, 19995, 14),
(12, 68735, 15),
(12, 68735, 16),
(12, 293863, 17),
(12, 1865, 18),
(12, 27205, 19),
(12, 10195, 20),
(16, 20526, 21),
(12, 293863, 22),
(12, 293863, 23),
(12, 293863, 24),
(12, 293863, 25),
(12, 293863, 26),
(12, 99861, 27),
(12, 99861, 28),
(12, 10195, 29),
(12, 76338, 30);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `likemovie`
--
ALTER TABLE `likemovie`
  ADD PRIMARY KEY (`sn`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `likemovie`
--
ALTER TABLE `likemovie`
  MODIFY `sn` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
