


class Student:
    def __init__(self, name: str, grades: list[int]) -> None:
        self.name = name
        self.grades = grades
        self.avg = sum(grades) / len(grades)
        self.prospech = self.getProspech()

    def getProspech(self) -> str:
        if self.avg < 1.5 and len(self.grades) != len(set(self.grades + [3,4,5])):
            return "Vyznamenanie"
        elif self.avg < 2 and len(self.grades) != len(set(self.grades + [4,5])):
            return "Veľmi dobre"
        elif 5 not in self.grades:
            return "Prospel"
        else:
            return "Neporospel"

    def __repr__(self) -> str:
        return f'{self.name}: {str(len(self.grades))} známok | priemer: {str(self.avg)} | {self.prospech}'
st = []

for _ in range(2):
    gr = []
    mn = input("Meno? > ")
    while (x:=input("Známka? > ")) != "0":
        gr.append(x)
    st.append(Student(mn, list(map(int, gr))))

for s in st:
    print(s)

