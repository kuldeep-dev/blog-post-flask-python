-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Aug 21, 2019 at 12:12 PM
-- Server version: 10.1.38-MariaDB
-- PHP Version: 7.3.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_blog`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` varchar(25) NOT NULL,
  `message` text NOT NULL,
  `created` datetime DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `name`, `email`, `phone`, `message`, `created`) VALUES
(1, 'afasd', 'asdf@sd.sd', '2323232323', 'dafsdfasdfasdf', '2019-08-19 13:19:29'),
(2, 'kuldeep', 'test@test.com', '1236547890', 'dsfsafdsfsdaf', NULL),
(3, 'aadf', 'admin@educators.com', '8054079951', 'asdfasdfasdfas fasdfasdfa dsfasdfasd asf', '2019-08-19 09:19:56'),
(5, 'adfasdfa', 'fasdfa@gfsdf.fgfh', '1231231233', 'fasd saf asdfasdf  sadfasdfsaf ', '2019-08-19 10:39:26');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `id` int(11) NOT NULL,
  `title` text NOT NULL,
  `tagname` text,
  `slug` varchar(250) NOT NULL,
  `content` text NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `created` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`id`, `title`, `tagname`, `slug`, `content`, `image`, `created`) VALUES
(2, 'this is blog1', NULL, 'first-post2', 'this is first post2', NULL, '2019-08-19 17:21:19'),
(3, 'this is blog2', NULL, 'first-post', 'this is first post', NULL, '2019-08-19 17:21:19'),
(4, 'this is blog3', NULL, 'first-post2', 'this is first post2', NULL, '2019-08-19 17:21:19'),
(5, 'this is blog4', NULL, 'first-post', 'this is first post', NULL, '2019-08-19 17:21:19'),
(6, 'this is blog5', NULL, 'first-post2', 'this is first post2', NULL, '2019-08-19 17:21:19'),
(7, 'this is blog6', NULL, 'first-post', 'this is first post', NULL, '2019-08-19 17:21:19'),
(8, 'this is blog7', NULL, 'first-post2', 'this is first post2', NULL, '2019-08-19 17:21:19');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
