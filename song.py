import pandas as pd

songlist = pd.read_csv('songdata.csv', header=0)
pd.set_option('display.max_colwidth', -1)

titles = songlist[songlist['song'].str.contains('baby|Baby')]
lyrics = songlist[songlist['text'].str.contains('baby|Baby')]
babysongs = pd.concat([lyrics, titles])
babysongs.reset_index(inplace = True)
babysongs.drop(['index', 'link'], axis=1, inplace=True)

index = -1
for row in babysongs['text']:
    newText = ""
    index += 1
    for line in row.splitlines():
        if 'baby' in line.lower():
            newText += line + "<br>"
    babysongs.set_value(index, 'text', newText)
    
babysongs.replace({'text': 'baby'} , {'text': '<b>baby</b>'}, inplace=True, regex=True)
babysongs.replace({'text': 'Baby'} , {'text': '<b>Baby</b>'}, inplace=True, regex=True)
babysongs.replace({'song': 'baby'} , {'song': '<b>baby</b>'}, inplace=True, regex=True)
babysongs.replace({'song': 'Baby'} , {'song': '<b>Baby</b>'}, inplace=True, regex=True)
babysongs.to_html('babysongs.html', escape=False)
