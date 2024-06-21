CREATE OR REPLACE FUNCTION udf_accounts_photos_count(
	account_username VARCHAR(30)
)
RETURNS INT
AS
$$
	DECLARE
		photos_count INT;
	BEGIN
		photos_count =
		(
		SELECT
			COUNT(ap.photo_id)
		FROM
			accounts AS a
		JOIN
			accounts_photos AS ap
		ON
			ap.account_id = a.id
		WHERE
			username = account_username
		);
	RETURN photos_count;
	END;
$$
LANGUAGE plpgsql;
