from lettuce import step, world
from nose.tools import assert_equals


@step("Given that world count is 5")
def set(step):
    world.count = 5
    assert_equals(world.count, 5)

@step("Then world count should be 6")
def check(step):
    assert_equals(world.count, 6)

@step("Then world count should be 5")
def check(step):
    assert_equals(world.count,5)

@step("When I add one to the world")
def check(step):
    world.count += 1

