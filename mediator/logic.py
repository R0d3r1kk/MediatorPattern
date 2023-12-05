from abc import ABCMeta, abstractmethod


class IRequestComponentHandler(metaclass=ABCMeta):

    """An interface that each component will implement"""
    @staticmethod
    @abstractmethod
    def handle(request):
        print(f'<<< In Request <<< : {request}')


class Component:

    def __init__(self, model, handler):
        self.model = model
        self.handler = handler


class Mediator:
    """A Subject whose notify method is mediated"""

    def __init__(self):
        self._components = set()
        self.response = None

    def add(self, component, component_handler:IRequestComponentHandler):
        """Add components"""
        new_component = Component(component, component_handler)
        self._components.add(new_component)

    def send(self, request):
        """Add components except for the originator component"""
        for component in self._components:
            if type(component.model) is type(request):
                component.model = request
                self.response = component.handler.handle(request)
