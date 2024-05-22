SELECT
	SUBSTRING("River Information", '([0-9]{1,4})') AS river_length
FROM view_river_info;

ALTER VIEW view_river_info
RENAME COLUMN "River information" TO "River Information";