UPDATE
		employees
SET
		salary = salary + 1500,
		job_title = 'Senior ' || job_title
WHERE
		hire_date BETWEEN '1998-1-1' and '2000-1-5'
