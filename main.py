import sql
import pgsql
from google.cloud import bigquery;


if __name__ == '__main__':

    #pgsql.query(sql.create_schema);

    #pgsql.query(sql.create_table);

    #client = bigquery.Client()
    #query = client.query(
        #"""
        #SELECT *
        #FROM `bigquery-public-data.stackoverflow.posts_questions`
        #ORDER BY view_count DESC
        #LIMIT 10;
        #"""
    #)
    #for row in query.result():
        #print(row)

    client = bigquery.Client()
    query = client.query(
        """
        WITH CTE_data AS (
            SELECT geo_id, sub_region_1 AS state, sub_region_2 AS county, AVG(retail_and_recreation_percent_change_from_baseline) AS sales_vector
            FROM bigquery-public-data.census_bureau_acs.county_2017_1yr
            JOIN bigquery-public-data.covid19_google_mobility.mobility_report ON geo_id ||'.0'= census_fips_code
            WHERE median_rent < 2000 AND median_age < 30
            GROUP BY geo_id, sub_region_1, sub_region_2
        )
        SELECT geo_id, state, county, sales_vector
        FROM CTE_data
        WHERE sales_vector > -15
        GROUP BY geo_id, state, county, sales_vector
        ORDER BY sales_vector DESC
        """
    );
    for row in query.result():
        #print(row)

        pgsql.query(sql.create_insert, row);