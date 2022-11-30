class Actor:
    def __init__(self, name):
        self.name = name
class Film:
    def __init__(self, name, starActor: Actor, visit):
        self.name = name
        self.starActor = starActor
        self.visit = visit
        self.totalVisitors = self.calculateTotalVisitors()
    def calculateTotalVisitors(self):
        return sum(self.visit)
    def __gt__(self, other):
        return self.totalVisitors > other.totalVisitors
    def __ge__(self, other):
        return self.totalVisitors >= other.totalVisitors
    def __le__(self, other):
        return self.totalVisitors >= other.totalVisitors
    def __lt__(self, other):
        return self.totalVisitors < other.totalVisitors
    def __eq__(self, other):
        if isinstance(other, Film):
            return self.totalVisitors == other.totalVisitors
        elif isinstance(other, Actor):
            return self.starActor.name == other.name
        else:
            return self.name == other

class FilmDB:
    def __init__(self) -> None:
        self.films = []
    def addFilm(self, film: Film) -> None:
        self.films.append(film)
    def printTotalVisitors(self, filmName: str) -> str:
        for film in self.films:
            if film == filmName:
                return f'{film.name}: {film.totalVisitors}'
    def sortFilms(self) -> str:
        self.films.sort(reverse=True)
        buf = ""
        i = 1
        for film in self.films:
            buf += f"{i}. {film.name}: {film.totalVisitors}\n"
            i += 1
        return buf
    def printTable(self, n: int) -> str:
        buf = "Popularity ratings:\n"
        for i in range(0, n):
            buf += f"{i}. {self.films[i].name}: {self.films[i].totalVisitors}\n"
        return buf
    def numFilms(self, starName: str) -> str:
        n=0
        f = []
        starName = Actor(starName)
        for film in self.films:
            if film == starName:
                n += 1
                f.append(film.name)
        buf = f"Actor: \"{starName.name}\" played in {n} films:\n"
        buf += "\n".join(f)
        return buf

db = FilmDB()
for _ in range(4):
    db.addFilm(Film(input("Film name? > "),Actor(input("Hviezdna rola? > ")),[int(input(f"Návštevnosť za {x}. týždeň? > ")) for x in range(1,5)]))


print(db.printTotalVisitors("nemo"))
print(db.sortFilms())
print(db.numFilms("Nic"))




