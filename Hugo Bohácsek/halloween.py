class Trip():
    def __init__(self, date: str, distance: float, time: int, target: str) -> None:
        self.date = date
        self.distance = distance
        self.time = time
        self.target = target
        self.avgSpeed = self.getAvgSpeed()
    def formatTime(self) -> str:
        return str(self.time//60) + ":" + str(self.time % 60)
    def getAvgSpeed(self) -> int:
        return self.distance / (self.time / 60)
    def __repr__(self) -> str:
        return f'{self.date}-> {str(self.distance)}km | {self.formatTime()} | {str(self.avgSpeed)}km/h | {self.target}'


a = [Trip(input("Dátum? > "), float(input("Vzdialenosť? > ")), int(input("Čas? > ")), input("Destinácia? > ")) for _ in range(2)]

for t in a:
    print(t)


