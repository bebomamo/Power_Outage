import pygame, unittest, game
from objects import *

class TestGame(unittest.TestCase):
    # Creates a new instance of States with all default values
    def setUp(self):
        self.states = States()

    # Test method that ensures the game's window functions as intended
    def test_window(self):
        # Window initialization
        self.assertEqual(self.states.jiggle_countdown, self.states.jiggle_time)
        self.assertEqual(self.states.window_phase, 1)

        # Test update_states
        self.states.jiggle_countdown = 1 # countdown hasn't finished
        game.update_states(self.states)
        self.assertNotEqual(self.states.jiggle_countdown, self.states.jiggle_time)
        self.assertEqual(self.states.window_phase, 1)

        self.states.jiggle_countdown = -1 # countdown has finished
        game.update_states(self.states)
        self.assertEqual(self.states.jiggle_countdown, self.states.jiggle_time)
        self.assertEqual(self.states.window_phase, 2)

        # TODO - add tests that check click functionality

    # Test method that ensures the game's door functions as intended
    def test_door(self):
        # Door initialization
        self.assertEqual(self.states.lock_countdown, self.states.lock_time)
        self.assertEqual(self.states.door_phase, 1)

        # Test update_states
        self.states.lock_countdown = 1 # countdown hasn't finished
        game.update_states(self.states)
        self.assertNotEqual(self.states.lock_countdown, self.states.lock_time)
        self.assertEqual(self.states.door_phase, 1)

        self.states.lock_countdown = -1 # countdown has finished
        game.update_states(self.states)
        self.assertEqual(self.states.lock_countdown, self.states.lock_time)
        self.assertEqual(self.states.door_phase, 2)
        
        # TODO - add tests that check click functionality

if __name__ == '__main__':
    unittest.main()