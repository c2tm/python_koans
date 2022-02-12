#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutAsserts(Koan):

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        # self.assertTrue(False) # This should be True
        self.assertTrue(True)  # Tests if value is true

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        # self.assertTrue(False, "This should be True -- Please fix this")
        # Tests if vsalue is true and displays a message if the test is failed
        self.assertTrue(True, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        # self.assertEqual(__, 1 + 1)
        # Tests if the first and second values are equal
        self.assertEqual(2, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        # expected_value = __
        # actual_value = 1 + 1
        # self.assertTrue(expected_value == actual_value)

        expected_value = 2
        actual_value = 1 + 1
        # Test will only pass if expected_value and actual_value are equal
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        # expected_value = __
        # actual_value = 1 + 1

        # self.assertEqual(expected_value, actual_value)

        expected_value = 2
        actual_value = 1 + 1

        # this test compares the two values to see if they are equal rather than true
        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        # assert False
        assert True  # Assert tests if the value is true

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(str, "navel".__class__)  # It's str, not <type 'str'>

        # .__class__ gives the class type of the object its used on, it displays it in the console by displaying <type 'str'>. The class in in quotes

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
