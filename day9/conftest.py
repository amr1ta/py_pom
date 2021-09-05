import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--option", action="store", default="non_headless")
    parser.addoption("--url", action="store", default="https://en.wikipedia.org/wiki/Main_Page")


