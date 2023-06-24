# For few-shots we can take the questions listed in Assigment. Ideally add to them COT (chain-of-thoughts)

few_shot = [
    "-- How many active agency customers did we have on January 1st, 2022? \n\
SELECT COUNT(user_id) AS active_customers FROM agency_data WHERE date = '2022-01-01' AND is_active = 1; \n\n",
    "-- When did we get the highest number of users per day in Q1 2023? \n\
SELECT date, COUNT(user_id) AS number_of_users FROM agency_data WHERE date BETWEEN '2023-01-01' AND '2023-03-31' GROUP BY date ORDER BY number_of_users DESC LIMIT 1; \n\n",
    "-- When did we get the maximum of daily visits on the website in 2022? \n\
SELECT date, daily_visits FROM agency_data WHERE platform = 'Website' AND date BETWEEN '2022-01-01' AND '2022-12-31' ORDER BY daily_visits DESC LIMIT 1;\n\n",
    "-- What was the average CPC in Google Ads in April 2023? \n\
SELECT AVG(cpc) AS average_cpc FROM agency_data WHERE platform = 'Google' AND date BETWEEN '2023-04-01' AND '2023-04-30'; \n\n",
    "-- How many LinkedIn clicks did we have in 2022? \n\
SELECT SUM(clicks) AS total_linkedin_clicks FROM agency_data WHERE platform = 'LinkedIn' AND date BETWEEN '2022-01-01' AND '2022-12-31'; \n\n",
    "-- Which platform had the highest CPC in 2022: Google or Bing? \n\
SELECT platform, AVG(cpc) AS average_cpc FROM agency_data WHERE platform IN ('Google', 'Bing') AND date BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY platform ORDER BY average_cpc DESC LIMIT 1;\n\n",
    "-- Get the best ad name by clicks from Facebook, Google, and LinkedIn for 2022.\n\
SELECT ad_name, SUM(clicks) AS total_clicks FROM agency_data WHERE platform IN ('Facebook', 'Google', 'LinkedIn') AND date BETWEEN '2022-01-01' AND '2022-12-31' GROUP BY ad_name ORDER BY total_clicks DESC LIMIT 1;\n\n"
]

# TODO Should be gathered programmatically
select = [
    "date platform user_id is_active daily_visits cpc ad_name clicks",
    "2022-01-01 Google 8544439b-0478-486f-8189-bd2e6bb9e5b9 1 0 2.3 Ad1 100",
    "2022-01-02 LinkedIn 98e21fbb-cb3e-49ee-b46e-7ca81a52ce3f 1 0 1.2 Ad2 230",
    "2022-02-05 Facebook dcf336c6-932b-409c-bd18-5816393dcfc1 1	0 1.8 Ad9 180",
    "2022-03-10 Google fd08bdfc-8e45-41e5-b287-0615ca898b23 1 0 2.4 Ad10 160",
    "2022-04-01 LinkedIn f29b55bf-90ea-451a-aa0b-ec6d8cf421cc 0	0 2.2 Ad11 240",
]

schema = 'CREATE TABLE agency_data (\
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
