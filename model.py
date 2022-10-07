class Show:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @property
    def likes(self):
        return self._likes

    def send_like(self):
        self._likes += 1

class Film(Show):
    def __init__(self, name, year, duration):
        self._name = name.title()
        self.year = year
        self.duration = duration
        self._likes = 0

class TVShow(Show ):
    def __init__(self, name, year, seasons):
        self._name = name.title()
        self.year = year
        self.seasons = seasons
        self._likes = 0

avengers = Film('Avengers - infinity war', 2018, 160)
avengers.send_like()
avengers.send_like()

print(f'Name: {avengers.name} - Year: {avengers.year} - Duration: {avengers.duration} - Likes: {avengers.likes}')

atlanta = TVShow('Atlanta', 2018, 2)
atlanta.send_like()
atlanta.send_like()

print(f'Name: {atlanta.name} - Year: {atlanta.year} - Seasons: {atlanta.seasons} - Likes: {atlanta.likes}')

