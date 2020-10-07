

import numpy as np


def Uniqueness(ResponsesMatrix ,NBits ,NFiles):

    UniquenessValue = 0
    for i in range(NFiles):
        for j in range( i +1 ,NFiles):
            UniquenessValue += ((ResponsesMatrix[i] != ResponsesMatrix[j]).sum() ) *(100.0 /NBits)

    return UniquenessValue


def Uniformity(ResponsesMatrix ,NBits ,NFiles):

    UniformityMatrix = []
    for i in range(NFiles):
        UniformityMatrix.append(np.sum(ResponsesMatrix[i] ) *(100.0 /NBits))
    return UniformityMatrix


def BitAliasing(ResponsesMatrix, NFiles):

    BitAliasdingMatrix = np.sum(ResponsesMatrix, axis=0 ) *(100.0 /NFiles)
    return BitAliasdingMatrix

def Reliability(ResponsesMatrix, NBits ,NFiles):
    HD_Intra = 0
    for j in range(1 ,NFiles):
        HD_Intra += (sum([(ResponsesMatrix[0][b ] ^ResponsesMatrix[j][b]) for b in range(NBits)] ) *(100.0 /NBits))
    ReliabilityValue = 100 - (HD_Intra /NFiles)
    return ReliabilityValue
