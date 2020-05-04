CREATE TABLE Contries (
    country VARCHAR(30) NOT NULL
    );

CREATE TABLE TotalCases (
    country VARCHAR(30) NOT NULL
    ,total_cases INT
    ,new_cases INT
    );

CREATE TABLE TotalDeaths (
    country VARCHAR(30) NOT NULL
    ,total_deaths INT
    ,new_deaths INT
    );

ALTER TABLE Contries ADD CONSTRAINT Contries_PK PRIMARY KEY (country);
ALTER TABLE TotalCases ADD CONSTRAINT TotalCases_PK PRIMARY KEY (country);
ALTER TABLE TotalDeaths ADD CONSTRAINT TotalDeaths_PK PRIMARY KEY (country);
