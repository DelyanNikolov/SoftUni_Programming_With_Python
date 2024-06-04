SELECT
	COUNT(*)
FROM
	countries as c
LEFT JOIN
	mountains_countries as mc
USING
	(country_code)
WHERE
	mc.mountain_id is NULL;