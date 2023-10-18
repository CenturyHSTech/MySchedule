"""
Test for HTML requirements
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_elements = [("doctype", 1),
                     ("html", 1),
                     ("head", 1),
                     ("title", 1),
                     ("h1", 1),
                     ("h2", 3),
                     ("p", 4),
                     ("a", 2)
                     ]
required_format_elements = [("strong or b", 2),
                            ("em or i", 2)
                            ]


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


def test_for_presence_of_html_files(files):
    assert len(files) > 0


@pytest.mark.parametrize("element,num", required_elements)
def test_files_for_required_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        actual = html.get_num_elements_in_file(element, file)
        assert actual >= num


@pytest.mark.parametrize("element,num", required_format_elements)
def test_files_for_required_format_elements(element, num, files):
    if not files:
        assert False
    for file in files:
        num_bold = html.get_num_elements_in_file("strong", file)
        num_bold += html.get_num_elements_in_file("b", file)
        num_italics = html.get_num_elements_in_file("em", file)
        num_italics += html.get_num_elements_in_file("i", file)

        if element == "strong or b":
            assert num_bold >= num
        elif element == "em or i":
            expected = num
            assert num_italics >= expected
