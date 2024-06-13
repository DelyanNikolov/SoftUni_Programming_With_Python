CREATE OR REPLACE FUNCTION
	fn_courses_by_client(
	phone_num VARCHAR(20)
	)
RETURNS INT
AS
$$
	BEGIN
	RETURN (SELECT
			count(*)
		FROM
			clients
		JOIN
			courses
		ON
			courses.client_id = clients.id
		WHERE
			clients.phone_number = phone_num);
	END;
$$
LANGUAGE plpgsql;
