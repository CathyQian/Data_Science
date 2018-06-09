class Garden(object):
    default_students = ['Alice', 'Bob', 'Charlie', 'David','Eve', 'Fred', 'Ginny', 'Harriet',
                'Ileana', 'Joseph', 'Kincaid', 'Larry']
    mapping = {'V': 'Violets', 'R':'Radishes', 'C':'Clover', 'G':'Grass'}

    def __init__(self, diagram, students = default_students):
        self.diagram = diagram.split('\n')
        self.students = sorted(students)

    def plants(self, student):
        if student in self.students:
            idx = self.students.index(student)
            flower_str = [self.diagram[0][2*idx], self.diagram[0][2*idx + 1],
                          self.diagram[1][2*idx], self.diagram[1][2*idx + 1]]
            flowers = []
            for f in flower_str:
                try:
                    flowers.append(self.mapping[f])
                except KeyError:
                    print('Input string does not represent the right flower!')
            return flowers
        else:
            raise Exception('The input student name is not in the students list.')
