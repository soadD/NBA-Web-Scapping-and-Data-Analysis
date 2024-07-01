
import pandas as pd
import requests
import time
import numpy as np

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


buzz_team
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

#Transformar Tabelas para 9cat
times = [buzz_team, hatter_team]

for df in times:
    df.drop(columns=['PLAYER_ID', 'RANK', 'TEAM_ID', 'AST_TOV', 'STL_TOV', 'EFF', 'TEAM', 'OREB', 'DREB', 'PF'], inplace=True)

buzz_team

#Exportar times
buzz_team.to_csv('buzz_team.csv', index=False)
hatter_team.to_csv('haater_team.csv',index=False)