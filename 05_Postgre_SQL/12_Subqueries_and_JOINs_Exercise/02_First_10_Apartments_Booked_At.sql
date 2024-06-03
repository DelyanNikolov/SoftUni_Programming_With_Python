SELECT
	a."name",
	a.country,
	b.booked_at::DATE
FROM
	apartments AS a
LEFT JOIN
	bookings AS b
ON
	a.booking_id = b.booking_id
LIMIT 10;