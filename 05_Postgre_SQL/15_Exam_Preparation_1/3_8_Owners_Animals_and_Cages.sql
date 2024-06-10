SELECT
	concat(o."name", ' - ', a."name") AS "owners - animals",
	o.phone_number,
	ac.cage_id
FROM
	owners AS o
JOIN
	animals AS a
	ON a.owner_id = o.id
	JOIN
		animal_types AS at
		ON at.id = a.animal_type_id
		JOIN animals_cages as ac
			ON ac.animal_id = a.id
			JOIN cages AS c
				ON c.id = ac.cage_id
WHERE
	at.animal_type = 'Mammals'
ORDER BY
	o.name, a."name" DESC;
