import clickhouse_connect


if __name__ == "__main__":
    # Set connection to clickhouse
    client = clickhouse_connect.get_client(
        host='[host]',
        port='[port]',
        username='[username]',
        password='[password]',
    )
    # Create table there (I used GPT-4 requestfor that)
    client.command(' \
        CREATE TABLE agency_data (\
            date Date,\
            platform String,\
            user_id UUID,\
            is_active UInt8,\
            daily_visits UInt32,\
            cpc Float32,\
            ad_name String,\
            clicks UInt32\
        ) ENGINE = MergeTree()\
        PARTITION BY toYYYYMM(date)\
        ORDER BY (date, platform);'
                   )
    # Fill in dummy data (I used GPT-4 request for that)
    client.command("\
        INSERT INTO agency_data (date, platform, user_id, is_active, daily_visits, cpc, ad_name, clicks) VALUES\
        ('2022-01-01', 'Google', generateUUIDv4(), 1, NULL, 2.3, 'Ad1', 100),\
        ('2022-01-02', 'LinkedIn', generateUUIDv4(), 1, NULL, 1.2, 'Ad2', 230),\
        ('2022-01-03', 'Website', NULL, NULL, 5000, NULL, NULL, NULL),\
        ('2023-01-01', 'Google', generateUUIDv4(), 1, NULL, 2.5, 'Ad3', 340),\
        ('2023-01-02', 'Bing', generateUUIDv4(), 0, NULL, 1.8, 'Ad4', 400),\
        ('2023-02-05', 'Facebook', generateUUIDv4(), 1, NULL, 1.9, 'Ad5', 300),\
        ('2023-02-10', 'Google', generateUUIDv4(), 1, NULL, 2.2, 'Ad6', 120),\
        ('2023-03-15', 'LinkedIn', generateUUIDv4(), 0, NULL, 2.1, 'Ad7', 140),\
        ('2023-03-20', 'Website', NULL, NULL, 6000, NULL, NULL, NULL),\
        ('2023-04-01', 'Bing', generateUUIDv4(), 0, NULL, 1.7, 'Ad8', 260),\
        ('2022-02-05', 'Facebook', generateUUIDv4(), 1, NULL, 1.8, 'Ad9', 180),\
        ('2022-03-10', 'Google', generateUUIDv4(), 1, NULL, 2.4, 'Ad10', 160),\
        ('2022-04-01', 'LinkedIn', generateUUIDv4(), 0, NULL, 2.2, 'Ad11', 240),\
        ('2022-05-20', 'Website', NULL, NULL, 5500, NULL, NULL, NULL),\
        ('2022-06-15', 'Bing', generateUUIDv4(), 0, NULL, 1.6, 'Ad12', 200);\
    ")
    # Check correctness
    print(client.command('SELECT TOP 5 * FROM agency_data;'))
    print(client.command(
        "desc agency_data"))
