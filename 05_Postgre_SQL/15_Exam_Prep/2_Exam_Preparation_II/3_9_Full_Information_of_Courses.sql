SELECT
	ad."name" AS address,
	CASE
		WHEN EXTRACT (HOUR FROM co."start") BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	co.bill,
	c.full_name,
	cr.make,
	cr.model,
	cat.name AS category_name
FROM
	courses AS co
JOIN
	clients AS c
ON
	c.id = co.client_id
JOIN
	cars AS cr
ON
	cr.id = co.car_id
JOIN
	categories AS cat
ON
	cat.id = cr.category_id
JOIN
	addresses AS ad
ON
	ad.id = co.from_address_id
ORDER BY
	co.id;
