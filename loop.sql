DECLARE
    count_country INTEGER := 10;
BEGIN
    FOR i IN 1..count_country LOOP
        INSERT INTO TotalCases (
            country,
            total_cases,
            new_cases
        ) VALUES (
            'Country' || i,
            i*i,
            i
        );
    END LOOP;
END;
