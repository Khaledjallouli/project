import requests
from bs4 import BeautifulSoup
from datetime import datetime

# IDEA
# Download .csv file from https://www.football-data.co.uk/germanym.php (updated frequently, only contains past matches)
# add missing matches to database
# Fetch dates for future matches from https://www.worldfootball.net/all_matches/bundesliga-2019-2020/ (updated realtime, contains all matches)
# predict them based on database contents

def fetchdata(season): # season == "19-20"
    firstseasonyear = season.split('-')[0]
    secondseasonyear = season.split('-')[1]

    pastbettingdata = []
    matchdata = []

    #
    # BEGIN past betting data
    #

    URL = "https://www.football-data.co.uk/mmz4281/"+firstseasonyear+secondseasonyear+"/D1.csv" # taken from https://www.football-data.co.uk/germanym.php
    #                                          .../season/[D1|D2].csv                           #TODO: when D1 and when D2?
    response = requests.get(URL)
    page = response.text
    matches = page.split('\n')
    matches.pop(0) # remove header line
    for match in matches:
        if match != "":
            matchvalues = match.split(',')
            #print(match)
            #print(matchvalues[1]) # date
            #print(matchvalues[2]) # time
            pastbettingdataentry = [matchvalues[1],matchvalues[2],matchvalues[11],matchvalues[13],matchvalues[12],matchvalues[14],matchvalues[23],matchvalues[24],matchvalues[25]]
            #                      [date          ,time          ,home-shots     ,h-shots-target ,away-shots     ,a-shots-target ,odds-home      ,odds-draw      ,odds-away      ]
            pastbettingdata.append(pastbettingdataentry)

    #
    # END past betting data
    # BEGIN match data
    #

    URL = "https://www.worldfootball.net/all_matches/bundesliga-20"+firstseasonyear+"-20"+secondseasonyear+"/"
    response = requests.get(URL)
    #page = response.text.replace("\t","") # remove whitespace for better debugging
    soup = BeautifulSoup(response.text, "html.parser")

    date = "" # initialize date at current scope
    for tr in soup.findAll('tr'):
        if len(tr.findAll('form')) == 0 and len(tr.findAll('th')) == 0 and len(tr.findAll('td')) >=5: # only when tr does contain neither form nor tableheader AND contains enough 'td's

            if type(tr.findAll('td')[0].a) != type(None): # if (new) date is set
                date = tr.findAll('td')[0].a.string # extract date from html

            time = tr.findAll('td')[1].string # extract time from html

            firstteam = tr.findAll('td')[2].a['href'].split('/')[2] # extract first team from html

            secondteam = tr.findAll('td')[4].a['href'].split('/')[2] # extract second team from html

            finalresult = ""
            if type(tr.findAll('td')[5].a.string) != type(None) and tr.findAll('td')[5].a.string.strip() != "-:-": # if result is not yet added
                result = tr.findAll('td')[5].a.string.split() # extract match results from html
                finalresult = result[0] # extract final match result
                #halftimeresult = result[1].replace('(','').replace(')','') #  extract halftime result
            
            if finalresult != "": # only add past games for now
                matchdataentry = [date,time,firstteam,secondteam,finalresult] # time is currently unused
                matchdata.append(matchdataentry)
    
    #
    # END match data
    # BEGIN merging
    #

    matches = []

    for index, pbd in enumerate(pastbettingdata): # only past matches are added for now
        md = matchdata[index] #date,time,firstteam.secondteam,finalresult

        hg = md[4].split(':')[0]
        ag = md[4].split(':')[1]
        result = 'D'
        if hg > ag:
            result = 'H'
        elif hg < ag:
            result = 'A'

        match = []
        match.append(md[2]) # hometeam
        match.append(md[3]) # awayteam
        date = datetime.strptime(pbd[0], "%d/%m/%Y") # get date from string
        datenum = int(datetime.strftime(date, "%Y%m%d")) # number from date
        match.append(datenum) # date
        match.append(result) # result
        match.append(pbd[6]) # odds-home
        match.append(pbd[7]) # odds-draw
        match.append(pbd[8]) # odds-away
        match.append(hg) # home-goals
        match.append(pbd[2]) # home-shots
        match.append(pbd[3]) # home-shots-on-target
        match.append(ag) # away-goals
        match.append(pbd[4]) # away-shots
        match.append(pbd[5]) # away-shots-on-target

        matches.append(match)
    
    return matches

# testing:
def main():
    print(fetchdata("19-20")[0])
if __name__ == "__main__":
    main()