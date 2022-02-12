#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutHashes in the Ruby Koans
#

from runner.koan import *


class AboutDictionaries(Koan):
    def test_creating_dictionaries(self):
        empty_dict = dict()
        self.assertEqual(dict, type(empty_dict))
        self.assertDictEqual({}, empty_dict)
        # self.assertEqual(__, len(empty_dict))

        self.assertEqual(0, len(empty_dict))

        # dictionaries have length, you can make empty dictionaries

    def test_dictionary_literals(self):
        empty_dict = {}
        self.assertEqual(dict, type(empty_dict))
        babel_fish = {'one': 'uno', 'two': 'dos'}
        # self.assertEqual(__, len(babel_fish))

        self.assertEqual(2, len(babel_fish))

        # the length of dictionaries is based on amount of key value pairs

    def test_accessing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        self.assertEqual('uno', babel_fish['one'])
        self.assertEqual('dos', babel_fish['two'])

        # dict['key'] = value

    def test_changing_dictionaries(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        babel_fish['one'] = 'eins'

        expected = {'two': 'dos', 'one': 'eins'}
        self.assertDictEqual(expected, babel_fish)

        # Dictionaries can be changed with dict['key'] = new value

    def test_dictionary_is_unordered(self):
        dict1 = {'one': 'uno', 'two': 'dos'}
        dict2 = {'two': 'dos', 'one': 'uno'}

        self.assertEqual(dict2 == dict1, dict1 == dict2)

        # Dictionaries are unordered

    def test_dictionary_keys_and_values(self):
        babel_fish = {'one': 'uno', 'two': 'dos'}
        # self.assertEqual(__, len(babel_fish.keys()))
        # self.assertEqual(__, len(babel_fish.values()))
        # self.assertEqual(__, 'one' in babel_fish.keys())
        # self.assertEqual(__, 'two' in babel_fish.values())
        # self.assertEqual(__, 'uno' in babel_fish.keys())
        # self.assertEqual(__, 'dos' in babel_fish.values())

        self.assertEqual(2, len(babel_fish.keys()))
        self.assertEqual(2, len(babel_fish.values()))
        self.assertEqual(True, 'one' in babel_fish.keys())
        self.assertEqual(False, 'two' in babel_fish.values())
        self.assertEqual(False, 'uno' in babel_fish.keys())
        self.assertEqual(True, 'dos' in babel_fish.values())

        # value in dict.keys() and value in dict.value() can test if a
        # value or key is in the dictionary

    def test_making_a_dictionary_from_a_sequence_of_keys(self):
        cards = {}.fromkeys(('red warrior', 'green elf', 'blue valkyrie',
                            'yellow dwarf', 'confused looking zebra'), 42)

        self.assertEqual(5, len(cards))
        self.assertEqual(42, cards['green elf'])
        self.assertEqual(42, cards['yellow dwarf'])

        # {}.fromkeys((keys), (values)) makes a dictionary from a user
        # supplied keys and values
