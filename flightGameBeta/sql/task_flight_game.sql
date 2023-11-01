/*
 Navicat Premium Data Transfer

 Source Server         : yangyangmariaDB
 Source Server Type    : MariaDB
 Source Server Version : 110102
 Source Host           : localhost:6033
 Source Schema         : flight_game

 Target Server Type    : MariaDB
 Target Server Version : 110102
 File Encoding         : 65001

 Date: 02/11/2023 02:36:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for task_flight_game
-- ----------------------------
DROP TABLE IF EXISTS `task_flight_game`;
CREATE TABLE `task_flight_game`  (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NULL DEFAULT NULL,
  `task_type_id` int(11) NULL DEFAULT NULL,
  `weather_id` int(11) NULL DEFAULT NULL,
  `addr_from` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `addr_to` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `is_done` tinyint(1) NULL DEFAULT NULL,
  `task_oil` double NULL DEFAULT NULL,
  `task_bonus` double NULL DEFAULT NULL,
  PRIMARY KEY (`task_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 307 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
