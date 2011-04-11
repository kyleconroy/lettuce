# -*- coding: utf-8 -*-
# <Lettuce - Behaviour Driven Development for python>
# Copyright (C) <2010-2011>  Gabriel Falcão <gabriel@nacaolivre.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os
import lettuce
import sys
from nose.tools import assert_equals, assert_true, with_setup
from lettuce import Runner
from tests.asserts import prepare_stdout
from tests.asserts import assert_stdout_lines

def feature_name(name):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)),
                        'syntax_features', name, "%s.feature" % name)

@with_setup(prepare_stdout)
def test_background_runs_before_each_scenario():
    'Test Background runs before each scenario'
    runner = Runner(feature_name('background_feature'))
    results = runner.run()
    assert_equals(results.steps_passed, 5)

OUTPUT1 = """
Feature: Validate that background works # tests/functional/syntax_features/background_feature/background_feature.feature:1
  Background:                           # tests/functional/syntax_features/background_feature/background_feature.feature:3

  Scenario: Counting the world is       # tests/functional/syntax_features/background_feature/background_feature.feature:6
    When I add one to the world         # tests/functional/syntax_features/background_feature/steps.py:19
    Then world count should be 6        # tests/functional/syntax_features/background_feature/steps.py:11

  Scenario: Renting a featured movie    # tests/functional/syntax_features/background_feature/background_feature.feature:10
    Then world count should be 5        # tests/functional/syntax_features/background_feature/steps.py:15

1 feature (1 passed)
4 scenarios (4 passed)
5 steps (5 passed)
"""

@with_setup(prepare_stdout)
def test_background_colorless_output():
    'Test Background color output'
    runner = Runner(feature_name('background_feature'), verbosity=3)
    runner.run()
    assert_equals(sys.stdout.getvalue(), OUTPUT1)
#    assert_stdout_lines(OUTPUT1)
