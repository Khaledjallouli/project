import sqlite3
from datetime import datetime, date

def create_database(file):
    with sqlite3.connect(file) as con:
        cursor = con.cursor()

        # required values for the model are:
        # - odds-home                       (nullable) (float)
        # - odds-draw                       (nullable) (float)
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
        cursor.execute("CREATE TABLE IF NOT EXISTS matches ("
            "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"    # primary-key
            "'predicted-classification-result' TEXT,"           # 'H'|'D'|'A'
            "'predicted-regression-result' TEXT,"               # "3-2"
            "'home-team' TEXT NOT NULL,"                        # self-explaining
            "'away-team' TEXT NOT NULL,"                        # self-explaining
            "'date' INTEGER NOT NULL,"                          # date, stored as int (to enable sorting) (sqlite doesn't support date-type)
            "'odds-home' REAL,"                                 # (float)
            "'odds-draw' REAL,"                                 # (float)
            "'odds-away' REAL,"                                 # (float)
            "'home-goals' INTEGER,"                             # (not to mistake for home-total-goals which is (calculated &) inserted into the model at position "home-goals")
            "'home-shots' INTEGER,"                             # (not to mistake for home-total-shots which is calculated & inserted into the model at position "home-shots")
            "'home-shots-on-target' INTEGER,"                   # (not to mistake for home-total-shots-on-target which is calculated & inserted into the model at position "home-shots-on-target")
            "'away-goals' INTEGER,"                             # (not to mistake for away-total-goals which is calculated & inserted into the model at position "away-goals")
            "'away-shots' INTEGER,"                             # (not to mistake for away-total-shots which is calculated & inserted into the model at position "away-shots")
            "'away-shots-on-target' INTEGER,"                   # (not to mistake for away-total-shots-on-target which is calculated & inserted into the model at position "away-shots-on-target")
            "UNIQUE('home-team','away-team','date')"            ### adding uniqueness
            ")")
        con.commit()

def add_match(file,hometeam,awayteam,date,predicted_classification_result,predicted_regression_result,oddshome,oddsdraw,oddsaway,homegoals,homeshots,homeshotsontarget,awaygoals,awayshots,awayshotsontarget):
    with sqlite3.connect(file) as con:
        cursor = con.cursor()
        cursor.execute("INSERT OR IGNORE INTO matches ("
            "'home-team',"
            "'away-team',"
            "'date',"
            "'predicted-classification-result',"
            "'predicted-regression-result',"
            "'odds-home',"
            "'odds-draw',"
            "'odds-away',"
            "'home-goals',"
            "'home-shots',"
            "'home-shots-on-target',"
            "'away-goals',"
            "'away-shots',"
            "'away-shots-on-target'"
            ") VALUES ('"
            +hometeam+"','"
            +awayteam+"',"
            +str(date)+",'"
            +str(predicted_classification_result)+"','"
            +str(predicted_regression_result)+"','"
            +oddshome+"','"
            +oddsdraw+"','"
            +oddsaway+"','"
            +homegoals+"','"
            +homeshots+"','"
            +homeshotsontarget+"','"
            +awaygoals+"','"
            +awayshots+"','"
            +awayshotsontarget+
            "')")
        con.commit()

def update_matchprediction(file,hometeam,awayteam,date,predicted_classification_result,predicted_regression_result):
     with sqlite3.connect(file) as con:
        cursor = con.cursor()    
        cursor.execute("UPDATE matches SET"
        "  'predicted-classification-result' = " + predicted_classification_result +
        ", 'predicted-regression-result' = " + predicted_regression_result +
        " WHERE"
        " 'hometeam' = " + hometeam + " AND" +
        " 'awayteam' = " + awayteam + " AND" +
        " 'date' = " + date)
        con.commit()

#Note: get_match only exists for controller.main (testing) purpose
def get_match(file,hometeam,awayteam,date):
    with sqlite3.connect(file) as con:
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT * FROM matches WHERE "
            "matches.'home-team'='"+hometeam+"' AND "
            "matches.'away-team'='"+awayteam+"' AND "
            "matches.'date'="+str(date)
        )

        return cursor.fetchall()[0]

def get_teamhistory(file,teamname,date): # return cumulated data of last 10 matches of team
    # get ids of last 10 matches as hometeam
    matches = []
    matchids = []
    with sqlite3.connect(file) as con:
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT id FROM matches WHERE "
            "(matches.'home-team'='"+teamname+"' OR "
            "matches.'away-team'='"+teamname+"') AND "
            "matches.'date' < "+str(date)+" "
            "ORDER BY matches.'date' "
            "LIMIT 10"
        )
        matchids = cursor.fetchall()
        matchids = [str(matchid["id"]) for matchid in matchids] # convert each tuple to single value and convert that to string
    
    # get gamedata of last 10 matches

    with sqlite3.connect(file) as con:
        con.row_factory = dict_factory
        cursor = con.cursor()
        
        joined_matchids = ','.join(matchids)
        cursor.execute("SELECT * FROM matches WHERE "
            "matches.'id' IN ("
            +joined_matchids+
            ")"
        )
        for match in cursor.fetchall():
            if match["home-team"] == teamname: # home-team
                # add home-team values
                matches.append([
                    match["home-goals"], # home-goals
                    match["home-shots"], # home-shots
                    match["home-shots-on-target"], # home-shots-on-target
                    match["away-goals"], # away-goals
                    match["away-shots"], # away-shots
                    match["away-shots-on-target"]  # away-shots-on-target
                ])
            elif match["away-team"] == teamname: # away-team
                # add away-team values
                matches.append([
                    match["away-goals"], # away-goals
                    match["away-shots"], # away-shots
                    match["away-shots-on-target"], # away-shots-on-target
                    match["home-goals"], # home-goals
                    match["home-shots"], # home-shots
                    match["home-shots-on-target"]  # home-shots-on-target
                ])
            else:
                raise Exception("Neither home-team nor away-team matches the provided teamname.")
    return matches # list of [own-goals, own-shots, own-shots-on-target, opposite-goals, opposite-shots, opposite-shots-on-target]

def get_matches(file):
    with sqlite3.connect(file) as con:
        con.row_factory = dict_factory
        cursor = con.cursor()
        cursor.execute("SELECT * FROM matches")
        return cursor.fetchall()

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

# testing:
def main():
    file = "database.sqlite"
    create_database(file)
    print(get_teamhistory(file,"bayern-muenchen",20200604))
if __name__ == "__main__":
    main()