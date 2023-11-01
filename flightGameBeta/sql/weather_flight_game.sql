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

 Date: 02/11/2023 02:36:55
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for weather_flight_game
-- ----------------------------
DROP TABLE IF EXISTS `weather_flight_game`;
CREATE TABLE `weather_flight_game`  (
  `weather_id` int(11) NOT NULL AUTO_INCREMENT,
  `weather_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `description` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `oil_consumption_rate` double NULL DEFAULT NULL,
  `bonus_per_km_rate` double NULL DEFAULT NULL,
  PRIMARY KEY (`weather_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 9 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of weather_flight_game
-- ----------------------------
INSERT INTO `weather_flight_game` VALUES (1, 'HOT', 'Temperature over +25C', 0.15, 0.15);
INSERT INTO `weather_flight_game` VALUES (2, 'COLD', 'Temperature under -20C', 0.3, 0.3);
INSERT INTO `weather_flight_game` VALUES (3, '0DEG', 'Temperature exactly 0C', 0.2, 0.2);
INSERT INTO `weather_flight_game` VALUES (4, '10DEG', 'Temperature exactly +10C', 0.7, 0.7);
INSERT INTO `weather_flight_game` VALUES (5, '20DEG', 'Temperature exactly +20C', 0, 0);
INSERT INTO `weather_flight_game` VALUES (6, 'CLEAR', 'Clear skies', 0, 0);
INSERT INTO `weather_flight_game` VALUES (7, 'CLOUDS', 'Cloudy', 0.1, 0.1);
INSERT INTO `weather_flight_game` VALUES (8, 'WINDY', 'Wind blows more than 10 m/s', 0.17, 0.17);

SET FOREIGN_KEY_CHECKS = 1;
