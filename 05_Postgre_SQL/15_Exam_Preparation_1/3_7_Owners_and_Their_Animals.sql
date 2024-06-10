SELECT
	o.name AS owner,
	count(*) AS count_of_animals
FROM
	owners as o
JOIN
	animals as a
ON
	a.owner_id = o.id
GROUP BY
	owner
ORDER BY
	count_of_animals DESC, o."name"
LIMIT 5;