import sqlite3
from datetime import datetime, date

# IDEA
# Download .csv file from https://www.football-data.co.uk/germanym.php (updated frequently)
# add missing matches to database
# Fetch dates for future matches from https://www.worldfootball.net/all_matches/bundesliga-2019-2020/
# predict them based on database contents

# Q
# - Where to take total goals from / how to calculate it?
# - last 10 games

def create_database(file):
    with sqlite3.connect(file) as con:
        cursor = con.cursor()

        # required values for the model are:
        # - odds-home                       (nullable) (float)
        # - odds-away                       (nullable) (float)
        # - home-wins                       (nullable) (calculated)
        # - home-draws                      (nullable) (calculated)
        # - home-losses                     (nullable) (calculated)
        # - home-goals                      (nullable) (not to mistake for home-total-goals which is (calculated &) inserted into the model at position "home-goals")
        # - home-opposition-goals           (nullable) (calculated)
        # - home-shots                      (nullable) (not to mistake for home-total-shots which is calculated & inserted into the model at position "home-shots")
        # - home-shots-on-target            (nullable) (not to mistake for home-total-shots-on-target which is calculated & inserted into the model at position "home-shots-on-target")
        # - home-opposition-shots           (nullable) (calculated)
        # - home-opposition-shots-on-target (nullable) (calculated)
        # - away-wins                       (nullable) (calculated)
        # - away-draws                      (nullable) (calculated)
        # - away-losses                     (nullable) (calculated)
        # - away-goals                      (nullable) (not to mistake for away-total-goals which is calculated & inserted into the model at position "away-goals")
        # - away-opposition-goals           (nullable) (calculated)
        # - away-shots                      (nullable) (not to mistake for away-total-shots which is calculated & inserted into the model at position "away-shots")
        # - away-shots-on-target            (nullable) (not to mistake for away-total-shots-on-target which is calculated & inserted into the model at position "away-shots-on-target")
        # - away-opposition-shots           (nullable) (calculated)
        # - away-opposition-shots-on-target (nullable) (calculated)
        cursor.execute("CREATE TABLE matches ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"    # primary-key
            "'predicted-result' TEXT,"                          # 'H'|'D'|'A'
            "'actual-result' TEXT,"                             # 'H'|'D'|'A'
            "'home-team' TEXT NOT NULL,"                        # self-explaining
            "'away-team' TEXT NOT NULL,"                        # self-explaining
            "'date' TEXT NOT NULL,"                             # date, stored as string (sqlite doesn't support date-type)
            "'odds-home' REAL,"                                 # (float)
            "'odds-away' REAL,"                                 # (float)
            "'home-goals' INTEGER,"                             # (not to mistake for home-total-goals which is (calculated &) inserted into the model at position "home-goals")
            "'home-shots' INTEGER,"                             # (not to mistake for home-total-shots which is calculated & inserted into the model at position "home-shots")
            "'home-shots-on-target' INTEGER,"                   # (not to mistake for home-total-shots-on-target which is calculated & inserted into the model at position "home-shots-on-target")
            "'away-goals' INTEGER,"                             # (not to mistake for away-total-goals which is calculated & inserted into the model at position "away-goals")
            "'away-shots' INTEGER,"                             # (not to mistake for away-total-shots which is calculated & inserted into the model at position "away-shots")
            "'away-shots-on-target' INTEGER"                    # (not to mistake for away-total-shots-on-target which is calculated & inserted into the model at position "away-shots-on-target")
            ")")
        con.commit()

def add_match(file,hometeam,awayteam,date,result,oddshome,oddsaway,homegoals,homeshots,homeshotsontarget,awaygoals,awayshots,awayshotsontarget):
    with sqlite3.connect(file) as con:
        cursor = con.cursor()
        cursor.execute("INSERT OR IGNORE INTO matches ("
            "'home-team',"
            "'away-team',"
            "'date',"
            "'actual-result',"
            "'odds-home',"
            "'odds-away',"
            "'home-goals',"
            "'home-shots',"
            "'home-shots-on-target',"
            "'away-goals',"
            "'away-shots',"
            "'away-shots-on-target'"
            ") VALUES ('"
            +hometeam+"','"
            +awayteam+"','"
            +date+"','"
            +result+"','"
            +oddshome+"','"
            +oddsaway+"','"
            +homegoals+"','"
            +homeshots+"','"
            +homeshotsontarget+"','"
            +awaygoals+"','"
            +awayshots+"','"
            +awayshotsontarget+
            "')")
        con.commit()

# testing:
def main():
    file = "database.sqlite"
    create_database(file)
if __name__ == "__main__":
    main()