import pandas as pd
import requests

#Importação de todas as estatísticas dos jogadores da NBA da temporada 23-24

testurl = 'https://stats.nba.com/stats/leagueLeaders?LeagueID=00&PerMode=Totals&Scope=S&Season=2023-24&SeasonType=Regular%20Season&StatCategory=PTS'

r = requests.get(url=testurl).json()

table_headers = r['resultSet']['headers']

players = pd.DataFrame(r['resultSet']['rowSet'], columns=table_headers)

#Times
luk_players = ['Reggie Jackson', 'Andre Drummond', 'Tim Hardaway Jr.', 'Jeff Green', 'Derrick Jones Jr.', 'Jayson Tatum', 'LeBron James', 'Jrue Holiday', 'Kawhi Leonard', 'Caris LeVert', 'Bruce Brown', 'Larry Nance', 'Daniel Theis', 'Caleb Houston', 'Mo Bamba', 'Bojan Bogdanovic', 'Khris Middleton', 'Gordon Hayward', 'Isaiah Livers', 'Robert Williams III']
buzz_players = ['LaMelo Ball', 'Desmond Bane', 'Terry Rozier', 'Trey Murphy III', 'P.J. Washington', 'Brandon Miller', 'Jonas Valanciunas', 'Jose Alvarado', 'Xavier Tillman', 'Quentin Grimes', 'Toumani Camara', 'Nicolas Batum', 'Josh Okogie', 'MarJon Beauchamp', 'Landry Shamet', 'Hunter Tyson', 'Amari Bailey']
hatter_players = ['Kyrie Irving', 'CJ McCollum', 'Anthony Davis', 'Paul George', 'Jimmy Butler', 'Kelly Oubre Jr.', 'Pascal Siakam', 'Norman Powell', 'Damian Lillard', "Royce O'Neale", 'Kelly Olynyk', 'Amir Coffey', 'Jordan Hawkins', 'Alec Burks', 'Dalano Banton', 'Chris Boucher', 'Monte Morris', 'Patty Mills', 'Vit Krejci']
esri_players = ['Derrick White', 'Kentavious Caldwell-Pope', 'Buddy Hield', 'Kevin Durant', 'Jerami Grant', 'Draymond Green', 'Nikola Jokic', 'Eric Gordon', 'Malcolm Brogdon', 'Taurean Prince', 'Isaiah Hartenstein', 'Aaron Holiday', 'Garrison Mathews', 'Gary Payton II', 'Scotty Pippen Jr.', 'Damian Jones', 'Javon Freeman-Liberty', 'T.J. Warren']
pied1_players = ['Dennis Schroder', 'Collin Sexton', "D'Angelo Russell", 'Grayson Allen', 'Bam Adebayo', 'Max Strus', 'Malachi Flynn', 'Devin Booker', 'John Collins', 'Simone Fontecchio', "Jae'Sean Tate", 'Keon Ellis', "De'Andre Hunter", 'Bradley Beal', 'OG Anunoby', 'Marvin Bagley', 'Tristan Thompson', 'Shake Milton', 'Thomas Bryant', 'Leaky Black', 'Kai Jones', 'Victor Oladipo']
savage31_players = ['Paul Reed', 'Domantas Sabonis', 'Josh Hart', 'Fred VanVleet', 'Alex Caruso', 'Nicolas Claxton', 'Kris Dunn', 'Matisse Thybulle', 'Sam Merril', 'Scottie Barnes', 'Vasilije Micic', 'Vince Williams', 'Chimezie Metu', 'Kobe Brown', 'Mitchell Robinson', 'Cody Martin', 'Jontay Porter', 'Luka Garza', 'Justin Champagnie', 'DeJon Jarreau']
thestove420_players = ['Georges Niang', 'Donte DiVincenzo', 'Bogdan Bogdanovic', 'Pat Connaughton', 'Drew Eubanks', 'T.J. McConnell', 'Andrew Wiggins', 'Jaren Jackson Jr.', 'Kevin Huerter', 'Luke Kornet', 'Justin Holiday', 'Jonathan Isaac', 'Trey Lyles', 'Jae Crowder', 'Evan Mobley', 'Jakob Poeltl', 'Josh Richardson', 'Luke Kennard', 'Robert Covington', 'Steven Adams']
eraserlawnmower_players = ['Ayo Dosunmu', 'Precious Achiuwa', 'Zion Williamson', 'Isaac Okoro', 'Kenrich Williams', 'Joe Ingles', 'Tyus Jones', 'Josh Green', 'Deandre Ayton', 'Donovan Mitchell', 'Gary Harris', 'Dean Wade', 'Nick Smith', 'Christian Wood', 'Jericho Sims', 'Jalen Wilson', 'Zach LaVine', 'Ben Simmons', 'Jalen Slawson', 'Lonzo Ball']
ect_players = ['Malik Beasley', 'Anthony Edwards', 'Terance Mann', 'Kevon Looney', 'Aaron Nesmith', 'Anthony Black', 'Dorian Finney-Smith', 'Miles McBride', "Day'Ron Sharpe", 'Gradey Dick', 'Ben Sheppard', 'AJ Green', 'Wendell Carter Jr.', 'Julian Strawther', 'Julius Randle', 'Davis Bertans', 'Patrick Baldwin', "De'Anthony Melton", 'Evan Fournier', 'Jarred Vanderbilt']
badsector_players = ['Austin Reaves', 'Jordan Poole', 'Aaron Wiggins', 'Grant Williams', "De'Aaron Fox", 'Daniel Gafford', 'Gary Trent Jr.', 'Jaylin Williams', 'Naji Marshall', 'David Roddy', 'Dario Saric', 'Santi Aldama', 'Kenyon Martin', 'Lauri Markkanen', 'Cam Reddish', 'Nassir Little']
kyletime_players = ['Naz Reid', 'Brook Lopez', 'Keegan Murray', 'Mike Conley', 'Jabari Walker', 'Victor Wembanyama', 'Duop Reath', 'Max Christie', 'Nick Richards', 'Amen Thompson', 'Dante Exum', 'Delon Wright', 'Bruno Fernando', 'Patrick Williams', 'Jared Butler', 'Dominick Barlow', 'Jarace Walker', 'Jett Howard', 'Jaylen Clark', 'Christian Koloko']
duncandunker_players = ['Christian Braun', 'Payton Pritchard', 'DeMar DeRozan', 'Luguentz Dort', 'Myles Turner', 'Clint Capela', 'Aaron Gordon', 'Luka Doncic', 'Russell Westbrook', 'JT Thor', 'Dennis Smith Jr.', 'Cam Whitmore', 'Nikola Jovic', 'Mason Plumlee', 'Anfernee Simons', 'DeAndre Jordan', 'Neemias Queta']
pittspipers_players = ['Moritz Wagner', 'Spencer Dinwiddie', 'Jonathan Kuminga', 'James Harden', 'Jaden McDaniels', 'Tyrese Maxey', 'Kris Murray', 'Troy Brown Jr.', 'Chris Paul', 'Torrey Craig', 'Jordan Nwora', 'Jalen McDaniels', 'Reggie Bullock', 'Markelle Fultz', 'Joel Embiid', 'Derrick Rose', 'Mojave King', 'Damion Lee']

