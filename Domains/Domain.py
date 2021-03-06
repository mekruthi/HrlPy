""" Domain Abstract Class """
import logging
import numpy as np


class Domain(object):
    #: The discount factor by which rewards are reduced
    discount_factor = .9
    #: The number of possible states in the domain
    states_num = 0  # was None
    #: The number of Actions the agent can perform
    actions_num = 0  # was None
    #: Limits of each dimension of the state space. Each row corresponds to one dimension and has two elements
    # [min, max]
    statespace_limits = None  # was None
    #: Number of dimensions of the state space
    state_space_dims = 0  # was None
    # a list of dimension that is continous
    continuous_dims = []
    #: The cap used to bound each episode (return to state 0 after)
    episodeCap = None
    #: A simple object that records the prints in a file
    logger = None
    # A seeded numpy random number generator
    random_state = None

    def __init__(self):
        self.logger = logging.getLogger("hrl.Domains." + self.__class__.__name__)
        self.state_space_dims = len(self.statespace_limits)
        # To make sure type of discount_factor is float. This will later on be used in
        self.discount_factor = float(self.discount_factor)
        # a new stream of random numbers for each domain
        self.random_state = np.random.RandomState()
        if self.continuous_dims:
            self.states_num = int(np.prod(self.statespace_limits[:, 1] - self.statespace_limits[:, 0]))
        else:
            self.states_num = np.inf

    def is_terminal(self, s):
        raise NotImplementedError("Implement initial state method")

    def possible_actions(self, s=None):
        return np.arange(self.actions_num)

    def s0(self):
        raise NotImplementedError("Implement initial state method")

    def step(self, s, a):
        """
        :param s: the state vector
        :param a: the action index
        :return: The tuple (r, ns, t, p_actions) =
            (Reward [value], next observed state, isTerminal [boolean])
        """
        raise NotImplementedError("Any domain needs to implement step function")

