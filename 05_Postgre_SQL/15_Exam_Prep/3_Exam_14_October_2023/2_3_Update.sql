UPDATE
	coaches
SET
	salary = salary * coach_level
WHERE
	id = (SELECT
			c.id
		FROM
			coaches AS c
		LEFT JOIN
			players_coaches AS pc
		ON
			c.id = pc.coach_id
		WHERE
			first_name LIKE 'C%'
		GROUP BY
			c.id
		HAVING
			COUNT(pc.player_id) > 0);