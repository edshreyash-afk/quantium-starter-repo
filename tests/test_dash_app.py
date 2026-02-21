import pytest
from main import app
from dash import html, dcc


def test_header_present():
    """Checks if an H1 header exists within the layout."""
    layout = app.layout

    def find_h1(children):
        if isinstance(children, html.H1):
            return True
        if hasattr(children, 'children') and children.children:
            if isinstance(children.children, list):
                return any(find_h1(child) for child in children.children)
            else:
                return find_h1(children.children)
        return False

    assert find_h1(layout)


def test_visualisation_present():
    """Checks if a dcc.Graph component exists."""
    layout = app.layout

    def find_graph(children):
        if isinstance(children, dcc.Graph):
            return True
        if hasattr(children, 'children') and children.children:
            if isinstance(children.children, list):
                return any(find_graph(child) for child in children.children)
            else:
                return find_graph(children.children)
        return False

    assert find_graph(layout)


def test_region_picker_present():
    """Checks if the RadioItems region picker exists."""
    layout = app.layout

    def find_radio(children):
        if isinstance(children, dcc.RadioItems):
            return True
        if hasattr(children, 'children') and children.children:
            if isinstance(children.children, list):
                return any(find_radio(child) for child in children.children)
            else:
                return find_radio(children.children)
        return False

    assert find_radio(layout)