from utils import *


class Obj(object):
    def __init__(self, filename):
        with open(filename) as f:
            self.lines = f.read().splitlines()

        self.vertices = []
        self.faces = []
        self.tvertices = []
        self.read()

    def read(self):
        for line in self.lines:
            if line:
                prefix, value = line.split(' ', 1)

                if prefix == 'v':
                    self.vertices.append(list(map(float, value.split(' '))))
                elif prefix == 'f':
                    self.faces.append([list(map(int, face.split('/')))
                                      for face in value.split(' ')])
                if prefix == 'vt':
                    vertice = list(map(float, value.split(' ')))
                    if(len(vertice) == 2):
                        vertice.append(0)
                    self.tvertices.append(vertice)
