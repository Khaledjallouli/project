import csv
import datetime
from functools import reduce

# Extract data from sqlite to csv

#(base) macspuck:data woiza$ sqlite3 eusoccerdatabase.sqlite
#sqlite> .headers on
#sqlite> .mode csv
#sqlite> .output matches_all.csv
#sqlite> SELECT id, country_id, league_id, season, stage, date, match_api_id, home_team_api_id, away_team_api_id, home_team_goal, away_team_goal, B365H, B365D, B365A FROM Match;
#sqlite> .quit


class Dataset:
    def __init__(self, file_path):
        
        self.raw_results = []
        self.processed_results = []

        with open(file_path) as stream:
            reader = csv.DictReader(stream)

            for row in reader:
                row['date'] = datetime.datetime.strptime(row['date'], '%Y-%m-%d %H:%M:%S')
                self.raw_results.append(row)

        for result in self.raw_results:
            home_statistics = self.get_statistics(result['home_team_api_id'], result['date'])

            if home_statistics is None:
                continue

            away_statistics = self.get_statistics(result['away_team_api_id'], result['date'])

            if away_statistics is None:
                continue

            processed_result = {
                'home_team_goal': int(result['home_team_goal']) if result['home_team_goal'] != '' else 0,
                'away_team_goal': int(result['away_team_goal']) if result['away_team_goal'] != '' else 0,
                'odds-home': float(result['B365H']) if result['B365H'] != '' else 0,
                'odds-draw': float(result['B365D']) if result['B365D'] != '' else 0,
                'odds-away': float(result['B365A']) if result['B365A'] != '' else 0,
            }

            for label, statistics in [('home', home_statistics), ('away', away_statistics)]:
                for key in statistics.keys():
                    processed_result[label + '-' + key] = statistics[key]

            self.processed_results.append(processed_result)

    # filter results to only contain matches played before a given date and by a given team
    def filter(self, team, date):
        def filter_fn(result):
            return (
                result['home_team_api_id'] == team or
                result['away_team_api_id'] == team
            ) and (result['date'] < date)

        return list(filter(filter_fn, self.raw_results))

    # team statistics
    def get_statistics(self, team, date, matches=10):
        recent_results = self.filter(team, date)
#        print(recent_results)
        if len(recent_results) < matches:
            return None

        # map a result to a set of performance measures
        def map_fn(result):
            if result['home_team_api_id'] == team:
                team_letter, opposition_letter = 'home_team', 'away_team'
                opposition = result['away_team_api_id']
            else:
                team_letter, opposition_letter = 'away_team', 'home_team'
                opposition = result['home_team_api_id']

            goals = int(result['{}_goal'.format(team_letter)])
            opposition_goals = int(result['{}_goal'.format(opposition_letter)])

            return {
                'wins': 1 if goals > opposition_goals else 0,
                'draws': 1 if goals == opposition_goals else 0,
                'losses': 1 if goals < opposition_goals else 0,
                'goals': goals,
                'opposition-goals': opposition_goals,
            }

        def reduce_fn(x, y):
            result = {}

            for key in x.keys():
                result[key] = x[key] + y[key]

            return result
        
        #print(reduce(reduce_fn, map(map_fn, recent_results[-matches:])))     
        #{'wins': 2, 'draws': 5, 'losses': 3, 'goals': 18, 'opposition-goals': 20}
        return reduce(reduce_fn, map(map_fn, recent_results[-matches:]))

