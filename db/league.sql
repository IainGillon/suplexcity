DROP TABLE IF EXISTS league;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS wrestlers;

CREATE TABLE wrestlers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    points INT 
);

CREATE TABLE league (
    id SERIAL PRIMARY KEY,
    -- wrestler_id INT REFERENCES Wrestler(id)

);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    -- wrestler_id INT REFERENCES Wrestler(id)
);