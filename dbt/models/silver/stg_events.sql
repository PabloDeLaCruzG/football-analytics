-- Query that reads all the event Parquet files from bronze/events, just a specific columns
SELECT 
    -- Basics
    id, match_id, index, period, timestamp, minute, second, type_name, team_name, player_name, x, y,

    -- Event Context
    possession, duration, type_id, possession_team_id, possession_team_name, play_pattern_id, play_pattern_name,
    team_id, tactics_formation, player_id, position_id, position_name,

    -- Pass specifics
    pass_recipient_id, pass_recipient_name, pass_length, pass_angle, pass_height_id, pass_height_name, 
    pass_switch, pass_cross, pass_cut_back, pass_deflected, pass_no_touch, pass_goal_assist, 
    pass_shot_assist, pass_assisted_shot_id, pass_miscommunication,

    -- Shot specifics
    shot_statsbomb_xg, shot_key_pass_id, shot_first_time, shot_one_on_one, end_x, end_y, end_z, 
    body_part_id, body_part_name, technique_id, technique_name, outcome_id, outcome_name, 
    sub_type_id, sub_type_name,

    -- Other types of events (duels, fouls, keeper)
    coalesce(under_pressure::boolean, false) as under_pressure, -- Change Nulls to false
    coalesce(aerial_won, false) as aerial_won, -- Change Nulls to false
    counterpress, off_camera, out, block_deflection, block_offensive, 
    dribble_nutmeg, dribble_overrun, foul_committed_offensive, foul_committed_advantage, 
    foul_committed_card_id, foul_committed_card_name, foul_won_defensive, foul_won_advantage, 
    bad_behaviour_card_id, bad_behaviour_card_name, substitution_replacement_id, substitution_replacement_name, 
    goalkeeper_position_id, goalkeeper_position_name, ball_recovery_recovery_failure

FROM read_parquet('/Users/pablodelacruz/Essentials/Projects/football-analytics/data/bronze/events/*.parquet') -- path since dbt/