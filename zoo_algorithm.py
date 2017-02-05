#!/usr/bin/env python

import math
import sys

def main():
    animal_file = open(sys.argv[1], 'rb')
    num_animals = int(sys.argv[2])
    
    zoo_length = int(math.ceil(math.sqrt(num_animals)))
    zoo_array = []
    
    for i in range(zoo_length):
        zoo_array.append([''] * zoo_length)
    
    for line in animal_file:
        split_line = line.strip().split(',')
        animal = split_line[0]
        enemies = []
        
        if len(split_line) > 0:
            enemies = split_line[1:]
        
        placed = False
        print enemies
        
        for i in range(zoo_length):
            if placed:
                break
            
            for j in range(zoo_length):
                suitable = True
                
                if zoo_array[i][j] == '':
                    neighbours = [zoo_array[i - 1][j], zoo_array[(i + 1) % zoo_length][j], zoo_array[i][j - 1], zoo_array[i][(j + 1) % zoo_length]]
                    
                    for enemy in enemies:
                        if enemy in neighbours:
                            suitable = False
                    
                    if suitable:
                        zoo_array[i][j] = animal
                        placed = True
                        break
    
    print(zoo_array)

if __name__ == '__main__':
    main()
    