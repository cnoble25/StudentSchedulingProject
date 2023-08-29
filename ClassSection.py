import csv


class ClassSection:
    all_classes = {}

    def __init__(self, Name, Teacher, Period, Size):
        self.name = Name
        self.teacher = Teacher
        self.period = Period
        self.size = Size
        self.roster = []
        try:
            ClassSection.all_classes[self.name].append(self)
        except:
            ClassSection.all_classes[self.name] = []
            ClassSection.all_classes[self.name].append(self)

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            ClassSection(
                Name=item.get('name'),
                Teacher=item.get('teacher'),
                Period=item.get('period'),
                Size=int(item.get('class size'))
            )