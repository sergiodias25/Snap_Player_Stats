import webbrowser
import assets.data_parser as data_parser
from datetime import datetime 

content = ""
screenWidthPrct = ''

def addPlayerData(template_file):
    global content
    content = template_file.read()
    content = content.replace("{{ playerName }}", data_parser.get_PlayerName())
    content = content.replace("{{ standing }}", str(data_parser.get_standing()))
    content = content.replace("{{ skillRating }}", str(data_parser.get_skillRating()))
    content = content.replace("{{ timeStarted }}", str(data_parser.get_timeStarted()))
    content = content.replace("{{ rankedCurrentLevel }}", str(data_parser.get_rankedCurrentLevel()))
    content = content.replace("{{ rankedCurrentLevelCubes }}", str(data_parser.get_rankedCurrentLevelCubes()))
    content = content.replace("{{ rankedMaxLevel }}", str(data_parser.get_rankedMaxLevel()))
    content = content.replace("{{ rankedMaxLevelCubes }}", str(data_parser.get_rankedMaxLevelCubes()))
    content = content.replace("{{ rankedCurrentWinStreak }}", str(data_parser.get_rankedCurrentWinStreak()))
    content = content.replace("{{ rankedGamesPlayedThisSeason }}", str(data_parser.get_rankedGamesPlayedThisSeason()))
    content = content.replace("{{ rankedWins }}", str(data_parser.get_rankedWins()))
    content = content.replace("{{ rankedLosses }}", str(data_parser.get_rankedLosses()))
    content = content.replace("{{ rankedTies }}", str(data_parser.get_rankedTies()))
    content = content.replace("{{ rankedWinPrct }}", str(data_parser.get_rankedWinPrct()))
    content = content.replace("{{ snaps }}", str(data_parser.get_Snaps()))
    content = content.replace("{{ concedes }}", str(data_parser.get_Concedes()))
    content = content.replace("{{ opponentConcedes }}", str(data_parser.get_opponentConcedes()))
    content = content.replace("{{ cardStatsBest }}", str(data_parser.get_BestCardStats()))
    content = content.replace("{{ cardStatsWorst }}", str(data_parser.get_WorstCardStats()))
    content = content.replace("{{ timeUpdated }}", str(data_parser.get_timeUpdated()))
    content = content.replace("{{ conquestPGPlayed }}", str(data_parser.get_conquestPGPlayed()))
    content = content.replace("{{ conquestPGStreak }}", str(data_parser.get_conquestPGStreak()))
    content = content.replace("{{ conquestSilverPlayed }}", str(data_parser.get_conquestSilverPlayed()))
    content = content.replace("{{ conquestSilverStreak }}", str(data_parser.get_conquestSilverStreak()))
    content = content.replace("{{ conquestGoldPlayed }}", str(data_parser.get_conquestGoldPlayed()))
    content = content.replace("{{ conquestGoldStreak }}", str(data_parser.get_conquestGoldStreak()))
    content = content.replace("{{ conquestInfinityPlayed }}", str(data_parser.get_conquestInfinityPlayed()))
    content = content.replace("{{ conquestInfinityStreak }}", str(data_parser.get_conquestInfinityStreak()))
    content = content.replace("{{ totalGoldSpent }}", str(data_parser.get_TotalGoldSpent()))
    content = content.replace("{{ totalCreditsSpent }}", str(data_parser.get_TotalCreditsSpent()))
    content = content.replace("{{ totalCollectorsTokensSpent }}", str(data_parser.get_TotalCollectorsTokensSpent()))
    content = content.replace("{{ battlePassesBought }}", str(data_parser.get_BattlePassesBought()))
    content = content.replace("{{ collectionLvl }}", str(data_parser.get_CollectionLvl()))
    content = content.replace("{{ avatarsOwned }}", str(data_parser.get_AvatarsOwned()))
    content = content.replace("{{ titlesOwned }}", str(data_parser.get_TitlesOwned()))
    content = content.replace("{{ cardBacksOwned }}", str(data_parser.get_CardBacksOwned()))
    content = content.replace("{{ cardsOwned }}", str(data_parser.get_CardsOwned()))
    content = content.replace("{{ cardSplits }}", str(data_parser.get_CardSplits()))
    content = content.replace("{{ variants }}", str(data_parser.get_Variants()))
    content = content.replace("{{ cardUnlockHistory }}", str(data_parser.get_CardUnlockHistory()))
    content = content.replace("{{ screenWidthPrct }}", screenWidthPrct)

if data_parser.isSystemWindows() or data_parser.isSystemLinux():
    screenWidthPrct = '70%'
if data_parser.isSystemMobile():
    screenWidthPrct = '95%'

fileNameToCreate = "stats_" + datetime.now().strftime("%d-%B-%Y-%H%M%S") + ".html"

with open("assets/template.html", encoding="utf-8-sig") as template_file:
    with open(fileNameToCreate, "w", encoding="utf-8") as generated_file:
        addPlayerData(template_file)
        
        generated_file.write(content)
        
        if data_parser.isSystemWindows() or data_parser.isSystemLinux():
           webbrowser.open_new_tab(fileNameToCreate)
        if data_parser.isSystemMobile():
            print("File stats.html generated in the project folder. Open it manually in your browser!")
