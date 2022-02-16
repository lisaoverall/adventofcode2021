from io import StringIO
from math import prod

test_data = 'C0015000016115A2E0802F182340'

with open('input.txt') as f:
    data = f.read().strip()

def make_buf(d):
    return StringIO(''.join(f'{int(char, 16):04b}' for char in d))

test_data = make_buf(test_data)
data = make_buf(data)

class Packet:
    def __init__(self, stream):
        self.stream = stream
        self.version = int(self.stream.read(3), 2)
        self.type_id= int(self.stream.read(3), 2)
        self.subpackets = [] if self.type_id == 4 else self.read_subpackets()
        self.value = {
            0: self.sum,
            1: self.prod,
            2: self.min,
            3: self.max,
            4: self.read_literal,
            5: self.greater_than,
            6: self.less_than,
            7: self.equal
        }[self.type_id]()
        self.versions_sum = sum(self.versions())

    def read_literal(self):
        heading = literal = ''
        while heading != '0':
            heading = self.stream.read(1)
            literal += self.stream.read(4)
        return int(literal, 2)

    def read_subpackets(self):
        length_type_id = self.stream.read(1)
        if length_type_id == '0':
            total_length = int(self.stream.read(15), 2)
            end = self.stream.tell() + total_length
            subpackets = []
            while self.stream.tell() < end:
                subpackets.append(Packet(stream=self.stream))
        else:
            num_subpackets = int(self.stream.read(11), 2)
            subpackets = [Packet(stream=self.stream) for _ in range(num_subpackets)]
        return subpackets 

    def sum(self):
        return sum(subpacket.value for subpacket in self.subpackets)

    def prod(self):
        return prod(subpacket.value for subpacket in self.subpackets)

    def min(self):
        return min(subpacket.value for subpacket in self.subpackets)

    def max(self):
        return max(subpacket.value for subpacket in self.subpackets)

    def greater_than(self):
        first, second, *_ = self.subpackets
        return int(first.value > second.value)

    def less_than(self):
        first, second, *_ = self.subpackets
        return int(first.value < second.value)

    def equal(self):
        first, second, *_ = self.subpackets
        return int(first.value == second.value)
                
    def versions(self):
        yield self.version
        for subpacket in self.subpackets:
            yield from subpacket.versions()
    
    def __repr__(self):
        return f'Packet(version={self.version}, type_id={self.type_id}, value={self.value}, subpackets={self.subpackets})'


test = Packet(test_data)
# decodes to:
# (10 + 11) + (12 + 13) = 21 + 25 = 46
assert test.versions_sum == 23
assert test.value == 46

solution = Packet(data)
print('Part 1:', solution.versions_sum)
print('Part 2:', solution.value)
