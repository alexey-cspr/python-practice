class VectorError(Exception):
    def __init__(self, msg):
        self.msg = msg

class Vector:

    def __init__(self, *values):
        for i in values:
            if not isinstance(i, int) and not isinstance(i, float):
                raise TypeError
        self.values = list()
        self.values.extend(values)
        self.length = len(values)
    
    def __len__(self):
        return self.length
    
    def __getitem__(self, pos):
        if pos < self.length:
            return self.values[pos]
        else:
            raise VectorError

    def __mul__(self, vector):
        if isinstance(vector, Vector):
            temp_vector = Vector()
            if self.length == vector.length:
                for i in range(self.length):
                    temp_vector.add_element(self.values[i] * vector.values[i])
                return temp_vector
            else :
                raise VectorError('differt lengths')
        else:
            for i in range(self.length):
                self.values[i] = self.values[i] * vector
            return self 

    def __sub__(self, vector):
        temp_vector = Vector()
        if self.length == vector.length:
            for i in range(self.length):
                    temp_vector.add_element(self.values[i] - vector.values[i])
            return temp_vector
        else:
            raise VectorError

    def __eq__(self, vector):
        # if self.values == vector.values:
        #     return True
        # else:
        #     return False
        return self.values == vector.values if True else False

    def __add__(self, vector):
        temp_vector = Vector()
        if self.length == vector.length:
            for i in range(self.length):
                temp_vector.add_element(self.values[i] + vector.values[i])
            return temp_vector
        else:
            raise VectorError('differt lengths')
    
    def add_element(self, element):
        self.values.append(element)
        self.length += 1
