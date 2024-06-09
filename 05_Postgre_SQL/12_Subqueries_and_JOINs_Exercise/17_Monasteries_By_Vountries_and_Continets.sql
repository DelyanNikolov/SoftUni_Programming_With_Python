UPDATE
	countries
SET
	country_name = 'Burma'
WHERE
	country_name = 'Myanmar';

INSERT INTO monasteries (monastery_name, country_code)
VALUES
	('Hanga Abbey', (SELECT
		country_code
	FROM
		countries
	WHERE
	country_name = 'Tanzania')
	);

SELECT
	c.continent_name,
	cou.country_name,
	COUNT(m.monastery_name) AS monasteries_count
FROM
	continents as c
LEFT JOIN
	countries as cou
USING
	(continent_code)
LEFT JOIN
	monasteries as m
ON
	cou.country_code = m.country_code
WHERE
	cou.three_rivers IS FALSE
GROUP BY
	cou.country_name, c.continent_name
ORDER BY
	monasteries_count DESC,
	cou.country_name