import csv
import datetime
from functools import reduce

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

            # home/away team wins or draw
            def winner():
                if int(result['home_team_goal']) > int(result['away_team_goal']):
                    return 'H'
                elif int(result['home_team_goal']) < int(result['away_team_goal']):
                    return 'A'
                elif int(result['home_team_goal']) == int(result['away_team_goal']):
                    return 'D'

            processed_result = {
                'result': winner(),
                'odds-home': float(result['B365H']) if result['B365H'] != '' else 0,
                'odds-draw': float(result['B365D']) if result['B365D'] != '' else 0,
                'odds-away': float(result['B365A']) if result['B365A'] != '' else 0,
            }

            for label, statistics in [('home', home_statistics), ('away', away_statistics)]:
                for key in statistics.keys():
                    processed_result[label + '-' + key] = statistics[key]

            #print(self.processed_results)
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
            shots = int(result['{}_shots'.format(team_letter)])
            shots_on_target = int(result['{}_shots_on_target'.format(team_letter)])
#            shot_accuracy = shots_on_target / shots if shots > 0 else 0

            opposition_goals = int(result['{}_goal'.format(opposition_letter)])
            opposition_shots = int(result['{}_shots'.format(opposition_letter)])
            opposition_shots_on_target = int(result['{}_shots_on_target'.format(opposition_letter)])

            return {
                'wins': 1 if goals > opposition_goals else 0,
                'draws': 1 if goals == opposition_goals else 0,
                'losses': 1 if goals < opposition_goals else 0,
                'goals': goals,
                'opposition-goals': opposition_goals,
                'shots':shots,
                'shots_on_target':shots_on_target,
#                'shot_accuracy':shot_accuracy,
                'opposition_shots':opposition_shots,
                'opposition_shots_on_target':opposition_shots_on_target,
            }

        def reduce_fn(x, y):
            result = {}

            for key in x.keys():
                result[key] = x[key] + y[key]

            return result
        
        #print(reduce(reduce_fn, map(map_fn, recent_results[-matches:])))     
        return reduce(reduce_fn, map(map_fn, recent_results[-matches:]))

