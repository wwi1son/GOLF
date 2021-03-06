from bs4 import BeautifulSoup
import urllib 

class pageParser(object):
    def __init__(self, url="http://espn.go.com/golf/players"):
        self.url = url
        self.page = self.get_page()
        self.rows = self.get_player_entries()
        self.playerMd = self.get_player_md()

    def get_page(self):
        response = urllib.urlopen(self.url)
        soup = BeautifulSoup(response)
        soup.unicode
        return soup

    def get_player_entries(self):
        div = self.page.find(id='my-players-table')
        table = div.table
        trlist = table.find_all('tr')
        rows = []
        for tr in trlist:
            if tr['class'][0] in ('evenrow', 'oddrow'):
                rows.append(tr)
        return rows

    def get_player_md(self):
        playerMd = {}
        for row in self.rows:
            playerDict = {}
            playerKey = (row['class'][1].split('-'))[-1]
            link, country = row.find_all('td')
            playerDict['playerCountry']= country.get_text()
            playerDict['playerLink'] = link.a['href']
            playerMd[playerKey] = playerDict
        return playerMd

pp = pageParser()