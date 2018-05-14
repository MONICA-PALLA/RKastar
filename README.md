# RKastar
Implementation of TSP and Astar using Ant Colony Algorithms and Particle Swarm Optimization and comparing the performance of 
algorithms.

Files included:

output.py - script for running antal.cpp and displaying the output by execution of "readfiles.py".

antal.cpp - TSP using ACO, reads "TSP.txt" and generates "city_data.txt" and "Data.txt".

readfiles.py - contains scripts for plotting the output for the TSP (requires matplotlib)

TSP.txt - specified co-ordinates of the cities (can be modified)

RK.py - script for TSP using PSO

RK_merged.py - combined both the output.py contents and RK.py output (includes both ACO and PSO for TSP)

*******************************************
phero.txt - heuristics as pheromone trails from antal.cpp for Astar (Astar using ACO)
