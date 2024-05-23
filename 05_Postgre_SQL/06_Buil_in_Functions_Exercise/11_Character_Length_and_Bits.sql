SELECT
	CONCAT(m.mountain_range, ' ', p.peak_name) AS mountain_information,
	CHAR_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS characters_length,
	BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)) AS bits_of_a_tring
FROM
	peaks AS p,
	mountains AS m
WHERE
	m.id = p.mountain_id