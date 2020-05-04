CREATE OR REPLACE VIEW Total AS
    SELECT 
        TotalCases.country, 
        TotalCases.total_cases,
        TotalCases.new_cases,
        TotalDeaths.total_deaths,
        TotalDeaths.data
    FROM
        TotalCases JOIN TotalDeaths
        ON TotalCases.country = TotalCases.country;
