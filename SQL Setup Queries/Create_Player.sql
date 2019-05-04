CREATE TABLE if not exists `Player` (
  	`id` int(11) NOT NULL PRIMARY KEY AUTO_INCREMENT,
  	`first_name` VARCHAR(255) NOT NULL,
    `last_name` VARCHAR(255) NOT NULL,
  	`team` VARCHAR(255),
  	`pos` VARCHAR(10) NOT NULL,
  	`AB` INT(11),
  	`R` INT(11),
  	`H` INT(11),
  	`HR` INT(11),
  	`RBI` INT(11),
  	`SB` INT(11),player
  	`BA` DOUBLE(4,3),
  	`OBP` DOUBLE(4,3),
	`OPS` DOUBLE(4,3),
  	`SLG` DOUBLE(4,3),
	`W` INT(2),
	`L` INT(2),
	`ERA` DOUBLE(10,2),
	`G` INT(3),
	`GS` INT(3),
	`SV` INT(3),
	`IP` DOUBLE(4,1),
	`SO` INT(4),
	`WHIP` DOUBLE(10,2)
);