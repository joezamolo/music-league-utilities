from lxml import html
import sys

XPATH_SONG_DIV = f"/html/body/div[1]/div[2]/div[2]/div/div"

file = sys.argv[1]
votes_html_raw = ""

with open(file) as f:
    votes_html_raw = f.read()

html_tree = html.fromstring(votes_html_raw)

submitter1 =   html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[1]/div[2]/div/div/div[3]/h6/text()")[0]
song_1 =       html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[1]/div[1]/div[2]/h6/a/text()")[0]
artist_1 =     html_tree.xpath(f"{XPATH_SONG_DIV}[4]/div[1]/div[1]/div[2]/p[1]/text()")[0]
submitter2 =   html_tree.xpath(f"{XPATH_SONG_DIV}[3]/div[1]/div[2]/div/div/div[3]/h6/text()")[0]

voter1 =       html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[1]/div[2]/b/text()")[0]
voter2 =       html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[2]/div[2]/b/text()")[0]
voter3 =       html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[3]/div[2]/b/text()")[0]

voter1_count = html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[1]/div[3]/h6/text()")[0]
voter2_count = html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[2]/div[3]/h6/text()")[0]
voter3_count = html_tree.xpath(f"{XPATH_SONG_DIV}[2]/div[3]/div[3]/div[3]/h6/text()")[0]


songs = html_tree.xpath(XPATH_SONG_DIV)
print(f"{len(songs)} songs")
for song in songs:
    submitter_html = song.xpath("./div[1]/div[2]/div/div/div[3]/h6/text()")
    song_title_html = song.xpath("./div[1]/div[1]/div[2]/h6/a/text()")
    artist_html = song.xpath("./div[1]/div[1]/div[2]/p[1]/text()")
    if submitter_html:
        print(f"{str(submitter_html[0])} - \"{str(song_title_html[0])}\" by {str(artist_html[0])}")
        
        votes_html = song.xpath("./div[3]/div")

        print(f"Votes:")
        vote_count = 0
        for vote_html in votes_html:
            voter_name_html = vote_html.xpath("./div[2]/b/text()")
            voter_vote_count_html = vote_html.xpath("./div[3]/h6/text()")
            if len(voter_vote_count_html) > 0:
                print(f"{voter_name_html[0]} - {voter_vote_count_html[0]} vote(s)")
                vote_count += int(voter_vote_count_html[0])
        
        print(f"{vote_count} total votes")
            




# parse input: link to HTML from round vote page

# Download HTML from the page

votes = []

# Loop over each song
    # Get submitter's name
    # Loop over voters
        # Get name of voter
        # Add voter to voter list
    # Add voter list to votes dict

# Write dict to a CSV file
