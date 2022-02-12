#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        # self.assertEqual(__, isinstance(string, str))
        # isinstance tests if string is a str type, returns true or false. Text in "" are strings.
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        # tests if '' strings are strings
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        # self.assertEqual(__, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str)
                         )  # tests if """" is a string

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        # self.assertEqual(__, isinstance(string, str))
        self.assertEqual(True, isinstance(string, str)
                         )  # tests if '''''' is a string

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        # self.assertEqual(__, isinstance(string, str))
        # tests if raw strings are strings
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        # self.assertEqual(__, string)
        # tests if single quotes can be used to inlucde double quotes in a string
        self.assertEqual('He said, "Go Away."', string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        # self.assertEqual(__, string)
        # tests if doubles quotes can be used to include single quotes in the string
        self.assertEqual("Don't", string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        # self.assertEqual(__, (a == b))
        # tests if backslashes can be used to inlcude more quotes in strings
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        # self.assertEqual(__, len(string))
        # tests if \n\ will display any characters following on next line
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        # self.assertEqual(__, len(string))
        # tests if triple quote strings can span multiple lines
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        # self.assertEqual(__, (a == b))
        # tests if triple quoted strings dont need backslashes
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        # self.assertEqual(__, string)'
        # Tests if you can escape a quote at the end of a triple quoted string
        self.assertEqual('Hello "world"', string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        # self.assertEqual(__, string)
        # Tests if strings can be concatenated with this syntax
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        # self.assertEqual(__, string)
        # tests if strongs can be concatenated without +
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)  # tests if + mutates original strings

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        # self.assertEqual(__, hi)
        # tests if strings can be appended to the end of other strings using +=
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        # self.assertEqual(__, original)
        self.assertEqual("Hello, ", original)  # tests if += mutates original

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(
            1, len(string))  # len returns the length of an iterable object
