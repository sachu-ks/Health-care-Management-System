-- phpMyAdmin SQL Dump
-- version 4.1.12
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Nov 02, 2022 at 06:58 AM
-- Server version: 5.6.16
-- PHP Version: 5.5.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `campus1`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=53 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add college', 7, 'add_college'),
(26, 'Can change college', 7, 'change_college'),
(27, 'Can delete college', 7, 'delete_college'),
(28, 'Can view college', 7, 'view_college'),
(29, 'Can add event', 8, 'add_event'),
(30, 'Can change event', 8, 'change_event'),
(31, 'Can delete event', 8, 'delete_event'),
(32, 'Can view event', 8, 'view_event'),
(33, 'Can add event_application', 9, 'add_event_application'),
(34, 'Can change event_application', 9, 'change_event_application'),
(35, 'Can delete event_application', 9, 'delete_event_application'),
(36, 'Can view event_application', 9, 'view_event_application'),
(37, 'Can add notification', 10, 'add_notification'),
(38, 'Can change notification', 10, 'change_notification'),
(39, 'Can delete notification', 10, 'delete_notification'),
(40, 'Can view notification', 10, 'view_notification'),
(41, 'Can add student', 11, 'add_student'),
(42, 'Can change student', 11, 'change_student'),
(43, 'Can delete student', 11, 'delete_student'),
(44, 'Can view student', 11, 'view_student'),
(45, 'Can add studymaterial', 12, 'add_studymaterial'),
(46, 'Can change studymaterial', 12, 'change_studymaterial'),
(47, 'Can delete studymaterial', 12, 'delete_studymaterial'),
(48, 'Can view studymaterial', 12, 'view_studymaterial'),
(49, 'Can add userlogin', 13, 'add_userlogin'),
(50, 'Can change userlogin', 13, 'change_userlogin'),
(51, 'Can delete userlogin', 13, 'delete_userlogin'),
(52, 'Can view userlogin', 13, 'view_userlogin');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_college`
--

CREATE TABLE IF NOT EXISTS `campusconnect_college` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `college_name` varchar(150) NOT NULL,
  `c_reg` varchar(150) NOT NULL,
  `c_addr` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `ph_no` varchar(150) NOT NULL,
  `website` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `logo` varchar(150) NOT NULL,
  `image` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `campusconnect_college`
--

INSERT INTO `campusconnect_college` (`id`, `college_name`, `c_reg`, `c_addr`, `email`, `ph_no`, `website`, `password`, `logo`, `image`) VALUES
(1, 'sngc', '3456', 'aluva,cochin', 'sngc@gmail.com', '', '', '1234', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_complaint_tbl`
--

CREATE TABLE IF NOT EXISTS `campusconnect_complaint_tbl` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` varchar(200) NOT NULL,
  `complaint` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `campusconnect_complaint_tbl`
--

INSERT INTO `campusconnect_complaint_tbl` (`id`, `uid`, `complaint`, `date`) VALUES
(1, '3', 'xdcd', '2022-11-09'),
(2, '3', 'ghj', '2022-11-06');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_event`
--

CREATE TABLE IF NOT EXISTS `campusconnect_event` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `college_name` varchar(150) NOT NULL,
  `event_name` varchar(150) NOT NULL,
  `event_desc` varchar(150) NOT NULL,
  `event_photo` varchar(150) NOT NULL,
  `start_date` varchar(150) NOT NULL,
  `end_date` varchar(150) NOT NULL,
  `venue` varchar(150) NOT NULL,
  `amount` varchar(150) NOT NULL,
  `seat` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `campusconnect_event`
--

INSERT INTO `campusconnect_event` (`id`, `college_name`, `event_name`, `event_desc`, `event_photo`, `start_date`, `end_date`, `venue`, `amount`, `seat`) VALUES
(1, '1', 'christmas', 'christmas', 'images_QImvZ44.png', '2022-12-29', '2022-12-27', 'sngc college', '50', '100');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_event_application`
--

CREATE TABLE IF NOT EXISTS `campusconnect_event_application` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `event_id` varchar(150) NOT NULL,
  `student_id` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  `result` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_notification`
