
import numpy as np

class SimpleRLAgent:
    def __init__(self, actions):
        self.actions = actions

    def choose_action(self, state):
        """
        Chooses an action based on the state (random policy).
        """
        return np.random.choice(self.actions)

if __name__ == "__main__":
    agent = SimpleRLAgent(actions=['explore', 'exploit'])
    state = [0.5, 0.1, 0.3]  # Example state
    action = agent.choose_action(state)
    print(f"Chosen action: {action}")
