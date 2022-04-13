import mysql.connector
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set_style("darkgrid")
sns.set(rc={'figure.figsize':(10,5)})
mydb = mysql.connector.connect(user='root', password='Berhed=1_2_3', host='localhost', database='NBAChamps')
mycursor = mydb.cursor()

# This file is responisble for fetching team data from the created database, and creating a figure using said data

years = ['\'00','\'01','\'02','\'03','\'04','\'05','\'06','\'07','\'08','\'09','\'10',
        '\'11','\'12','\'13','\'14','\'15','\'16','\'17','\'18','\'19','\'20','\'21']

#POINTS PER GAME
sql_ppg = mycursor.execute('SELECT championship_teams.ppg, team_year_avg.ppg '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
ppg_fetch = mycursor.fetchall()
ppg_data = []
for i in range(len(ppg_fetch)):
    temp1 = [float(ppg_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(ppg_fetch[i][1]), years[i], 'League']
    ppg_data.append(temp1)
    ppg_data.append(temp2)

ppg_graph = pd.DataFrame(data= ppg_data, columns=['ppg','year','team'])

fig = sns.lineplot(x="year", y="ppg",
             hue="team",
             data=ppg_graph)
plt.show()


# FEILD GOALS ATTEMPTED
sql_fga = mycursor.execute('SELECT championship_teams.fga, team_year_avg.fga '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
fga_fetch = mycursor.fetchall()
fga_data = []
for i in range(len(fga_fetch)):
    temp1 = [float(fga_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(fga_fetch[i][1]), years[i], 'League']
    fga_data.append(temp1)
    fga_data.append(temp2)

fga_graph = pd.DataFrame(data= fga_data, columns=['fga','year','team'])

sns.lineplot(x="year", y="fga",
             hue="team",
             data=fga_graph)
plt.show()


# FEILD GOAL PERCENTAGE
sql_fgp = mycursor.execute('SELECT championship_teams.fgp, team_year_avg.fgp '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
fgp_fetch = mycursor.fetchall()
fgp_data = []
for i in range(len(fgp_fetch)):
    temp1 = [float(fgp_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(fgp_fetch[i][1]), years[i], 'League']
    fgp_data.append(temp1)
    fgp_data.append(temp2)

fgp_graph = pd.DataFrame(data= fgp_data, columns=['fgp','year','team'])

sns.lineplot(x="year", y="fgp",
             hue="team",
             data=fgp_graph)
plt.show()


# 3 POINT ATTEMPTED
sql_3pa = mycursor.execute('SELECT championship_teams.3pa, team_year_avg.3pa '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
Tpa_fetch = mycursor.fetchall()
Tpa_data = []
for i in range(len(Tpa_fetch)):
    temp1 = [float(Tpa_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(Tpa_fetch[i][1]), years[i], 'League']
    Tpa_data.append(temp1)
    Tpa_data.append(temp2)

Tpa_graph = pd.DataFrame(data= Tpa_data, columns=['3pa','year','team'])

sns.lineplot(x="year", y="3pa",
             hue="team",
             data=Tpa_graph)
plt.show()


# 3 POINT PERCENTAGE 
sql_3pp = mycursor.execute('SELECT championship_teams.3pp, team_year_avg.3pp '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
Tpp_fetch = mycursor.fetchall()
Tpp_data = []
for i in range(len(Tpp_fetch)):
    temp1 = [float(Tpp_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(Tpp_fetch[i][1]), years[i], 'League']
    Tpp_data.append(temp1)
    Tpp_data.append(temp2)

Tpp_graph = pd.DataFrame(data= Tpp_data, columns=['3pp','year','team'])

sns.lineplot(x="year", y="3pp",
             hue="team",
             data=Tpp_graph)
plt.show()


# FREE THROWS ATTEMPTED
sql_fta = mycursor.execute('SELECT championship_teams.fta, team_year_avg.fta '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
fta_fetch = mycursor.fetchall()
fta_data = []
for i in range(len(fta_fetch)):
    temp1 = [float(fta_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(fta_fetch[i][1]), years[i], 'League']
    fta_data.append(temp1)
    fta_data.append(temp2)

fta_graph = pd.DataFrame(data= fta_data, columns=['fta','year','team'])

sns.lineplot(x="year", y="fta",
             hue="team",
             data=fta_graph)
plt.show()


# OFFENSIVE REBOUNDS
sql_oreb = mycursor.execute('SELECT championship_teams.oreb, team_year_avg.oreb '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
oreb_fetch = mycursor.fetchall()
oreb_data = []
for i in range(len(oreb_fetch)):
    temp1 = [float(oreb_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(oreb_fetch[i][1]), years[i], 'League']
    oreb_data.append(temp1)
    oreb_data.append(temp2)

oreb_graph = pd.DataFrame(data= oreb_data, columns=['oreb','year','team'])

sns.lineplot(x="year", y="oreb",
             hue="team",
             data=oreb_graph)
plt.show()


# TOTAL REBOUNDS
sql_reb = mycursor.execute('SELECT championship_teams.reb, team_year_avg.reb '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
reb_fetch = mycursor.fetchall()
reb_data = []
for i in range(len(reb_fetch)):
    temp1 = [float(reb_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(reb_fetch[i][1]), years[i], 'League']
    reb_data.append(temp1)
    reb_data.append(temp2)

reb_graph = pd.DataFrame(data= reb_data, columns=['reb','year','team'])

sns.lineplot(x="year", y="reb",
             hue="team",
             data=reb_graph)
plt.show()

# ASSITS
sql_ast = mycursor.execute('SELECT championship_teams.ast, team_year_avg.ast '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
ast_fetch = mycursor.fetchall()
ast_data = []
for i in range(len(ast_fetch)):
    temp1 = [float(ast_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(ast_fetch[i][1]), years[i], 'League']
    ast_data.append(temp1)
    ast_data.append(temp2)

ast_graph = pd.DataFrame(data= ast_data, columns=['ast','year','team'])

sns.lineplot(x="year", y="ast",
             hue="team",
             data=ast_graph)
plt.show()

# TURNOVERS
sql_tov = mycursor.execute('SELECT championship_teams.tov, team_year_avg.tov '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
tov_fetch = mycursor.fetchall()
tov_data = []
for i in range(len(tov_fetch)):
    temp1 = [float(tov_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(tov_fetch[i][1]), years[i], 'League']
    tov_data.append(temp1)
    tov_data.append(temp2)

tov_graph = pd.DataFrame(data= tov_data, columns=['tov','year','team'])

sns.lineplot(x="year", y="tov",
             hue="team",
             data=tov_graph)
plt.show()

# STEALS
sql_stl = mycursor.execute('SELECT championship_teams.stl, team_year_avg.stl '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
stl_fetch = mycursor.fetchall()
stl_data = []
for i in range(len(stl_fetch)):
    temp1 = [float(stl_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(stl_fetch[i][1]), years[i], 'League']
    stl_data.append(temp1)
    stl_data.append(temp2)

stl_graph = pd.DataFrame(data= stl_data, columns=['stl','year','team'])

sns.lineplot(x="year", y="stl",
             hue="team",
             data=stl_graph)
plt.show()

# BLOCKS
sql_blk = mycursor.execute('SELECT championship_teams.blk, team_year_avg.blk '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
blk_fetch = mycursor.fetchall()
blk_data = []
for i in range(len(blk_fetch)):
    temp1 = [float(blk_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(blk_fetch[i][1]), years[i], 'League']
    blk_data.append(temp1)
    blk_data.append(temp2)

blk_graph = pd.DataFrame(data= blk_data, columns=['blk','year','team'])

sns.lineplot(x="year", y="blk",
             hue="team",
             data=blk_graph)
plt.show()

# FOULS
sql_pf = mycursor.execute('SELECT championship_teams.pf, team_year_avg.pf '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
pf_fetch = mycursor.fetchall()
pf_data = []
for i in range(len(pf_fetch)):
    temp1 = [float(pf_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(pf_fetch[i][1]), years[i], 'League']
    pf_data.append(temp1)
    pf_data.append(temp2)

pf_graph = pd.DataFrame(data= pf_data, columns=['pf','year','team'])

sns.lineplot(x="year", y="pf",
             hue="team",
             data=pf_graph)
plt.show()

# HEIGHT
sql_height = mycursor.execute('SELECT championship_teams.height, team_year_avg.height '
                        'FROM championship_teams '
                        'INNER JOIN team_year_avg '
                        'ON championship_teams.year_id = team_year_avg.year_id')
height_fetch = mycursor.fetchall()
height_data = []
for i in range(len(height_fetch)):
    temp1 = [float(height_fetch[i][0]), years[i], 'Champs']
    temp2 = [float(height_fetch[i][1]), years[i], 'League']
    height_data.append(temp1)
    height_data.append(temp2)

height_graph = pd.DataFrame(data= height_data, columns=['height','year','team'])

sns.lineplot(x="year", y="height",
             hue="team",
             data=height_graph)
plt.show()

# SEED (BAR GRAPH)  
sql_seed = mycursor.execute('SELECT seed from championship_teams')
seed_fetch = mycursor.fetchall()
seed_data = []
occurences = {'1':0, '2':0, '3':0, '4':0}
for i in range(len(seed_fetch)):
    occurences[str(seed_fetch[i][0])] += 1

for i in range(len(seed_fetch)):
    temp = [seed_fetch[i][0], occurences[str(seed_fetch[i][0])]]
    seed_data.append(temp)

seed_graph = pd.DataFrame(data=seed_data, columns=['seed','number of occurences'])

sns.barplot(x="seed", y="number of occurences", data=seed_graph)
plt.show()

