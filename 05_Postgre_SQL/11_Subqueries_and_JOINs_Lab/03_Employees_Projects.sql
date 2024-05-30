SELECT
	e.employee_id,
	concat(e.first_name, ' ', e.last_name) AS full_name,
	p.project_id,
	p.name AS project_name
FROM employees as e
	JOIN employees_projects AS ep
		ON ep.employee_id = e.employee_id
	JOIN projects as p
		ON p.project_id = ep.project_id
WHERE p.project_id = 1