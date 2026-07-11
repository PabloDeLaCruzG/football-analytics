-- Query thath reads all the event Parquet files from bronze/events, just a specific columns
SELECT id, match_id, index, period, timestamp, minute, second, type_name, team_name, player_name, x, y
FROM read_parquet('/Users/pablodelacruz/Essentials/Projects/football-analytics/data/bronze/events/*.parquet') -- path since dbt/