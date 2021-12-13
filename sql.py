create_schema = ('''
    CREATE SCHEMA IF NOT EXISTS petl3;
''')

create_table = ('''
    CREATE TABLE IF NOT EXISTS petl3.viable_counties (
        geo_id INT,
        state TEXT,
        county TEXT,
        sales_vector INT
    );
''')

create_insert = ('''
    INSERT INTO petl3.viable_counties
    VALUES(%s, %s, %s, %s);
''')