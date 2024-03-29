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
        super().__init__(name, year)
        self.duration = duration

class TVShow(Show):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

avengers = Film('Avengers - infinity war', 2018, 160)
avengers.send_like()
avengers.send_like()

atlanta = TVShow('Atlanta', 2018, 2)
atlanta.send_like()
atlanta.send_like()


films_and_tvshows = [avengers, atlanta]

for show in films_and_tvshows:
    details = show.duration if hasattr(show, 'duration') else show.seasons
    print(f'{show.name} - {show.year} - {details} - {show.likes}')