from komitas.components import *
from komitas.html.tags import *
from komitas.html.attributes import *

class IntroducitonPage(Component):
    def __call__(self):
        return Div().attrs(
            (Class, "container mt-4")
        ).innrs(
            H1("Welcome to Komitas"),
            P(
                "Komitas is a modern web framework designed to simplify the "
                "process of building interactive web applications using "
                "component-based architecture."
            ),
            H2("Getting Started"),
            P(
                "To get started with Komitas, check out the documentation "
                "and explore the various components and features available."
            ),
        )
    
class MotivationPage(Component):
    def __call__(self):
        return Div().attrs(
            (Class, "container mt-4")
        ).innrs(
            H1("Motivation"),
            P(
                "The motivation behind Komitas is to provide developers with "
                "a powerful yet easy-to-use framework that leverages Python's "
                "capabilities for web development."
            ),
            P(
                "By focusing on components, Komitas allows for reusable and "
                "maintainable code, making it easier to build complex UIs."
            ),
        )
