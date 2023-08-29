import csv
from ClassSection import ClassSection
import random


class Student:
    all_students = []

    def __init__(self, Name, Grade, Advisor, Requests: list):
        self.name = Name
        self.grade = Grade
        self.advisor = Advisor
        self.requests = Requests
        self.requests = [i for i in self.requests if i != '']
        self.schedule = {"Q1/3 P1": None,
                         "Q1/3 P2": None,
                         "Q1/3 P3": None,
                         "Q1/3 P4": None,
                         "Q2/4 P1": None,
                         "Q2/4 P2": None,
                         "Q2/4 P3": None,
                         "Q2/4 P4": None,
                         }
        Student.all_students.append(self)

    # def make_schedule(self):
    #     for i in self.requests:
    #         for x in ClassSection.all_classes[i]:
    #             if len(x.roster) < x.size and self.schedule[x.period] is None:
    #                 check = 0
    #                 for z in self.schedule.values():
    #                     if z is not None and x is not None:
    #                         if x.name == z.name:
    #                             check += 1
    #                 if check == 0:
    #                     self.schedule[x.period] = x
    #                     x.roster.append(self)

    def reset_rest_roster(self):
        for x in self.schedule.values():
            if x is not None:
                x.roster.remove(self)

    def make_schedule(self):
        for i in self.requests:
            for x in ClassSection.all_classes[i]:
                if len(x.roster) < x.size and self.schedule[x.period] is None:
                    check = 0
                    for z in self.schedule.values():
                        if z is not None and x is not None:
                            if x.name == z.name:
                                check += 1
                    if check == 0:
                        self.schedule[x.period] = x
                        x.roster.append(self)
        SL = 0
        for p in self.schedule.values():
            if p is not None:
                SL += 1
        if SL != len(self.requests):
            try:
                random.shuffle(self.requests)
                self.reset_rest_roster()
                self.schedule = dict.fromkeys(self.schedule, None)
                self.make_schedule()
            except:
                pass

    def repr(self):
        return f'{self.name}: \n\t' \
               f'Period 1 (1/3): {self.schedule["Q1/3 P1"]}\n\t' \
               f'Period 2 (1/3): {self.schedule["Q1/3 P2"]}\n\t' \
               f'Period 3 (1/3): {self.schedule["Q1/3 P3"]}\n\t' \
               f'Period 4 (1/3): {self.schedule["Q1/3 P4"]}\n\t' \
               f'Period 1 (2/4): {self.schedule["Q2/4 P1"]}\n\t' \
               f'Period 2 (2/4): {self.schedule["Q2/4 P2"]}\n\t' \
               f'Period 3 (2/4): {self.schedule["Q2/4 P3"]}\n\t' \
               f'Period 4 (2/4): {self.schedule["Q2/4 P4"]}\n\t'

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Student(
                Name=item.get('name'),
                Grade=item.get('grade'),
                Advisor=item.get('advisor'),
                Requests=[item.get('req1'), item.get('req2'), item.get('req3'), item.get('req4'), item.get('req5'),
                          item.get('req6'), item.get('req7'), item.get('req8'), item.get('req9')]
            )
