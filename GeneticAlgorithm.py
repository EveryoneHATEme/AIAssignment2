import numpy as np
import random

import Notes
import Scales
from Track import Track
from Chords import Chord


class GeneticAlgorithm:
    rewards = [
        300,    # perfect unison
        -300,   # minor second
        -100,   # major second
        0,      # minor third
        100,    # major third
        200,    # perfect fourth
        -200,   # augmented fourth / diminished fifth
        200,    # perfect fifth
        100,    # minor sixth
        0,      # major sixth
        -100,   # minor seventh
        -300    # major seventh
    ]

    def __init__(self, track: Track, population_size: int = 100, offsprings_number: int = 30, generations: int = 500):
        self.track = track
        self.population_size = population_size
        self.offsprings_number = offsprings_number
        self.generations = generations

    def get_individual(self):
        chosen_scale: Scales.Scale = random.choice(self.track.most_probable_scales)
        degrees = random.choices(range(len(chosen_scale.scheme)), k=self.track.get_beats_count())
        chords = [chosen_scale.get_chord_from(degree) for degree in degrees]
        return chords

    def get_initial_population(self):
        return sorted((self.get_individual() for _ in range(self.population_size)), key=self.fitness)

    def get_parents(self, population):
        mothers = population[-2 * self.offsprings_number::2]
        fathers = population[-2 * self.offsprings_number + 1::2]

        return mothers, fathers

    def cross(self, mother, father):
        mother_head = mother[:len(mother) // 2].copy()
        mother_tail = mother[len(mother) // 2:].copy()
        father_tail = father[len(father) // 2:].copy()

        mapping = {father_tail[i]: mother_tail[i] for i in range(len(mother_tail))}

        for i in range(len(mother_head)):
            while mother_head[i] in father_tail:
                mother_head[i] = mapping[mother_head[i]]

        return [*mother_head, *father_tail]

    def mutate(self, offspring):
        i, j = random.sample(range(len(offspring)), 2)
        offspring[i], offspring[j] = offspring[j], offspring[i]
        return offspring

    def replace_population(self, population, new_individuals):
        new_population = sorted([*population, *new_individuals], key=self.fitness)
        return new_population[-len(population):]

    def evolution_step(self, population):
        mothers, fathers = self.get_parents(population)
        offsprings = []

        for mother, father in zip(mothers, fathers):
            offspring = self.mutate(self.cross(mother, father))
            offsprings.append(offspring)

        new_population = self.replace_population(population, offsprings)
        return new_population

    def evolution(self):
        population = self.get_initial_population()

        for generation in range(self.generations):
            population = self.evolution_step(population)

        return population[-1]

    @classmethod
    def beat_fitness(cls, chord: Chord, beat: list[Notes.Note]):
        fitness = 0

        for beat_note in beat:
            for chord_note in chord:
                interval = Notes.Note.get_interval(beat_note.__class__, chord_note)
                fitness += cls.rewards[interval]

        return fitness

    def fitness(self, chords: list[Chord]):
        if len(chords) != len(self.track.get_beats()):
            raise WrongChordsFormat

        total_fitness = sum(
            (self.beat_fitness(chord, beat) for chord, beat in zip(chords, self.track.get_beats()))
        )

        return total_fitness


class WrongChordsFormat(Exception):
    pass
