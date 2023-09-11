#MIT License

#Copyright (c) 2023 Vidal Klaas Gregorius Spierings

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Toelichting: het plaatsen van het blok met de naam 'Air' dient effectievelijk als een verwijder commando voor een blok op de aangegeven coordinaten.

from time import sleep
from random import randint

# importeer alleen de functies vanuit bijbehorende classes die nodig zijn voor dit project

world.fill(from_me(0, 0, 0), from_me(11, 180, 10), "Cyan Stained Glass", "hollow")

# buitenste frame bouwen

world.fill(from_me(1, 0, 0), from_me(1, 1, 0), "Air", "hollow")

# verwijder benedenste glas rand op de xz as

world.fill(from_me(1, 0, 1), from_me(10, 0, 9), "Air")

# creëer ingang gebouw

world.fill(from_me(-1, -1, -3), from_me(12, -1, 11), "Quartz Bricks", "hollow")

# tegelvloer omringt door wolkenkrabber bouwen

world.fill(from_me(1, -1, 1), from_me(10, -1, 9), "White concrete")

# creëer vloer voor de begane grond

world.fill(from_me(1, 0, 9), from_me(10, 7, 9), "Block Of Iron")

# creëer ijzeren wand voor balie bij de lobby

world.fill(from_me(2, 0, 8), from_me(9, 0, 7), "Block Of Quartz")
world.fill(from_me(3, 0, 8), from_me(8, 0, 8), "Air")

stoelIndex = 0

for count in range(3):
    world.fill(from_me(3 + stoelIndex, 0, 8), from_me(3 + stoelIndex, 0, 8), "Nether Brick Fence")
    stoelIndex += 2

# creëer elke twee blokken een stoel. 

# stoelIndex begint bij 0 en incrementeert de locatie op de x-as waar een stoel geplaatst dient te worden steeds met een factor van 2

world.fill(from_me(10, 7, 9), from_me(1, 7, 1), "White Concrete")

# creëer plafond

show_title("The Shard", "32 London Bridge St,\nLondon SE1 9SG,\nVerenigd Koninkrijk", None, 10, 150, 10)

# Toon welkomstitel

random_number_of_villagers = randint(1, 3)

world.summon("Villager", from_me(4, 3, 4), random_number_of_villagers)

# spawn een willekeurig aantal 'Villager' Mobs/NPC's (tussen de 1 en 3) in de lobby

agent.teleport(from_me(3, 1, 8))

agent.turn("right")
agent.turn("right")

sleep(11)

agent.say("Goedemorgen, welkom bij The Shard, komt u om in te checken bij het Shangri-La hotel?")

# spawn agent op een stoel bij de balie en verwelkom de speler na drie seconden met een welkomstbericht