--

CREATE TABLE IF NOT EXISTS `campusconnect_notification` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file` varchar(150) NOT NULL,
  `description` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `campusconnect_notification`
--

INSERT INTO `campusconnect_notification` (`id`, `file`, `description`, `date`) VALUES
(1, 'images_Kw50iF7.png', 'informtaions', '2022-10-31'),
(2, 'images_Kw50iF7.png', 'saxsdc', '2022-10-31');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_student`
--

CREATE TABLE IF NOT EXISTS `campusconnect_student` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `student_name` varchar(150) NOT NULL,
  `s_address` varchar(150) NOT NULL,
  `reg_no` varchar(150) NOT NULL,
  `email` varchar(150) NOT NULL,
  `ph_no` varchar(150) NOT NULL,
  `photo` varchar(150) NOT NULL,
  `college_id` varchar(150) NOT NULL,
  `dept` varchar(150) NOT NULL,
  `password` varchar(150) NOT NULL,
  `semester` varchar(150) NOT NULL,
  `sex` varchar(150) NOT NULL,
  `age` varchar(150) NOT NULL,
  `course` varchar(150) NOT NULL,
  `year_of_pass` varchar(150) NOT NULL,
  `year_of_join` varchar(150) NOT NULL,
  `status` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `campusconnect_student`
--

INSERT INTO `campusconnect_student` (`id`, `student_name`, `s_address`, `reg_no`, `email`, `ph_no`, `photo`, `college_id`, `dept`, `password`, `semester`, `sex`, `age`, `course`, `year_of_pass`, `year_of_join`, `status`) VALUES
(1, 'anoop', 'kollam', '123456', 'anoop@gmail.com', '7689776622', 'images_Kw50iF7 (1).png', '', '', '12345', '', 'male', '24', '', '', '', ''),
(3, 'anoop', '', '123456', 'anu@gmail.com', '', '', '1', 'computer', '123', '1', '', '', 'bca', '2019', '2016', '');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_studymaterial`
--

CREATE TABLE IF NOT EXISTS `campusconnect_studymaterial` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `file` varchar(150) NOT NULL,
  `student_name` varchar(150) NOT NULL,
  `course` varchar(150) NOT NULL,
  `semester` varchar(150) NOT NULL,
  `date` varchar(150) NOT NULL,
  `subject` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumping data for table `campusconnect_studymaterial`
--

INSERT INTO `campusconnect_studymaterial` (`id`, `file`, `student_name`, `course`, `semester`, `date`, `subject`) VALUES
(1, 'images_Kw50iF7 (1)_jzSYFUq.png', '1', '', '', '2022-10-02', 'sdsd'),
(2, 'images_Kw50iF7 (1)_9BK2Ww1.png', '1', '', '', '2022-10-02', 'sdsd'),
(3, 'images_Kw50iF7 (1)_y3XSNTN.png', '1', '', '', '2022-10-09', 'szx'),
(4, 'a5.jpg', '2', 'bca', '1', '2022-11-15', 'dcdxc'),
(5, 'a1.jpg', '3', 'bca', '1', '2022-11-02', 'sdsd'),
(6, 'a1_IaSIPfj.jpg', '3', 'bca', '1', '2022-11-02', 'sdsd');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_tbl_post`
--

