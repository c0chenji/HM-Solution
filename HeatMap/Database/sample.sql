-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Sep 23, 2020 at 07:51 PM
-- Server version: 5.6.17
-- PHP Version: 5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `sample`
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=45 ;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add camera', 1, 'add_camera'),
(2, 'Can change camera', 1, 'change_camera'),
(3, 'Can delete camera', 1, 'delete_camera'),
(4, 'Can view camera', 1, 'view_camera'),
(5, 'Can add channel', 2, 'add_channel'),
(6, 'Can change channel', 2, 'change_channel'),
(7, 'Can delete channel', 2, 'delete_channel'),
(8, 'Can view channel', 2, 'view_channel'),
(9, 'Can add frame', 3, 'add_frame'),
(10, 'Can change frame', 3, 'change_frame'),
(11, 'Can delete frame', 3, 'delete_frame'),
(12, 'Can view frame', 3, 'view_frame'),
(13, 'Can add heatmap', 4, 'add_heatmap'),
(14, 'Can change heatmap', 4, 'change_heatmap'),
(15, 'Can delete heatmap', 4, 'delete_heatmap'),
(16, 'Can view heatmap', 4, 'view_heatmap'),
(17, 'Can add direction', 5, 'add_direction'),
(18, 'Can change direction', 5, 'change_direction'),
(19, 'Can delete direction', 5, 'delete_direction'),
(20, 'Can view direction', 5, 'view_direction'),
(21, 'Can add log entry', 6, 'add_logentry'),
(22, 'Can change log entry', 6, 'change_logentry'),
(23, 'Can delete log entry', 6, 'delete_logentry'),
(24, 'Can view log entry', 6, 'view_logentry'),
(25, 'Can add permission', 7, 'add_permission'),
(26, 'Can change permission', 7, 'change_permission'),
(27, 'Can delete permission', 7, 'delete_permission'),
(28, 'Can view permission', 7, 'view_permission'),
(29, 'Can add group', 8, 'add_group'),
(30, 'Can change group', 8, 'change_group'),
(31, 'Can delete group', 8, 'delete_group'),
(32, 'Can view group', 8, 'view_group'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add content type', 10, 'add_contenttype'),
(38, 'Can change content type', 10, 'change_contenttype'),
(39, 'Can delete content type', 10, 'delete_contenttype'),
(40, 'Can view content type', 10, 'view_contenttype'),
(41, 'Can add session', 11, 'add_session'),
(42, 'Can change session', 11, 'change_session'),
(43, 'Can delete session', 11, 'delete_session'),
(44, 'Can view session', 11, 'view_session');

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
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$EiurRJwC7mVN$75CXMm6cy1IDO7PDHKhcY34TmktRH+vTwUIiSaeTLpA=', '2020-09-18 16:33:12.773115', 1, 'admin', '', '', 'jeff@facialstats.com', 1, 1, '2020-09-11 15:40:40.319117');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
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
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2020-09-11 15:42:34.801665', '1', 'Camera object (1)', 1, '[{"added": {}}]', 1, 1),
(2, '2020-09-11 15:46:26.300906', '2', 'Camera object (2)', 1, '[{"added": {}}]', 1, 1);

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
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=12 ;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'admin', 'logentry'),
(8, 'auth', 'group'),
(7, 'auth', 'permission'),
(9, 'auth', 'user'),
(10, 'contenttypes', 'contenttype'),
(1, 'Interface', 'camera'),
(2, 'Interface', 'channel'),
(5, 'Interface', 'direction'),
(3, 'Interface', 'frame'),
(4, 'Interface', 'heatmap'),
(11, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=29 ;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-09-11 15:38:55.824140'),
(2, 'auth', '0001_initial', '2020-09-11 15:38:59.558353'),
(3, 'Interface', '0001_initial', '2020-09-11 15:39:14.749222'),
(4, 'Interface', '0002_auto_20200511_0411', '2020-09-11 15:39:18.441433'),
(5, 'Interface', '0003_auto_20200511_0432', '2020-09-11 15:39:20.799568'),
(6, 'Interface', '0004_delete_channel', '2020-09-11 15:39:21.294597'),
(7, 'Interface', '0005_channeldetail', '2020-09-11 15:39:22.166646'),
(8, 'Interface', '0006_auto_20200511_1127', '2020-09-11 15:39:26.021867'),
(9, 'Interface', '0007_auto_20200811_1741', '2020-09-11 15:39:28.675019'),
(10, 'Interface', '0008_auto_20200812_1444', '2020-09-11 15:39:34.105329'),
(11, 'Interface', '0009_channel_directions', '2020-09-11 15:39:35.367402'),
(12, 'Interface', '0010_direction', '2020-09-11 15:39:36.297455'),
(13, 'Interface', '0011_auto_20200910_1553', '2020-09-11 15:39:41.108730'),
(14, 'admin', '0001_initial', '2020-09-11 15:39:41.800769'),
(15, 'admin', '0002_logentry_remove_auto_add', '2020-09-11 15:39:44.968951'),
(16, 'admin', '0003_logentry_add_action_flag_choices', '2020-09-11 15:39:45.104958'),
(17, 'contenttypes', '0002_remove_content_type_name', '2020-09-11 15:39:47.497095'),
(18, 'auth', '0002_alter_permission_name_max_length', '2020-09-11 15:39:49.163191'),
(19, 'auth', '0003_alter_user_email_max_length', '2020-09-11 15:39:50.826286'),
(20, 'auth', '0004_alter_user_username_opts', '2020-09-11 15:39:50.992295'),
(21, 'auth', '0005_alter_user_last_login_null', '2020-09-11 15:39:52.050356'),
(22, 'auth', '0006_require_contenttypes_0002', '2020-09-11 15:39:52.178363'),
(23, 'auth', '0007_alter_validators_add_error_messages', '2020-09-11 15:39:52.320371'),
(24, 'auth', '0008_alter_user_username_max_length', '2020-09-11 15:39:53.989467'),
(25, 'auth', '0009_alter_user_last_name_max_length', '2020-09-11 15:39:55.743567'),
(26, 'auth', '0010_alter_group_name_max_length', '2020-09-11 15:39:57.389661'),
(27, 'auth', '0011_update_proxy_permissions', '2020-09-11 15:39:57.541670'),
(28, 'sessions', '0001_initial', '2020-09-11 15:39:58.192707');

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
('h1zo6bo7irqndcikv22wp9v5ayt5gn2r', 'MTcyMWY5MzBhZDc5ODgyNTFlNzAyNjk3Zjc2NDU3M2VkNjU4ZGE2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZmRlY2M4NDNhMDBhNjI0ZGJjOGI3MDhhNTMxZGMzNzRjNDg2OWJmIn0=', '2020-09-25 20:14:48.757515'),
('q1jhk90nihevdpcyaw0tlm8dlya8kbxu', 'MTcyMWY5MzBhZDc5ODgyNTFlNzAyNjk3Zjc2NDU3M2VkNjU4ZGE2Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4ZmRlY2M4NDNhMDBhNjI0ZGJjOGI3MDhhNTMxZGMzNzRjNDg2OWJmIn0=', '2020-10-02 16:33:12.951125');

-- --------------------------------------------------------

--
-- Table structure for table `interface_camera`
--

CREATE TABLE IF NOT EXISTS `interface_camera` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `camera_model` varchar(40) NOT NULL,
  `rtsp_url` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Interface_camera_camera_model_a9313cbd_uniq` (`camera_model`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `interface_camera`
--

INSERT INTO `interface_camera` (`id`, `camera_model`, `rtsp_url`) VALUES
(1, 'axis', '/axis-media/media.amp'),
(2, 'axis1', ':89/mjpg/video.mjpg'),
(3, 'Axis3', ':8000/mjpg/video.mjpg');

-- --------------------------------------------------------

--
-- Table structure for table `interface_channel`
--

CREATE TABLE IF NOT EXISTS `interface_channel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(128) NOT NULL,
  `password` varchar(128) NOT NULL,
  `IP` varchar(15) NOT NULL,
  `portNum` varchar(5) NOT NULL,
  `cameraNum` varchar(3) NOT NULL,
  `description` varchar(255) NOT NULL,
  `enabled` tinyint(1) NOT NULL,
  `coordinates` varchar(1200) NOT NULL,
  `names` varchar(600) NOT NULL,
  `camera_id` int(11) NOT NULL,
  `directions` varchar(600) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `IP` (`IP`),
  UNIQUE KEY `description` (`description`),
  KEY `Interface_channel_camera_id_1a053820_fk_Interface_camera_id` (`camera_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=23 ;

--
-- Dumping data for table `interface_channel`
--

INSERT INTO `interface_channel` (`id`, `username`, `password`, `IP`, `portNum`, `cameraNum`, `description`, `enabled`, `coordinates`, `names`, `camera_id`, `directions`) VALUES
(1, 'Jeff', '123', '184.68.127.82', '1', '1', 'GolfCourt', 0, '[{"points":[[102,59],[123,245],[442,248],[433,60],[102,59]],"done":true,"center":{"x":275,"y":152},"zoneName":"zone 1"},{"points":[[478,53],[484,251],[661,249],[671,49],[478,53]],"done":true,"center":{"x":574,"y":149},"zoneName":"zone 3"},{"points":[[230,273],[235,467],[614,464],[619,279],[230,273]],"done":true,"center":{"x":423,"y":370},"zoneName":"zone 2"}]', '[]', 2, '[[[40,224],[368,163]],[[36,255],[389,382]],[[38,236],[599,173]]]'),
(2, 'Jeff', '123', '142.112.65.17', '1', '1', 'Port', 0, '[{"points":[[111,161],[37,281],[224,370],[321,291],[111,161]],"done":true,"center":{"x":171,"y":272},"zoneName":"main zone"}]', '[]', 2, '[[[35,319],[260,212]],[[41,343],[286,279]],[[23,252],[164,210]]]'),
(20, 'juli', '123', '', '2', '1', '12312312', 0, '', '', 1, ''),
(21, 'test', '123', '142.177.82.43', '1', '1', 'newPort', 0, '[{"points":[[127,132],[51,250],[95,388],[281,406],[331,299],[321,161],[127,132]],"done":true,"center":{"x":198,"y":270},"zoneName":"zone 1"},{"points":[[461,79],[371,273],[404,410],[596,424],[665,337],[698,157],[461,79]],"done":true,"center":{"x":531,"y":262},"zoneName":"zone 2"}]', '[]', 1, '[[[39,184],[255,233]],[[80,435],[584,268]]]'),
(22, 'ak', '123', '162.17.212.89', '1', '1', 'beach', 1, '[{"points":[[86,217],[93,450],[374,451],[381,202],[86,217]],"done":true,"center":{"x":235,"y":329},"zoneName":"zone 1"},{"points":[[463,114],[460,298],[647,284],[657,118],[463,114]],"done":true,"center":{"x":555,"y":203},"zoneName":"zone 2"}]', '[]', 3, '[[[23,358],[240,317]],[[242,397],[340,241]],[[100,272],[216,214]]]');

-- --------------------------------------------------------

--
-- Table structure for table `interface_direction`
--

CREATE TABLE IF NOT EXISTS `interface_direction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topColor` varchar(255) NOT NULL,
  `bottomColor` varchar(255) NOT NULL,
  `topLeftX` int(11) NOT NULL,
  `topLeftY` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `direction` varchar(648) NOT NULL,
  `frame_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Interface_direction_frame_id_e48c3113_fk_Interface_frame_id` (`frame_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- Table structure for table `interface_frame`
--

CREATE TABLE IF NOT EXISTS `interface_frame` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img_name` varchar(40) NOT NULL,
  `captureTime` datetime(6) NOT NULL,
  `channel_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Interface_frame_channel_id_8e921a2f_fk_Interface_channel_id` (`channel_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=826 ;

--
-- Dumping data for table `interface_frame`
--

INSERT INTO `interface_frame` (`id`, `img_name`, `captureTime`, `channel_id`) VALUES
(708, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:04.427536', 22),
(709, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:04.669550', 22),
(710, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:05.143577', 22),
(711, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:09.393820', 22),
(712, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:21.896535', 22),
(713, '24bfd52e-6db1-49a5-a832-f7ea8fceb7bf.jpg', '2020-09-23 16:15:22.150550', 22),
(714, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:17:49.881000', 22),
(715, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:17:50.141015', 22),
(716, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:03.246764', 22),
(717, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:07.693018', 22),
(718, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:16.107500', 22),
(719, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:20.945776', 22),
(720, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:35.242594', 22),
(721, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:41.927977', 22),
(722, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:48.067328', 22),
(723, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:48.407347', 22),
(724, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:54.643704', 22),
(725, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:18:55.096730', 22),
(726, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:00.963065', 22),
(727, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:05.838344', 22),
(728, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:06.108360', 22),
(729, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:11.305657', 22),
(730, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:11.526670', 22),
(731, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:20.442179', 22),
(732, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:20.690194', 22),
(733, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:28.971667', 22),
(734, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:40.143306', 22),
(735, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:47.905750', 22),
(736, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:53.987098', 22),
(737, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:54.748142', 22),
(738, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:55.385178', 22),
(739, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:19:55.700196', 22),
(740, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:00.768486', 22),
(741, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:01.006500', 22),
(742, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:05.276744', 22),
(743, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:10.025015', 22),
(744, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:14.573276', 22),
(745, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:14.776287', 22),
(746, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:15.030302', 22),
(747, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:23.157767', 22),
(748, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:23.605792', 22),
(749, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:32.168282', 22),
(750, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:36.714542', 22),
(751, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:36.943555', 22),
(752, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:41.424811', 22),
(753, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:54.204542', 22),
(754, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:54.552562', 22),
(755, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:54.780575', 22),
(756, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:55.022589', 22),
(757, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:55.452614', 22),
(758, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:20:59.208829', 22),
(759, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:02.119995', 22),
(760, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:02.765032', 22),
(761, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:03.008046', 22),
(762, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:03.255060', 22),
(763, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:03.491074', 22),
(764, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:03.736088', 22),
(765, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:08.849380', 22),
(766, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:09.192400', 22),
(767, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:09.644425', 22),
(768, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:09.884439', 22),
(769, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:20.817065', 22),
(770, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:21.154084', 22),
(771, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:21.376096', 22),
(772, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:21.613110', 22),
(773, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:21.848123', 22),
(774, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:26.997418', 22),
(775, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:27.231431', 22),
(776, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:36.598967', 22),
(777, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:37.168000', 22),
(778, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:37.496018', 22),
(779, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:37.728032', 22),
(780, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:41.634255', 22),
(781, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:49.228690', 22),
(782, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:21:56.892128', 22),
(783, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:15.306181', 22),
(784, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:15.554195', 22),
(785, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:15.801209', 22),
(786, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:20.462476', 22),
(787, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:20.725491', 22),
(788, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:29.951019', 22),
(789, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:35.099313', 22),
(790, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:35.332327', 22),
(791, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:35.579341', 22),
(792, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:41.698691', 22),
(793, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:41.934704', 22),
(794, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:42.550739', 22),
(795, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:42.809754', 22),
(796, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:51.793268', 22),
(797, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:51.998280', 22),
(798, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:52.214292', 22),
(799, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:52.480307', 22),
(800, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:22:56.357529', 22),
(801, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:01.477822', 22),
(802, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:01.732837', 22),
(803, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:01.966850', 22),
(804, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:07.051141', 22),
(805, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:07.275154', 22),
(806, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:07.490166', 22),
(807, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:08.062199', 22),
(808, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:16.833700', 22),
(809, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:17.065714', 22),
(810, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:35.904791', 22),
(811, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:38.812957', 22),
(812, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:48.843531', 22),
(813, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:49.085545', 22),
(814, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:49.315558', 22),
(815, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:49.545571', 22),
(816, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:49.773584', 22),
(817, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:56.529971', 22),
(818, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:56.817987', 22),
(819, '56b365a8-3589-41cf-b46e-05dc8399672f.jpg', '2020-09-23 16:23:57.425022', 22),
(820, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:35.399421', 22),
(821, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:35.968453', 22),
(822, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:43.941909', 22),
(823, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:44.399936', 22),
(824, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:47.890135', 22),
(825, '3f2bd082-9995-48aa-88b8-ecc16a831d82.jpg', '2020-09-23 16:50:51.608348', 22);

-- --------------------------------------------------------

--
-- Table structure for table `interface_heatmap`
--

CREATE TABLE IF NOT EXISTS `interface_heatmap` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `topColor` varchar(255) NOT NULL,
  `bottomColor` varchar(255) NOT NULL,
  `topLeftX` int(11) NOT NULL,
  `topLeftY` int(11) NOT NULL,
  `width` int(11) NOT NULL,
  `height` int(11) NOT NULL,
  `dwellingTime` int(11) NOT NULL,
  `zoneArea` int(11) NOT NULL,
  `frame_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Interface_heatmap_frame_id_8d50644e_fk_Interface_frame_id` (`frame_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=723 ;

--
-- Dumping data for table `interface_heatmap`
--

INSERT INTO `interface_heatmap` (`id`, `topColor`, `bottomColor`, `topLeftX`, `topLeftY`, `width`, `height`, `dwellingTime`, `zoneArea`, `frame_id`) VALUES
(605, 'white', 'white', 302, 330, 35, 70, 4, 0, 708),
(606, 'black', 'red', 85, 324, 21, 28, 4, 0, 709),
(607, 'white', 'white', 299, 228, 18, 39, 5, 0, 710),
(608, 'yellow', 'white', 158, 263, 11, 41, 3, 0, 711),
(609, 'red', 'black', 526, 264, 25, 32, 4, 1, 712),
(610, 'black', 'black', 525, 218, 22, 30, 4, 1, 713),
(611, 'black', 'red', 561, 216, 15, 36, 4, 1, 714),
(612, 'white', 'yellow', 564, 205, 43, 29, 4, 1, 715),
(613, 'red', 'red', 147, 399, 36, 51, 9, 0, 716),
(614, 'black', 'red', 522, 225, 22, 46, 13, 1, 717),
(615, 'red', 'white', 469, 255, 18, 26, 30, 1, 718),
(616, 'white', 'white', 540, 266, 13, 26, 4, 1, 719),
(617, 'black', 'black', 635, 232, 10, 29, 10, 1, 720),
(618, 'white', 'white', 229, 399, 37, 52, 6, 0, 721),
(619, 'white', 'white', 203, 265, 34, 58, 18, 0, 722),
(620, 'white', 'white', 125, 263, 25, 29, 8, 0, 723),
(621, 'white', 'white', 340, 219, 19, 38, 14, 0, 724),
(622, 'white', 'white', 371, 224, 12, 42, 5, 0, 725),
(623, 'black', 'black', 632, 210, 18, 22, 36, 1, 726),
(624, 'red', 'black', 591, 218, 20, 33, 16, 1, 727),
(625, 'white', 'white', 490, 194, 19, 28, 4, 1, 728),
(626, 'red', 'red', 605, 201, 23, 36, 67, 1, 729),
(627, 'white', 'white', 576, 202, 20, 22, 60, 1, 730),
(628, 'white', 'white', 575, 203, 21, 22, 13, 1, 731),
(629, 'black', 'black', 628, 194, 19, 24, 8, 1, 732),
(630, 'white', 'red', 600, 194, 22, 33, 13, 1, 733),
(631, 'white', 'white', 337, 314, 30, 63, 5, 0, 734),
(632, 'white', 'white', 308, 253, 17, 38, 8, 0, 735),
(633, 'red', 'white', 572, 204, 22, 22, 24, 1, 736),
(634, 'white', 'white', 198, 270, 23, 61, 15, 0, 737),
(635, 'white', 'white', 190, 258, 19, 62, 8, 0, 738),
(636, 'red', 'red', 483, 188, 28, 22, 8, 1, 739),
(637, 'red', 'black', 599, 203, 23, 25, 48, 1, 740),
(638, 'red', 'red', 600, 216, 23, 25, 21, 1, 741),
(639, 'red', 'red', 352, 229, 16, 43, 30, 0, 742),
(640, 'white', 'black', 454, 197, 23, 16, 8, 1, 743),
(641, 'white', 'red', 468, 255, 20, 26, 143, 1, 744),
(642, 'white', 'white', 451, 193, 30, 25, 9, 1, 745),
(643, 'white', 'red', 575, 203, 21, 22, 5, 1, 746),
(644, 'red', 'red', 619, 203, 16, 36, 13, 1, 747),
(645, 'red', 'white', 570, 207, 22, 22, 5, 1, 748),
(646, 'red', 'red', 596, 204, 30, 36, 13, 1, 749),
(647, 'red', 'white', 623, 177, 32, 22, 72, 1, 750),
(648, 'red', 'black', 469, 255, 18, 26, 18, 1, 751),
(649, 'white', 'yellow', 581, 205, 23, 39, 14, 1, 752),
(650, 'yellow', 'red', 516, 195, 21, 16, 26, 1, 753),
(651, 'white', 'white', 300, 241, 18, 40, 13, 0, 754),
(652, 'yellow', 'yellow', 563, 237, 15, 26, 8, 1, 755),
(653, 'red', 'black', 600, 202, 20, 25, 8, 1, 756),
(654, 'red', 'white', 626, 177, 22, 27, 8, 1, 757),
(655, 'yellow', 'red', 178, 252, 28, 52, 26, 0, 758),
(656, 'red', 'white', 496, 239, 20, 54, 196, 1, 759),
(657, 'white', 'red', 599, 207, 22, 62, 22, 1, 760),
(658, 'white', 'white', 242, 253, 20, 51, 22, 0, 761),
(659, 'black', 'red', 487, 216, 15, 29, 16, 1, 762),
(660, 'white', 'white', 279, 382, 40, 31, 7, 0, 763),
(661, 'white', 'white', 285, 343, 27, 39, 7, 0, 764),
(662, 'white', 'red', 505, 233, 37, 56, 31, 1, 765),
(663, 'white', 'white', 158, 275, 17, 55, 13, 0, 766),
(664, 'white', 'white', 132, 266, 18, 27, 9, 0, 767),
(665, 'white', 'white', 105, 265, 21, 27, 5, 0, 768),
(666, 'white', 'white', 451, 268, 20, 29, 40, 1, 769),
(667, 'red', 'yellow', 603, 173, 47, 31, 17, 1, 770),
(668, 'yellow', 'white', 127, 255, 44, 64, 17, 0, 771),
(669, 'black', 'yellow', 297, 291, 25, 46, 7, 0, 772),
(670, 'white', 'white', 84, 259, 41, 35, 7, 0, 773),
(671, 'yellow', 'yellow', 363, 327, 15, 59, 12, 0, 774),
(672, 'yellow', 'red', 154, 401, 55, 52, 4, 0, 775),
(673, 'red', 'red', 576, 184, 60, 41, 26, 1, 776),
(674, 'white', 'white', 239, 384, 28, 67, 22, 0, 777),
(675, 'black', 'black', 615, 219, 20, 25, 15, 1, 778),
(676, 'red', 'yellow', 116, 413, 37, 37, 6, 0, 779),
(677, 'white', 'red', 166, 417, 32, 33, 10, 0, 780),
(678, 'black', 'black', 627, 209, 25, 25, 7, 1, 781),
(679, 'red', 'red', 599, 202, 23, 26, 70, 1, 782),
(680, 'red', 'black', 466, 255, 19, 25, 61, 1, 783),
(681, 'black', 'black', 510, 249, 19, 47, 26, 1, 784),
(682, 'red', 'red', 571, 203, 24, 26, 5, 1, 785),
(683, 'yellow', 'white', 628, 174, 23, 30, 18, 1, 786),
(684, 'white', 'white', 335, 233, 35, 47, 10, 0, 787),
(685, 'white', 'yellow', 330, 318, 21, 55, 5, 0, 788),
(686, 'white', 'yellow', 257, 360, 34, 95, 289, 0, 789),
(687, 'black', 'white', 512, 229, 15, 33, 14, 1, 790),
(688, 'red', 'red', 503, 194, 19, 20, 6, 1, 791),
(689, 'white', 'red', 484, 248, 17, 53, 20, 1, 792),
(690, 'red', 'red', 546, 248, 15, 28, 17, 1, 793),
(691, 'yellow', 'yellow', 219, 425, 19, 26, 13, 0, 794),
(692, 'white', 'white', 283, 233, 21, 44, 6, 0, 795),
(693, 'white', 'white', 457, 264, 11, 33, 101, 1, 796),
(694, 'red', 'red', 516, 195, 22, 16, 63, 1, 797),
(695, 'white', 'red', 529, 282, 21, 30, 16, 1, 798),
(696, 'white', 'yellow', 469, 255, 19, 25, 5, 1, 799),
(697, 'black', 'black', 626, 229, 31, 38, 9, 1, 800),
(698, 'white', 'red', 469, 255, 19, 26, 5, 1, 801),
(699, 'white', 'yellow', 457, 205, 32, 27, 6, 1, 802),
(700, 'red', 'red', 570, 203, 21, 22, 6, 1, 803),
(701, 'white', 'white', 354, 369, 26, 32, 11, 0, 804),
(702, 'yellow', 'white', 339, 405, 15, 35, 4, 0, 805),
(703, 'white', 'white', 239, 363, 28, 44, 5, 0, 806),
(704, 'white', 'yellow', 243, 368, 43, 89, 5, 0, 807),
(705, 'yellow', 'red', 87, 297, 32, 18, 5, 0, 808),
(706, 'white', 'red', 468, 255, 19, 26, 5, 1, 809),
(707, 'red', 'black', 525, 220, 20, 38, 24, 1, 810),
(708, 'red', 'yellow', 239, 239, 18, 42, 14, 0, 811),
(709, 'black', 'white', 505, 246, 26, 57, 65, 1, 812),
(710, 'white', 'white', 242, 238, 12, 29, 24, 0, 813),
(711, 'white', 'red', 468, 255, 19, 26, 19, 1, 814),
(712, 'white', 'white', 173, 244, 14, 30, 8, 0, 815),
(713, 'white', 'white', 568, 207, 21, 22, 8, 1, 816),
(714, 'red', 'red', 610, 220, 23, 21, 31, 1, 817),
(715, 'white', 'white', 84, 262, 17, 35, 6, 0, 818),
(716, 'white', 'white', 100, 260, 24, 33, 6, 0, 819),
(717, 'black', 'red', 611, 231, 20, 39, 3, 1, 820),
(718, 'red', 'red', 525, 226, 19, 37, 4, 1, 821),
(719, 'black', 'black', 615, 248, 20, 28, 12, 1, 822),
(720, 'black', 'black', 600, 234, 13, 28, 7, 1, 823),
(721, 'black', 'red', 588, 221, 17, 30, 19, 1, 824),
(722, 'red', 'red', 580, 203, 66, 69, 19, 1, 825);

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

--
-- Constraints for table `interface_channel`
--
ALTER TABLE `interface_channel`
  ADD CONSTRAINT `Interface_channel_camera_id_1a053820_fk_Interface_camera_id` FOREIGN KEY (`camera_id`) REFERENCES `interface_camera` (`id`);

--
-- Constraints for table `interface_direction`
--
ALTER TABLE `interface_direction`
  ADD CONSTRAINT `Interface_direction_frame_id_e48c3113_fk_Interface_frame_id` FOREIGN KEY (`frame_id`) REFERENCES `interface_frame` (`id`);

--
-- Constraints for table `interface_frame`
--
ALTER TABLE `interface_frame`
  ADD CONSTRAINT `Interface_frame_channel_id_8e921a2f_fk_Interface_channel_id` FOREIGN KEY (`channel_id`) REFERENCES `interface_channel` (`id`);

--
-- Constraints for table `interface_heatmap`
--
ALTER TABLE `interface_heatmap`
  ADD CONSTRAINT `Interface_heatmap_frame_id_8d50644e_fk_Interface_frame_id` FOREIGN KEY (`frame_id`) REFERENCES `interface_frame` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
