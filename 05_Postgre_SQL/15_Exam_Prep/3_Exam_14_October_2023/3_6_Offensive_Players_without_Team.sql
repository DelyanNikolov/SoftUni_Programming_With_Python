SELECT
	p.id,
	CONCAT(first_name, ' ', last_name) AS full_name,
	p.age,
	p.position,
	p.salary,
	sd.pace,
	sd.shooting
FROM
	players AS p
JOIN
	skills_data AS sd
ON
	sd.id = p.skills_data_id
WHERE
	position = 'A'
	AND
	team_id IS NULL
	AND
	pace + shooting > 130;