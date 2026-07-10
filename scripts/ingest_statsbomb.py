from mplsoccer import Sbopen
import pandas as pd
import pathlib

BRONZE_DIR = pathlib.Path("data/bronze")
COMPETITION_ID = 11

def get_matches(competition_id, season_id):
    parser = Sbopen()
    return parser.match(competition_id, season_id)

"""
Returns 4 Dataframes, 
 - df_event (every action in the match)
 - df_related (links between related events)
 - df_freeze (player position at the moment of a shot, for Example.)
 - df_tactics (tactical lineup)
"""
def get_events(match_id):
    parser = Sbopen()
    return parser.event(match_id)

"""
Take a DF, a match_id, and a name like 'events' or 'tactics'
Create the directory BRONZE_DIR / name if it dowsn't exist
Save the DF as a Parquet file
"""
def save_to_bronze(df, match_id, name):
    dir = pathlib.Path(BRONZE_DIR) / name
    dir.mkdir(parents=True, exist_ok=True)

    file = dir / f"{match_id}.parquet"
    
    # convert timestamps for parquet
    if 'timestamp' in df.columns:
        df['timestamp'] = df['timestamp'].astype(str)

    df.to_parquet(file)


if __name__ == "__main__":
    
    """ Get all matches """
    print("Getting matches")
    df_match = get_matches(COMPETITION_ID, 4)
    print(f"{df_match.shape} - Matches!")
    # print(df_match.shape) # matches and columns
    # print(df_match.columns.tolist()) # To know the columns

    """ Save each match and his events in the correct Dir"""
    for _, row in df_match.iterrows():
        df_event, df_related, df_freeze, df_tactics = get_events(row['match_id'])

        print(f"Processing match {row['match_id']}...")

        save_to_bronze(df_event, row['match_id'], "events")
        save_to_bronze(df_related, row['match_id'], "related_events")
        save_to_bronze(df_freeze, row['match_id'], "freeze_events")
        save_to_bronze(df_tactics, row['match_id'], "tactics_events")

        print(f"Done match {row['match_id']}!")
    
    print(f"Ingest is DONE!")


    # Check if there are any nested column that need to be serialize to string
    # for col in df_event.columns:
    #     if df_event[col].dtype == 'object':
    #         print(col, type(df_event[col].iloc[0]))