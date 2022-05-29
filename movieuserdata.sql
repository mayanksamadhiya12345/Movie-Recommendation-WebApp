-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.2:3307
-- Generation Time: May 29, 2022 at 08:21 PM
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
-- Table structure for table `movieuserdata`
--

CREATE TABLE `movieuserdata` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `useremail` varchar(100) NOT NULL,
  `userpassword` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `movieuserdata`
--

INSERT INTO `movieuserdata` (`id`, `username`, `useremail`, `userpassword`) VALUES
(12, 'mayank', 'mayank@gmail.com', '1234'),
(13, 'shivam', 'shivam@gmail.com', '1234'),
(14, 'thor', '1234@gmail.com', '12345'),
(15, '1234', '12@gmail.com', '1234'),
(16, 'palak', 'palak@gmail.com', '1234'),
(17, 'thor', '12@gmail.com', '1234'),
(18, 'thor', '12@gmail.com', '1234'),
(19, 'hima', 'hima@gmail.com', '123'),
(20, 'tyudeg', 'maay@gmai.com', '111'),
(21, 'avae', 're@gmail.com', '1'),
(22, 'shi', 'shi@gmail.com', '122');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `movieuserdata`
--
ALTER TABLE `movieuserdata`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `movieuserdata`
--
ALTER TABLE `movieuserdata`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
