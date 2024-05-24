from random import randint
from collections import Counter
from schedulers import *
import csv

def createList():
    x = randint(4, 15)
    list = []
    for i in range(x):
        list.append(randint(1,20))
    return list

def find_min_position(list):
    min_value = min(list)
    min_position = list.index(min_value)
    return min_position

def calculateBestPolicy(RR, MLQ, SJF):
    algoritmos = ['RR', 'MLQ', 'SJF']

    response = [RR[0], MLQ[0], SJF[0]]
    turnaround = [RR[1], MLQ[1], SJF[1]]
    wait = [RR[2], MLQ[2], SJF[2]]

    bests = [find_min_position(response), find_min_position(turnaround), find_min_position(wait)]
    
    if (bests.count(0))>=2:
        best = algoritmos[0]

    elif (bests.count(1))>=2:
        best = algoritmos[1]
    elif (bests.count(2))>=2:
        best = algoritmos[2]
    else:
        prom_RR = sum(RR)/3
        prom_MLQ = sum(MLQ)/3
        prom_SJF = sum(SJF)/3
        if prom_RR < prom_MLQ and prom_RR < prom_SJF:
            best = algoritmos[0]
        elif prom_MLQ < prom_RR and prom_MLQ < prom_SJF:
            best = algoritmos[1]
        else:
            best = algoritmos[2]

    return best

def calculateBestRR(RR):
    quantums = [1, 2, 4, 8]
    response = []
    turnaround = []
    wait = []
    for rr in RR:
        response.append(rr[0])
        turnaround.append(rr[1])
        wait.append(rr[2])

    bests = [find_min_position(response), find_min_position(turnaround), find_min_position(wait)]
    if (bests.count(0))>=2:
        best = 0
    elif (bests.count(1))>=2:
        best = 1
    elif (bests.count(2))>=2:
        best = 2
    else:
        best = 3

    return RR[best], quantums[best]

#ajusta la lista de jobs para que tenga una longitud de 15
def adjust_list(lst, length=15, fill_value=0):
    while len(lst) < length:
        lst.append(fill_value)
    return lst
    
def main():

    data_lists = []

    for i in range(1000):
        list = createList()
        n_Jobs = len(list)
        _RR  = []
        j = 1
        while j <= 8:
            _RR.append(RR(list, j))
            j *= 2
        best_RR, q = calculateBestRR(_RR)
        _MLQ = MLQ(list)
        _SJF = SJF(list)

        best = calculateBestPolicy(best_RR, _MLQ, _SJF)

        if best != 'RR':
            q = 0

        data = [n_Jobs] + adjust_list(list) + [best, q]
        data_lists.append(data)


        with open('output.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data_lists)


if __name__ == '__main__':
    main()