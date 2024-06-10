SELECT
	name AS volunteers,
	phone_number,
	TRIM(address, 'Sofia, ')
FROM
	volunteers
	JOIN
		volunteers_departments ON volunteers_departments.id = volunteers.department_id
WHERE
	address LIKE '%Sofia%'
	AND
	volunteers_departments.department_name = 'Education program assistant'
ORDER BY
	volunteers.name;