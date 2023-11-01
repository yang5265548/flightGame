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

 Date: 02/11/2023 02:36:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for user_airplane_flight_game
-- ----------------------------
DROP TABLE IF EXISTS `user_airplane_flight_game`;
CREATE TABLE `user_airplane_flight_game`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NULL DEFAULT NULL,
  `airplane_type_id` int(11) NULL DEFAULT NULL,
  `current_fuel_capacity` double NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 42 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
