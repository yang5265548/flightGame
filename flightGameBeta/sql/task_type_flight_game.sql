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

 Date: 02/11/2023 02:36:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for task_type_flight_game
-- ----------------------------
DROP TABLE IF EXISTS `task_type_flight_game`;
CREATE TABLE `task_type_flight_game`  (
  `task_type_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `bonus_per_km` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `oil_consumption` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`task_type_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of task_type_flight_game
-- ----------------------------
INSERT INTO `task_type_flight_game` VALUES (1, 'A', '50', '150');
INSERT INTO `task_type_flight_game` VALUES (2, 'B', '100', '150');
INSERT INTO `task_type_flight_game` VALUES (3, 'C', '150', '200');
INSERT INTO `task_type_flight_game` VALUES (4, 'D', '200', '250');
INSERT INTO `task_type_flight_game` VALUES (5, 'E', '250', '300');
INSERT INTO `task_type_flight_game` VALUES (6, 'F', '300', '350');
INSERT INTO `task_type_flight_game` VALUES (7, 'G', '350', '400');
INSERT INTO `task_type_flight_game` VALUES (8, 'S', '500', '600');

SET FOREIGN_KEY_CHECKS = 1;
