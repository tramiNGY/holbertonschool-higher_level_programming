-- lists all cities contained in the database hbtn_0d_usa
SELECT cities.id AS id, cities.name AS city_name, states.name AS state_name FROM cities JOIN states ON cities.states_id = state_id ORDER BY cities.id ASC;
