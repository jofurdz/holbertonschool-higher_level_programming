-- lists all cities contained in the databse

SELECT cities.id, cities.name, states.name
FROM cities JOIN states on cities.state_id = states.id;
