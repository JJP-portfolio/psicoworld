class Entity:

    def __init__(self):
        self.components = {}

    def add_component(self, component):
        self.components[type(component).__name__] = component

    def get_component(self, component_type):
        return self.components.get(component_type.__name__)

    def has_component(self, component_type):
        return component_type.__name__ in self.components
    