CREATE TABLE IF NOT EXISTS `campusconnect_tbl_post` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject` varchar(200) NOT NULL,
  `date` varchar(225) NOT NULL,
  `post` varchar(225) NOT NULL,
  `sid` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=16 ;

--
-- Dumping data for table `campusconnect_tbl_post`
--

INSERT INTO `campusconnect_tbl_post` (`id`, `subject`, `date`, `post`, `sid`) VALUES
(1, 'dfd', '2022-11-09', '6.jpg', '2'),
(2, 'dfd', '2022-11-09', '6_SAqDyRu.jpg', '2'),
(3, 'sf', '2022-11-10', 'logo.png', '3'),
(4, 'sf', '2022-11-10', 'logo_fVejePM.png', '3'),
(5, 'sf', '2022-11-10', 'logo_ABcc2J2.png', '3'),
(6, 'sf', '2022-11-10', 'logo_TS4w72z.png', '3'),
(7, 'sf', '2022-11-10', 'logo_ETLriTd.png', '3'),
(8, 'sfd', '2022-11-15', 'logo11.png', '3'),
(9, 'sfd', '2022-11-15', 'logo11_Awv6Ns4.png', '3'),
(10, 'sfd', '2022-11-15', 'logo11_7LVD3YJ.png', '3'),
(11, 'sfd', '2022-11-15', 'logo11_3pQ2hnm.png', '3'),
(12, 'sfd', '2022-11-15', 'logo11_r4EBLcq.png', '3'),
(13, 'sfd', '2022-11-15', 'logo11_yYRCDHX.png', '3'),
(14, 'sfd', '2022-11-15', 'logo11_iuNGdyt.png', '3'),
(15, 'sfd', '2022-11-15', 'logo11_KNi5QZA.png', '3');

-- --------------------------------------------------------

--
-- Table structure for table `campusconnect_userlogin`
--

CREATE TABLE IF NOT EXISTS `campusconnect_userlogin` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `email` varchar(150) NOT NULL,
  `passwd` varchar(150) NOT NULL,
  `category` varchar(150) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=6 ;

--
-- Dumping data for table `campusconnect_userlogin`
--

INSERT INTO `campusconnect_userlogin` (`id`, `email`, `passwd`, `category`) VALUES
(1, 'sngc@gmail.com', '1234', 'college'),
(2, 'anoop@gmail.com', '12345', 'student'),
(3, '', '', 'student'),
(4, 'anu@gmail.com', '123', 'student'),
(5, 'anu@gmail.com', '123', 'student');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=14 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(7, 'campusconnect', 'college'),
(8, 'campusconnect', 'event'),
(9, 'campusconnect', 'event_application'),
(10, 'campusconnect', 'notification'),
(11, 'campusconnect', 'student'),
(12, 'campusconnect', 'studymaterial'),
(13, 'campusconnect', 'userlogin'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=20 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-10-31 04:27:25.533256'),
(2, 'auth', '0001_initial', '2022-10-31 04:27:27.155361'),
(3, 'admin', '0001_initial', '2022-10-31 04:27:27.524022'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-10-31 04:27:27.540228'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-10-31 04:27:27.554436'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-10-31 04:27:27.760648'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-10-31 04:27:27.909300'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-10-31 04:27:28.027472'),
(9, 'auth', '0004_alter_user_username_opts', '2022-10-31 04:27:28.050449'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-10-31 04:27:28.132792'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-10-31 04:27:28.144728'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-10-31 04:27:28.170445'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-10-31 04:27:28.283183'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-10-31 04:27:28.392809'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-10-31 04:27:28.517240'),
(16, 'auth', '0011_update_proxy_permissions', '2022-10-31 04:27:28.543193'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-10-31 04:27:28.641636'),
(18, 'campusconnect', '0001_initial', '2022-10-31 04:27:29.648266'),
(19, 'sessions', '0001_initial', '2022-10-31 04:27:29.819544');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('sduufh5harmhdxofassv9zajsvajr2i1', 'e30:1opNBl:y9OU31BL95C1WL6DWssj9luUeA9zrPnu6r0-e1gKbdI', '2022-11-14 05:18:21.021119'),
('ucx3hdt6y054a0xjo4obxupqtg8fhafy', 'eyJzdHVkZW50X2lkIjozfQ:1oq5uv:8Q3M0qGj8da9lx_DwA_m_Kd2PfzGaLrjh29xK1SQTJg', '2022-11-16 05:03:57.311211');

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
