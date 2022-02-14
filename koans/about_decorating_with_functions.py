#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *


class AboutDecoratingWithFunctions(Koan):
    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(), "o/~ We all live in a broken submarine o/~")
        self.assertEqual('COWBELL BABY!', self.mediocre_song.wow_factor)

        #i understand that fn.wow_factor will overwrite the fn with a new value.

    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        self.assertEqual('<llama/>', self.render_tag('llama'))

        #Im interested in what the use case for this is