#Armazenando os times em um dicionário
teams = {'luk_team': luk_players,'buzz_team': buzz_players,'hatter_team': hatter_players,'pied1_team': pied1_players, "savage31_team": savage31_players, 'thestove420_team': thestove420_players,'eraserlawnmower_team': eraserlawnmower_players,'ect_team': ect_players,'badsector_team': badsector_players,'kyletime_team': kyletime_players,'duncandunker_team': duncandunker_players,'pittspipers_team': pittspipers_players, 'esri_team': esri_players }
team_dfs = {}

#Rodando um for para armazenar os devidos jogadores em cada uma das keys
for team_name, team in teams.items():
    team_stats = pd.DataFrame()  # Initialize an empty DataFrame for each team
    print(f"Processing team: {team_name}")
    for player in team:
        player_stats = players[players['PLAYER'] == player]
        team_stats = pd.concat([team_stats, player_stats], ignore_index=True)
    team_dfs[team_name] = team_stats

#Verificando as keys do dicionário
if isinstance(team_dfs, dict):
    print(team_dfs.keys())

#Armazenando as keys em variáveis
for key in team_dfs.keys():
    globals()[key] = team_dfs[key]

#Alocando estas variáveis em Dataframes
buzz_team = pd.DataFrame(buzz_team)
buzz_team['team'] = 'Buzz'

luk_team = pd.DataFrame(luk_team)
luk_team['team'] = 'luk'

esri_team = pd.DataFrame(esri_team)
esri_team['team'] = 'esri'

pied1_team = pd.DataFrame(pied1_team)
pied1_team['team'] = 'pied1'

thestove420_team = pd.DataFrame(thestove420_team)
thestove420_team['team'] = 'thestove420'

eraserlawnmower_team = pd.DataFrame(eraserlawnmower_team)
eraserlawnmower_team['team'] = 'eraserlawnmower'

ect_team = pd.DataFrame(ect_team)
ect_team['team'] = 'ect'

badsector_team = pd.DataFrame(badsector_team)
badsector_team['team'] = 'badsector'

kyletime_team = pd.DataFrame(kyletime_team)
kyletime_team['team'] = 'kyletime'

duncandunker_team = pd.DataFrame(duncandunker_team)
duncandunker_team['team'] = 'duncandunker'

hatter_team = pd.DataFrame(hatter_team)
hatter_team['team'] = 'hatter'

kyletime_team = pd.DataFrame(kyletime_team)
kyletime_team['team'] = 'kyletime'

savage31_team = pd.DataFrame(savage31_team)
savage31_team['team'] = '31savage'

# List of dataframes
dataframes = [buzz_team, luk_team, esri_team, pied1_team, thestove420_team, eraserlawnmower_team, ect_team, badsector_team, kyletime_team, duncandunker_team, hatter_team, savage31_team]

# Concatenate all dataframes
box_and_one_dinasty = pd.concat(dataframes, ignore_index=True)

box_and_one_dinasty

#Exportar times
box_and_one_dinasty.to_csv('box_and_one_dinasty.csv', index=False)