import numpy as np


class Kalman:
    def __init__(self, F, Q, H, R):
        self.n = F.shape[1]
        self.m = H.shape[1]
        self.F = F
        self.H = H
        self.Q = Q
        self.R = R
        self.P = np.eye(self.n)
        self.x = np.zeros((self.n, 1))
        self.I = np.eye(self.n)

    def predecir(self):
        self.x = np.dot(self.F, self.x)
        self.P = np.dot(np.dot(self.F, self.P), self.F.T) + self.Q
        return self.x

    def actualizar(self, z):
        y = z - np.dot(self.H, self.x)
        S = self.R + np.dot(self.H, np.dot(self.P, self.H.T))
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        #print('K = ', K)
        self.x = self.x + np.dot(K, y)
        self.P = np.dot(self.I - np.dot(K, self.H), self.P)
        return K #Es la ganancia de Kalman