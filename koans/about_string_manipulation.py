#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string)

        # .format can be used to make dynamic strings

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        # self.assertEqual(__, string)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string)

        # values used in .format can be used in any order or repeated

    def test_any_python_expression_may_be_interpolated(self):
        import math  # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
                                                            decimal_places)
        # self.assertEqual(__, string)
        self.assertEqual("The square root of 5 is 2.2361", string)

        # Expressions may be interpolated in strings

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # self.assertEqual(__, string[7:10])

        self.assertEqual("let", string[7:10])

        # string[7:10] is not inclusive, creates a substring

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        # self.assertEqual(__, string[1])

        self.assertEqual('a', string[1])

        # You can target single characters from strings

    def test_single_characters_can_be_represented_by_integers(self):
        # self.assertEqual(__, ord('a'))
        # self.assertEqual(__, ord('b') == (ord('a') + 1))
        self.assertEqual(97, ord('a'))
        self.assertEqual(True, ord('b') == (ord('a') + 1))

        # ord(char) returns the char in unicode

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        # self.assertListEqual([__, __, __], words)

        self.assertListEqual(["Sausage", "Egg", "Cheese"], words)

        # .split() seperates a string into a list by words (or letters if one word)

    def test_strings_can_be_split_with_different_patterns(self):
        import re  # import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;')

        words = pattern.split(string)

        # self.assertListEqual([__, __, __, __], words)

        self.assertListEqual(["the", "rain", "in", "spain"], words)

        # Strings can be split with different patterns

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n'
        self.assertNotEqual('\n', string)
        # self.assertEqual(__, string)
        # self.assertEqual(__, len(string))

        self.assertEqual("\\n", string)
        self.assertEqual(2, len(string))

        # raw strings do not include the n in \\n as it is an escape char

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        # self.assertEqual(__, ' '.join(words))

        self.assertEqual("Now is the time", ' '.join(words))

        # Join creates a string from a list

    def test_strings_can_change_case(self):
        # self.assertEqual(__, 'guido'.capitalize())
        # self.assertEqual(__, 'guido'.upper())
        # self.assertEqual(__, 'TimBot'.lower())
        # self.assertEqual(__, 'guido van rossum'.title())
        # self.assertEqual(__, 'ToTaLlY aWeSoMe'.swapcase())

        self.assertEqual('Guido', 'guido'.capitalize())
        self.assertEqual('GUIDO', 'guido'.upper())
        self.assertEqual('timbot', 'TimBot'.lower())
        self.assertEqual('Guido Van Rossum', 'guido van rossum'.title())
        self.assertEqual('tOtAlLy AwEsOmE', 'ToTaLlY aWeSoMe'.swapcase())

        # These string methods change the case of strings in different ways
