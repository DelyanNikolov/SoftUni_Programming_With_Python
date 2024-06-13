CREATE OR REPLACE PROCEDURE sp_players_team_name(
	IN player_name VARCHAR(50),
	OUT team_name VARCHAR(50)
)
AS
$$
	BEGIN
		SELECT
			t."name" INTO team_name
		FROM
			players AS p
		JOIN
			teams AS t
		ON
			t.id = p.team_id
		WHERE
			CONCAT(p.first_name, ' ', p.last_name) = player_name;

	IF team_name IS NULL THEN
		team_name := 'The player currently has no team';
	END IF;

	END;
$$
LANGUAGE plpgsql;