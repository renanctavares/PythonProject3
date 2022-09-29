class Film:
    def __init__(self, name, year, duration):
        self.name = name.title()
        self.year = year
        self.duration = duration
        self.likes = 0

    def send_like(self):
        self.likes += 1

class TVShow:
    def __init__(self, name, year, seasons):
        self.name = name.title()
        self.year = year
        self.seasons = seasons
        self.likes = 0

    def send_like(self):
        self.likes += 1

avengers = Film('Avengers - infinity war', 2018, 160)
avengers.send_like()
avengers.send_like()

print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration} - Likes: {avengers.likes}')

atlanta = TVShow('Atlanta', 2018, 2)
atlanta.send_like()
atlanta.send_like()

print(f'Name: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons} - Likes: {atlanta.likes}')

