CREATE OR REPLACE VIEW
	view_continents_countries_currencies_details
AS
SELECT
	CONCAT(cont.continent_name, ': ', cont.continent_code
	) AS continent_details,
	CONCAT_WS(' - ',
			coun.country_name,
			coun.capital,
			coun.area_in_sq_km,
			'km2'
	) AS country_information,
	CONCAT(cur.description, ' (', cur.currency_code, ')'
	) AS currencies

FROM
	continents AS cont,
	countries AS coun,
	currencies AS cur
WHERE
	cont.continent_code = coun.continent_code
	AND
	coun.currency_code = cur.currency_code

ORDER BY
	country_information,
	currencies;

SELECT * FROM view_continents_countries_currencies_details