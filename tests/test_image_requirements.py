"""
Test for a bullet or number list with at least 3 list items.
"""
from file_clerk import clerk
import pytest
from webcode_tk import html_tools as html

required_image_elements = 3
required_images = 3


@pytest.fixture
def files():
    files = clerk.get_all_files_of_type("project/", "html")
    return files


@pytest.fixture
def number_figures():
    number_figures = html.get_num_elements_in_folder("figure", "project/")
    return number_figures


@pytest.fixture
def total_images():
    total_images = 0
    for type in ("jpg", "png", "gif", "webp", "svg"):
        images = clerk.get_all_files_of_type("project/", type)
        total_images += len(images)
    return total_images


def test_files_for_required_figure_elements(number_figures):
    assert number_figures >= required_image_elements


def test_files_for_figcaptions(number_figures):
    number_figcaptions = html.get_num_elements_in_folder("figcaption", "project/")
    expected = number_figures
    assert number_figcaptions == expected


def test_files_for_number_img_tags(number_figures):
    number_img_tags = html.get_num_elements_in_folder("img", "project/")
    expected = number_figures
    assert number_img_tags >= expected


def test_for_number_of_image_files(total_images):
    assert total_images >= 2
