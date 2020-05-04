CREATE OR REPLACE VIEW Total AS
    SELECT 
        Countries.country, 
        Cases.total_cases,
        Cases.new_cases,
        Cases.total_deaths,
        Cases.data,
        Disease.disease
    FROM
        Countries JOIN Cases
        ON Countries.total_cases = Cases.total_cases
        JOIN Disease
        ON Disease.data = Cases.data;
