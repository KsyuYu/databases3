CREATE TABLE Contries (
    country VARCHAR(30) NOT NULL
    );

CREATE TABLE TotalCases (
    country VARCHAR(30) NOT NULL
    ,total_cases INT NOT NULL
    ,new_cases INT NOT NULL
    );

CREATE TABLE TotalDeaths (
    country VARCHAR(30) NOT NULL
    ,total_deaths INT NOT NULL
    ,new_deaths INT NOT NULL
    );

ALTER TABLE Contries ADD CONSTRAINT Contries_PK PRIMARY KEY (country);
ALTER TABLE TotalCases ADD CONSTRAINT TotalCases_PK PRIMARY KEY (country);
ALTER TABLE TotalDeaths ADD CONSTRAINT TotalDeaths_PK PRIMARY KEY (country);
