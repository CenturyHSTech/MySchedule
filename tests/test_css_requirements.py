"""
Test for CSS requirements
"""
from file_clerk import clerk
import pytest

style_tag_re = r'/\<(\w+)\s[^>]*?style=([\"|\']).*?\2\s?[^>]*?(\/?)>'


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.fixture
def stylesheet_files():
    files = clerk.get_all_files_of_type("project/", "css")
    return files
