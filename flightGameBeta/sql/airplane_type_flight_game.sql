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

 Date: 02/11/2023 02:35:33
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for airplane_type_flight_game
-- ----------------------------
DROP TABLE IF EXISTS `airplane_type_flight_game`;
CREATE TABLE `airplane_type_flight_game`  (
  `airplane_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `airplane_type` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `fuel_tank_capacity` double NULL DEFAULT NULL,
  PRIMARY KEY (`airplane_type_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of airplane_type_flight_game
-- ----------------------------
INSERT INTO `airplane_type_flight_game` VALUES (0, 'A', 10000000);

SET FOREIGN_KEY_CHECKS = 1;
