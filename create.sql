CREATE TABLE Countries(
country VARCHAR(30) NOT NULL,
total_cases INT NOT NULL REFERENCES Rank (total_cases)
);

CREATE TABLE Cases(
total_cases VARCHAR2 (30) NOT NULL,
new_cases INT NOT NULL,
total_deaths INT NOT NULL,
data DATE);

CREATE TABLE Disease(
disease VARCHAR2 (50) NOT NULL,
data DATE);

ALTER TABLE Countries ADD CONSTRAINT Countries_PK PRIMARY KEY (country);
ALTER TABLE Cases ADD CONSTRAINT Cases_PK PRIMARY KEY (total_cases);
ALTER TABLE Disease ADD CONSTRAINT Disease_PK PRIMARY KEY (data);
