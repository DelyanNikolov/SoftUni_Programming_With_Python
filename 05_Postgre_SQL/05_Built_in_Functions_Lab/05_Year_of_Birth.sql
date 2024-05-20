SELECT
	first_name,
	last_name,
	extract('year' from born) AS year
FROM authors

--SELECT
--	first_name,
--	last_name,
--	date_part('year', born) AS year
--FROM authors