# First create a City class that will allow us
# to create and handle our cities.
# Create Population
# pip install numpy pandas matplotlib

import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt

from tkinter import Tk, Canvas, Frame, BOTH, Text

import math


class City:

    def __init__(self, x, y):

        self.x = x
        self.y = y

    def distance(self, city):

        xDis = abs(
            self.x - city.x
        )

        yDis = abs(
            self.y - city.y
        )

        return np.sqrt(
            (xDis ** 2) +
            (yDis ** 2)
        )

    def __repr__(self):

        return f"({self.x},{self.y})"


class Fitness:

    def __init__(self, route):

        self.route = route
        self.distance = 0
        self.fitness = 0.0

    def routeDistance(self):

        if self.distance == 0:

            pathDistance = 0

            for i in range(
                len(self.route)
            ):

                fromCity = self.route[i]

                toCity = (
                    self.route[i + 1]
                    if i + 1 < len(self.route)
                    else self.route[0]
                )

                pathDistance += (
                    fromCity.distance(toCity)
                )

            self.distance = pathDistance

        return self.distance

    def routeFitness(self):

        if self.fitness == 0:

            self.fitness = (
                1 /
                float(self.routeDistance())
            )

        return self.fitness


def createRoute(cityList):

    return random.sample(
        cityList,
        len(cityList)
    )


def initialPopulation(popSize, cityList):

    return [
        createRoute(cityList)
        for _ in range(popSize)
    ]


def rankRoutes(population):

    fitnessResults = {
        i: Fitness(route).routeFitness()
        for i, route in enumerate(population)
    }

    return sorted(
        fitnessResults.items(),
        key=operator.itemgetter(1),
        reverse=True
    )


def selection(popRanked, eliteSize):

    selectionResults = []

    df = pd.DataFrame(
        np.array(popRanked),
        columns=["Index", "Fitness"]
    )

    df['cum_sum'] = df.Fitness.cumsum()

    df['cum_perc'] = (
        100 *
        df.cum_sum /
        df.Fitness.sum()
    )

    for i in range(eliteSize):

        selectionResults.append(
            popRanked[i][0]
        )

    for _ in range(
        len(popRanked) - eliteSize
    ):

        pick = 100 * random.random()

        for i in range(
            len(popRanked)
        ):

            if pick <= df.iat[i, 3]:

                selectionResults.append(
                    popRanked[i][0]
                )

                break

    return selectionResults


def matingPool(
    population,
    selectionResults
):

    return [
        population[i]
        for i in selectionResults
    ]


def breed(parent1, parent2):

    childP1 = []
    childP2 = []

    geneA = int(
        random.random() *
        len(parent1)
    )

    geneB = int(
        random.random() *
        len(parent1)
    )

    startGene = min(
        geneA,
        geneB
    )

    endGene = max(
        geneA,
        geneB
    )

    childP1 = parent1[
        startGene:endGene
    ]

    childP2 = [
        item
        for item in parent2
        if item not in childP1
    ]

    return childP1 + childP2


def breedPopulation(
    matingpool,
    eliteSize
):

    children = matingpool[:eliteSize]

    length = (
        len(matingpool) -
        eliteSize
    )

    pool = random.sample(
        matingpool,
        len(matingpool)
    )

    for _ in range(length):

        child = breed(
            pool[_],
            pool[
                len(matingpool) - _ - 1
            ]
        )

        children.append(child)

    return children


def mutate(
    individual,
    mutationRate
):

    for swapped in range(
        len(individual)
    ):

        if random.random() < mutationRate:

            swapWith = int(
                random.random() *
                len(individual)
            )

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1

    return individual


def mutatePopulation(
    population,
    mutationRate
):

    return [
        mutate(ind, mutationRate)
        for ind in population
    ]


def nextGeneration(
    currentGen,
    eliteSize,
    mutationRate
):

    popRanked = rankRoutes(
        currentGen
    )

    selectionResults = selection(
        popRanked,
        eliteSize
    )

    matingpool = matingPool(
        currentGen,
        selectionResults
    )

    children = breedPopulation(
        matingpool,
        eliteSize
    )

    return mutatePopulation(
        children,
        mutationRate
    )


def geneticAlgorithm(
    population,
    popSize,
    eliteSize,
    mutationRate,
    generations
):

    pop = initialPopulation(
        popSize,
        population
    )

    print(
        "Initial distance: " +
        str(
            1 /
            rankRoutes(pop)[0][1]
        )
    )

    for _ in range(generations):

        pop = nextGeneration(
            pop,
            eliteSize,
            mutationRate
        )

    print(
        "Final distance: " +
        str(
            1 /
            rankRoutes(pop)[0][1]
        )
    )

    bestRouteIndex = rankRoutes(
        pop
    )[0][0]

    return pop[bestRouteIndex]


def geneticAlgorithmPlot(
    population,
    popSize,
    eliteSize,
    mutationRate,
    generations
):

    pop = initialPopulation(
        popSize,
        population
    )

    progress = [
        1 /
        rankRoutes(pop)[0][1]
    ]

    for _ in range(generations):

        pop = nextGeneration(
            pop,
            eliteSize,
            mutationRate
        )

        progress.append(
            1 /
            rankRoutes(pop)[0][1]
        )

    plt.plot(progress)

    plt.ylabel('Distance')
    plt.xlabel('Generation')

    plt.show()


def main():

    cityList = [

        City(
            int(random.random() * 200),
            int(random.random() * 200)
        )

        for _ in range(25)
    ]

    geneticAlgorithmPlot(
        population=cityList,
        popSize=100,
        eliteSize=20,
        mutationRate=0.01,
        generations=500
    )


if __name__ == '__main__':
    main()
    
    
    
#here the GSA is used to find the best route for the traveling salesman problem using a genetic algorithm. The code defines classes for City and Fitness, and functions for creating routes, populations, ranking routes, selection, mating, breeding, mutation, and running the genetic algorithm. The main function generates a list of random cities and runs the genetic algorithm to find the best route, plotting the progress of the distance over generations.