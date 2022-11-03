#!/usr/bin/env python3
# File       : P2.py
# Description: @property decorator
# Copyright 2022 Harvard University. All Rights Reserved.

class Animal:

    # class attribute for species that exist in universe
    _species_universe = [
        'cat', 'dog', 'duck', 'elf', 'goblin', 'horse', 'human', 'mermaid',
        'nightingale', 'pig', 'swan', 'wolf'
    ]

    @staticmethod
    def _valid_species(s):
        if s not in Animal._species_universe:
            raise ValueError(f'Species `{s}` does not exist in universe')

    def __init__(self, name, species):
        self._valid_species(species)
        self.name = name
        self._species = species

    def __repr__(self):
        cls = type(self)
        return f"{cls.__name__}('{self.name}', '{self.species}')"
    
    def set_species(self,species):
        self._valid_species(species)
        self.species = species

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self,into):
        if into not in Animal._species_universe:
            raise ValueError(f'Species `{into}` does not exist in universe')
        self._species = into

    @species.deleter
    def species(self):
        del self._species
        
if __name__ == "__main__":
    animal = Animal('Snoopy','dog')
    print(animal.species)
    animal.species = 'cat'
    print(animal.species)
    del animal.species
    print(animal.species)
