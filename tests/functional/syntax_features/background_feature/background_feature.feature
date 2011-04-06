Feature: Validate that background works

    Background:
        Given that world count is 5

    Scenario: Counting the world is
        When I add one to the world
        Then world count should be 6

    Scenario: Renting a featured movie
        Then world count should be 5