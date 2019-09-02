from behave import given, when, then
from hamcrest import assert_that, equal_to

from pages.locators import *
from pages.home_page import HomePage
from pages.search_page import SearchPage


@given("User is on wikipedia Homepage")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.open(context.homepage_url)


@when('User searches "{word}"')
def step_impl(context, word):
    """
    :type context: behave.runner.Context
    """
    homepage = HomePage(context.driver)
    homepage.set_search_query(word)
    homepage.search()


@then('Title of the page should be "{word}"')
def step_impl(context, word):
    """
    :type context: behave.runner.Context
    """
    search_page = SearchPage(context.driver)
    assert_that(search_page.heading_text(), equal_to(word))
