SELECT
	t.id AS team_id,
	t.name As team_name,
	count(p.id) AS player_count,
	t.fan_base
FROM
	teams AS t
LEFT JOIN
	players AS p
ON
	p.team_id = t.id
WHERE
	t.fan_base > 30000
GROUP BY
	t.id
ORDER BY
	count(p.id) DESC, t.fan_base DESC;