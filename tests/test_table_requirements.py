"""
Test for a bullet or number list with at least 3 list items.
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_list_elements = [("ul or ol", 1),
                          ("li", 3)]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.mark.parametrize("element,num", required_list_elements)
def test_files_for_required_list_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        num_lists = html.get_num_elements_in_file("ul", file)
        num_lists += html.get_num_elements_in_file("ol", file)
        if element == "ul or ol":
            assert num_lists >= num
        elif element == "li":
            actual = html.get_num_elements_in_file(element, file)
            expected = num * num_lists
            assert actual >= expected
