import pandas as pd
import requests


#Importação de todas as estatísticas dos jogadores da NBA da temporada 23-24

testurl = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS'

r = requests.get(url=testurl).json()

table_headers = r['resultSet']['headers']

players = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)

#Importando times

#Buzz (meu)
buzz_players = ['LaMelo Ball', 'Desmond Bane', 'Terry Rozier', 'Trey Murphy III', 'P.J. Washington', 'Brandon Miller', 'Jonas Valanciunas', 'Jose Alvarado', 'Xavier Tillman', 'Quentin Grimes']

buzz_team = pd.DataFrame()
temp_buzz = []

for i in buzz_players:
    stats = players[players['PLAYER'] == i]
    temp_buzz.append(stats)

buzz_team = pd.concat(temp_buzz, ignore_index=True)

buzz_team
#Faltou Trey Murphy no time
trey = players.loc[players['PLAYER'].str.contains('Trey', case=False)]

trey
#Adicionando Trey Murphy III no time (Colocando o nome certo na lista lá em cima)

#Hatter Team
royce = players.loc[players['PLAYER'].str.contains('Royce', case=False)]
royce

hatter_players = ['Kyrie Irving', 'CJ McCollum', 'Anthony Davis', 'Paul George', 'Jimmy Butler', 'Kelly Oubre Jr.', 'Pascal Siakam', 'Norman Powell', 'Damian Lillard', "Royce O'Neale"]

hatter_team = pd.DataFrame()
temp_hatter = []

for i in hatter_players:
    stats = players[players['PLAYER'] == i]
    temp_hatter.append(stats)

hatter_team = pd.concat(temp_hatter, ignore_index=True)

hatter_team

#Ersi576 Team
esri_players = ['Derrick White', 'Kentavious Caldwell-Pope', 'Buddy Hield', 'Kevin Durant', 'Jerami Grant', 'Draymond Green', 'Nikola Jokic', 'Eric Gordon', 'Malcolm Brogdon', 'Taurean Prince', 'Isaiah Hartenstein', 'Aaron Holiday', 'Garrison Mathews', 'Gary Payton II', 'Scotty Pippen Jr.', 'Damian Jones', 'Javon Freeman-Liberty', 'T.J. Warren']

esri_team = pd.DataFrame()
temp_esri = []

for i in esri_players:
    stats = players[players['PLAYER'] == i]
    temp_esri.append(stats)

esri_team = pd.concat(temp_esri, ignore_index=True)

esri_team.sort_values(by='RANK', ascending=True, inplace=True)

esri_team
# Scotty Pippen missing
scottie = players.loc[players['PLAYER'].str.contains('Pippen', case=False)]
scottie

#LUK Team
luk_players = ['Reggie Jackson', 'Andre Drummond', 'Tim Hardaway Jr.', 'Jeff Green', 'Derrick Jones Jr.', 'Jayson Tatum', 'LeBron James', 'Jrue Holiday', 'Kawhi Leonard', 'Caris LeVert', 'Bruce Brown', 'Larry Nance', 'Daniel Theis', 'Caleb Houston', 'Mo Bamba', 'Bojan Bogdanovic', 'Khris Middleton', 'Gordon Hayward', 'Isaiah Livers', 'Robert Williams III']

luk_team = pd.DataFrame()
temp_luk = []

for i in luk_players:
    stats = players[players['PLAYER'] == i]
    temp_luk.append(stats)

luk_team = pd.concat(temp_luk, ignore_index=True)

luk_team

luk_team.sort_values(by='RANK', ascending=True, inplace=True)

luk_team

#Pied1 Team
pied1_players = ['Dennis Schroder', 'Collin ']

pied1_team = pd.DataFrame()
temp_pied1 = []

for i in pied1_players:
    stats = players[players['PLAYER'] == i]
    temp_pied1.append(stats)

pied1_team = pd.concat(temp_pied1, ignore_index=True)

pied1_team

pied1_team.sort_values(by='RANK', ascending=True, inplace=True)

pied1_team

#Transformar Tabelas para 9cat
times = [buzz_team, hatter_team]

for df in times:
    df.drop(columns=['PLAYER_ID', 'RANK', 'TEAM_ID', 'AST_TOV', 'STL_TOV', 'EFF', 'TEAM', 'OREB', 'DREB', 'PF'], inplace=True)

buzz_team

#Transformar pontuação em médias

def calcular_medias(dataframe):
    # Calcula a média para cada coluna
    dataframe['REB'] /= dataframe['GP']
    dataframe['AST'] /= dataframe['GP']
    dataframe['STL'] /= dataframe['GP']
    dataframe['BLK'] /= dataframe['GP']
    dataframe['TOV'] /= dataframe['GP']
    dataframe['PTS'] /= dataframe['GP']
    return dataframe

# Chame a função para atualizar os valores no DataFrame
buzz_team = calcular_medias(buzz_team).round(1)
hatter_team = calcular_medias(hatter_team).round(1)

buzz_team
hatter_team

#Criando um dataframe com as médias dos times

# Removendo tipos strings
buzz_stats = buzz_team.drop(columns=['PLAYER']).mean()
buzz_stats['TEAM'] = 'Buzz'
hatter_stats = hatter_team.drop(columns=['PLAYER']).mean()
hatter_stats['TEAM'] = 'Hatter'
buzz_stats
hatter_stats

team_stats = [buzz_stats, hatter_stats]
team_stats

team_stats = pd.DataFrame(team_stats)

team_stats

#Exportar times
#buzz_team.to_csv('buzz_team.csv', index=False)
#hatter_team.to_csv('hatter_team.csv',index=False)