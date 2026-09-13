class State:
    def __init__(self,game):
        self.game = game

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass


class StateMachine:
    def __init__(self):
        self.states = {}
        self.current = None

    def register(self, name, state):
        self.states[name] = state

    def change(self, name):
        if self.current:
            self.current.exit()
        self.current = self.states[name]
        self.current.enter()

    def handle_events(self, events):
        if self.current:
            self.current.handle_events(events)

    def update(self, dt):
        if self.current:
            self.current.update(dt)

    def render(self, screen):
        if self.current:
            self.current.render(screen)
