CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
    IN animal_name VARCHAR(30),
    OUT owner_name VARCHAR(30)
)
AS
$$
BEGIN
    SELECT
        o.name
    INTO owner_name
    FROM
        animals AS a
    LEFT JOIN
        owners AS o
    ON o.id = a.owner_id
    WHERE
        a.name = animal_name;

    IF owner_name IS NULL THEN
        owner_name := 'For adoption';
    END IF;
END;
$$
LANGUAGE plpgsql;
