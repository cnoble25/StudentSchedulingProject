from Student import Student
from ClassSection import ClassSection
import random
import math

def get_percent():
    counter = 0
    for t in Student.all_students:
        SL = 0
        for i in t.schedule.values():

            if i is not None:
                # print(i.name)
                SL += 1

        # print(f'{len(x.requests)} , {SL}')
        if len(t.requests) <= SL:
            counter += 1
    return counter / len(Student.all_students)


def reset():
    for p in Student.all_students:
        p.schedule = dict.fromkeys(p.schedule, None)
    for y in ClassSection.all_classes.values():
        for i in y:
            i.roster = []


def try_for_percent(percent):
    p = get_percent()

    while p <= percent:
        for m in Student.all_students:
            random.shuffle(m.requests)
        reset()

        for k in range(len(Student.all_students)):
            Student.all_students[k].make_schedule()
        p = get_percent()
        print(p)
    return p



if __name__ == '__main__':
    ClassSection.instantiate_from_csv('sample class data.csv')
    Student.instantiate_from_csv('sample student data no names.csv')
    for x in range(len(Student.all_students)):
        Student.all_students[x].make_schedule()
    while get_percent() < 0.63:
        reset()
        random.shuffle(Student.all_students)
        for x in range(len(Student.all_students)):
            Student.all_students[x].make_schedule()

    for x in range(len(Student.all_students)):
        print(Student.all_students[x].repr())

    for x in range(3):
        print()

    for x in ClassSection.all_classes.values():
        for i in x:
            names = []
            for z in i.roster:
                names.append(z.name)
            print(f'{i.name}, {i.teacher}, {i.period}, size of class: {len(names)}')

    print(f'{math.ceil(get_percent()*100)} %')