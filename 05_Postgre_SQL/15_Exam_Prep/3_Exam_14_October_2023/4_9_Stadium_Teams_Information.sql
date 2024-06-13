CREATE OR REPLACE FUNCTION fn_stadium_team_name(
	stadium_name VARCHAR(30)
)
RETURNS TABLE (fn_stadium_team_name VARCHAR(100))
AS
$$
	BEGIN
		RETURN QUERY
			SELECT
				t.name
			FROM
				stadiums AS s
			JOIN
				teams AS t
			ON
				t.stadium_id = s.id
			WHERE
				s.name = stadium_name
			ORDER BY
				t.name;
	END;
$$
LANGUAGE
	plpgsql;