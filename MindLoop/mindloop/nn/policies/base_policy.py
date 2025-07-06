class Policy:
    """Base class for robot control policies."""
    def forward(self, observation):
        raise NotImplementedError

    def act(self, observation):
        return self.forward(observation) 