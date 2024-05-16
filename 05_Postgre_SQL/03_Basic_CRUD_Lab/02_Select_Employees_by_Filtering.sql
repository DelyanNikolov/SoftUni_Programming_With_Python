SELECT
	id,
	concat(first_name, ' ', last_name) AS full_name,
	job_title,
	salary
FROM employees AS e
WHERE salary > 1000.00