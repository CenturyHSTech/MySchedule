"""
Test for a bullet or number list with at least 3 list items.
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_table_elements = [("h2 or caption", 2),
                           ("table", 2),
                           ("tr", 12),
                           ("th", 8),
                           ("td", 32)]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.mark.parametrize("element,num", required_table_elements)
def test_files_for_required_table_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        num_table_labels = html.get_num_elements_in_file("h2", file)
        num_table_labels += html.get_num_elements_in_file("caption", file)
        if element == "h2 or caption":
            assert num_table_labels >= num
        else:
            actual = html.get_num_elements_in_file(element, file)
            expected = num
            assert actual >= expected
