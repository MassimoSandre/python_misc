import math
from decimal import Decimal
from unicodedata import decimal

class Pendulum():
    def __init__(self, n, g=9.8) -> None:
        self.thetas = [Decimal(3.1415/2)]*n
        self.thetaDots = [Decimal(0)]*n
        self.n = n
        self.g = -g


    def __matrix_vector_mul(self, matrix, vector):
        res = []
        for row in matrix:
            res.append(0)
            
            for i,col in enumerate(row):
                res[-1] += Decimal(col)*Decimal(vector[i])

        return res

    def A(self, thetas):
        mat = []
        for i in range(self.n):
            mat.append([])
            for j in range(self.n):
                mat[-1].append((self.n - max(i,j)) * math.cos(thetas[i] - thetas[j]))

        return mat.copy()
        

    def b(self, thetas, thetaDots):
        v = []
        for i in range(self.n):
            bi = 0
            for j in range(self.n):
                bi -= Decimal((self.n - max(i,j))) * Decimal(math.sin(thetas[i] - thetas[j])) * (thetaDots[j] ** 2)
            
            bi -= Decimal(self.g * (self.n-i)) * Decimal(math.sin(thetas[i]))
            v.append(bi)
        return v.copy()


    def f(self, thetas, thetaDots):
        A = self.A(thetas)
        b = self.b(thetas,thetaDots)
        return [thetaDots, self.__matrix_vector_mul(A,b)]

    def RK4(self, dt, thetas, thetaDots):
        dt = Decimal(dt)
        k1 = self.f(thetas, thetaDots)
        k2 = self.f([thetas[i] + k1[0][i]*dt/2 for i in range(self.n)], [thetaDots[i] + k1[1][i]*dt/2 for i in range(self.n)])
        k3 = self.f([thetas[i] + k2[0][i]*dt/2 for i in range(self.n)], [thetaDots[i] + k2[1][i]*dt/2 for i in range(self.n)])
        k4 = self.f([thetas[i] + k3[0][i]*dt for i in range(self.n)], [thetaDots[i] + k3[1][i]*dt for i in range(self.n)])

        thetaDeltas = [(k1[0][i] + k2[0][i]*2 + k3[0][i]*2 + k4[0][i])*dt/6 for i in range(self.n)]
        thetaDotDeltas = [(k1[1][i] + k2[1][i]*2 + k3[1][i]*2 + k4[1][i])*dt/6 for i in range(self.n)]

        return [[thetas[i]+thetaDeltas[i] for i in range(self.n)], [thetaDots[i]+thetaDotDeltas[i] for i in range(self.n)]]

    def update(self,dt):
        new_state = self.RK4(dt, self.thetas, self.thetaDots)
        self.thetas = new_state[0]
        self.thetaDots = new_state[1]

    def get_coordinates(self):
        x,y = 0,0
        coords = []
        for i in range(self.n):
            theta = self.thetas[i]
            x += math.sin(theta)
            y += math.cos(theta)
            coords.append((x,y))
        return coords.copy()