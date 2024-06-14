CREATE OR REPLACE FUNCTION fn_creator_with_board_games(
	first_name_creator VARCHAR(30)
)
RETURNS INT
AS
$$
	DECLARE
		bg_count INT;
	BEGIN
		bg_count =
		(
		SELECT
			COUNT(*)
		FROM
			creators AS c
		JOIN
			creators_board_games AS cbg
		ON
			cbg.creator_id = c.id
		WHERE
			c.first_name = first_name_creator);
	RETURN bg_count;
	END;
$$
LANGUAGE plpgsql;
