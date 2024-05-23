SELECT
	user_id,
	AGE(starts_at, booked_at) as "Early Birds"
FROM
	bookings
WHERE
	starts_at - booked_at >= '10 MONTHS'