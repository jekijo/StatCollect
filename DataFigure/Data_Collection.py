import requests
from bs4 import BeautifulSoup
import mysql.connector
#This file is responsible for the data collected for this project

#Defining Indexes of stats that are collected so I can recall them in order easier (this is the order in which the website used has listed them)
FG = 0
FGA = 1
FGP = 2
ThreeP = 3
ThreePA = 4
ThreePP = 5
TwP = 6
TwPA = 7
TwPP = 8
FT = 9
FTA = 10
FTP = 11
ORB = 12
DRB = 13
TRB = 14
AST = 15
STL = 16
BLK = 17
TOV = 18
PF = 19
PPG = 20

#Creating MySQL cursor
mydb = mysql.connector.connect(user='root', password='Berhed=1_2_3', host='localhost', database='NBAChamps')
mycursor = mydb.cursor()

#Years that I will be pulling data on
years = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010',
         '2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']
#seeding gathered manually based on the website used to collect data (teams were organized by ppg per each year)
seed = [6, 3, 3, 12, 24, 18, 6, 14, 11, 3, 12, 11, 7, 5, 6, 1, 8, 1, 1, 8, 11, 1]

#Webscraping data for team averages for each year, puts all relevant data in a list, index from variables
for i in range(len(years)):
    url = f"https://www.basketball-reference.com/leagues/NBA_{years[i]}.html"
    league_avg = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    stats = soup.findChildren('table')
    if i < 16:
        table = stats[2]
    else:
        table = stats[4]
    if i < 5:
        row = table.findChildren('tr')[30]
    else:
        row = table.findChildren('tr')[31]
    for val in row:
        n_val = val.string
        league_avg.append(n_val)
    league_avg = league_avg[-21:]
    #This pushes the data to the MySQL database
    mycursor.execute("INSERT INTO team_year_avg(ppg, fgm, fga, fgp, 3pm, 3pa, 3pp, fta, ftm, ftp," 
                    "oreb, dreb, reb, ast, tov, stl, blk, pf)" 
                    f" VALUES({league_avg[PPG]}, {league_avg[FG]}, {league_avg[FGA]}, {league_avg[FGP]}, {league_avg[ThreeP]}, "
                    f"{league_avg[ThreePA]}, {league_avg[ThreePP]}, {league_avg[FT]}, {league_avg[FTA]}, {league_avg[FTP]}, "
                    f"{league_avg[ORB]}, {league_avg[DRB]}, {league_avg[TRB]}, {league_avg[AST]}, {league_avg[TOV]}, "
                    f"{league_avg[STL]}, {league_avg[BLK]}, {league_avg[PF]})")
    mydb.commit()

#Webscraping data for champion team averages for each year, puts all relevant data in a list, index from variables
for i in range(len(years)):
    url = f"https://www.basketball-reference.com/leagues/NBA_{years[i]}.html"
    league_avg = []
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    stats = soup.findChildren('table')
    if i < 16:
        table = stats[2]
    else:
        table = stats[4]
    row = table.findChildren('tr')[seed[i]]
    for val in row:
        n_val = val.string
        league_avg.append(n_val)
    league_avg = league_avg[-21:]
    #This pushes the data to the MySQL database
    mycursor.execute("INSERT INTO championship_teams(ppg, fgm, fga, fgp, 3pm, 3pa, 3pp, fta, ftm, ftp," 
                    "oreb, dreb, reb, ast, tov, stl, blk, pf)" 
                    f" VALUES({league_avg[PPG]}, {league_avg[FG]}, {league_avg[FGA]}, {league_avg[FGP]}, {league_avg[ThreeP]}, "
                    f"{league_avg[ThreePA]}, {league_avg[ThreePP]}, {league_avg[FT]}, {league_avg[FTA]}, {league_avg[FTP]}, "
                    f"{league_avg[ORB]}, {league_avg[DRB]}, {league_avg[TRB]}, {league_avg[AST]}, {league_avg[TOV]}, "
                    f"{league_avg[STL]}, {league_avg[BLK]}, {league_avg[PF]})")
    mydb.commit()

#pushing team name and conference seed to the championship team table
team_seed_list = [['LAL',1], ['LAL',2], ['LAL',3], ['SAS',1], ['DET',3], ['SAS',2], ['MIA',2],
          ['SAS',3], ['BOS',1], ['LAL',1], ['LAL',1], ['DAL',3], ['MIA',2], ['MIA',1],
          ['SAS',1], ['GSW',1], ['CLE',1], ['GSW',1], ['GSW',2], ['TOR',2], ['LAL',1], ['MIL',3]]
for i in range(len(team_seed_list)):
    mycursor.execute(f"UPDATE championship_teams SET team = '{team_seed_list[i][0]}', seed = {team_seed_list[i][1]} WHERE (year_id={i+1})")
    mydb.commit()

#This was used to gather info about the average height for all the champion teams
teams = ['LAL', 'LAL', 'LAL', 'SAS', 'DET', 'SAS', 'MIA', 'SAS', 'BOS', 'LAL', 'LAL',
         'DAL', 'MIA', 'MIA', 'SAS', 'GSW', 'CLE', 'GSW', 'GSW', 'TOR', 'LAL', 'MIL']
champ_height = []

#This function turns a list of heights in the format of 'ft-inch' into an average of total inches
def avg_inches(l):
    inch_total = 0
    for i in l:
        ft,inch = i.split('-')
        ft = int(ft)*12
        inch_total += int(inch)
        inch_total += ft
    avg = inch_total/len(l)
    return avg
#this loop collected the average of all heights of each championship team

for i in range(len(years)):
    temp_h = []
    url = f"https://www.basketball-reference.com/teams/{teams[i]}/{years[i]}.html"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'lxml')
    stats = soup.findChildren('table')
    height_table = stats[0]
    tbody = height_table.findChildren('tr')
    for i in range(1,len(tbody)):
        trow = tbody[i]
        h = trow.find('td',{'data-stat':'height'})
        temp_h.append(h.text)
    champ_height.append(avg_inches(temp_h))


#This is the list of the average height of all NBA players from the years 2000-2021, this data was collected manually and placed in the following list
avg_height_list = [78.93, 78.90, 78.93, 79.17, 79.20, 79.13, 79.05, 78.94, 78.99, 79.12, 78.98, 79.12,
                   78.94, 78.86, 78.84, 78.72, 78.73, 78.84, 78.55, 78.58, 78.45, 78.33]

#Once the data was collected, this was used to push the data to the database
for i in range(len(years)):
    mycursor.execute(f"UPDATE championship_teams SET height = '{champ_height[i]}' WHERE (year_id={i+1})")
    mycursor.execute(f"UPDATE team_year_avg SET height = '{avg_height_list[i]}' WHERE (year_id={i+1})")
    mydb.commit()