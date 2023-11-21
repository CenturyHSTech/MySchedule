"""
Test CSS Requirements.
"""
import pytest
import file_clerk.clerk as clerk
from webcode_tk import css_tools as css
from webcode_tk import color_tools
from webcode_tk import html_tools as html

project_path = "project/"
html_files = html.get_all_html_files(project_path)
styles_by_html_files = css.get_styles_by_html_files(project_path)
global_color_rules = []
for file in html_files:
    global_color_rules.append(css.get_global_colors(file))
global_color_contrast_tests = []
no_style_attribute_tests = []


def get_all_color_rule_results():
    color_rule_results = css.get_project_color_contrast(project_path)
    return color_rule_results


def set_style_attribute_tests(path):
    results = []
    for file in html_files:
        data = html.get_style_attribute_data(file)
        if data:
            for datum in data:
                results.append(datum)
    return results


def get_unique_font_families(project_folder):
    font_rules = css.get_unique_font_rules(project_folder)
    font_families_tests = []
    for file in font_rules:
        # apply the file, unique rules, unique selectors, and unique values
        filename = file.get("file")
        unique_rules = file.get("rules")
        passes_rules = len(unique_rules) >= 2
        passes_selectors = passes_rules
        unique_values = []
        for rule in unique_rules:
            value = rule.get("family")
            if value not in unique_values:
                unique_values.append(value)
        passes_values = len(unique_values) == 2
        font_families_tests.append((filename, passes_rules, passes_selectors,
                                    passes_values))
    return font_families_tests


def get_font_rules_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append(test[:2])
    return rules_data


def get_font_selector_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0], test[2]))
    return rules_data


def get_font_family_data(font_tests):
    rules_data = []
    for test in font_tests:
        rules_data.append((test[0], test[3]))
    return rules_data


def get_table_colors_applied():
    filename = all_color_data[0][0]
    table_colors = []
    colors_applied = False
    for row in all_color_data:
        current_file = row[0]
        if current_file != filename:
            table_colors.append((filename, colors_applied))
            filename = current_file
            colors_applied = False
        selector = row[1]
        if "table" not in selector:
            continue
        color = row[3]
        bg_color = row[4]
        if color and bg_color:
            colors_applied = True
            table_colors.append((current_file, colors_applied))


def prep_global_color_tests(global_color_contrast_tests,
                            global_color_rules):
    for rule in global_color_rules:
        path = list(rule.keys())[0]
        file = path.split("/")[-1]
        data = rule[path]
        ratio = data.get("contrast_ratio")
        passes = data.get("passes_normal_aaa")
        global_color_contrast_tests.append(
            (file, ratio, passes)
        )


prep_global_color_tests(global_color_contrast_tests,
                        global_color_rules)
font_families_tests = get_unique_font_families(project_path)
font_rules_results = get_font_rules_data(font_families_tests)
font_selector_results = get_font_selector_data(font_families_tests)
font_family_results = get_font_family_data(font_families_tests)
all_color_rules_results = get_all_color_rule_results()
style_attributes_data = set_style_attribute_tests(project_path)
link_colors = css.get_link_color_data(project_path)


@pytest.fixture
def project_folder():
    return project_path


@pytest.fixture
def all_color_data():
    return all_color_rules_results


@pytest.fixture
def link_color_details():
    return link_colors


@pytest.mark.parametrize("file,tag,value", style_attributes_data)
def test_files_for_style_attribute_data(file, tag, value):
    results = f"Tag: <{tag}> from '{file}' has a style attribute"
    assert not results


def test_files_for_has_style_attributes(project_folder):
    results = "No style attributes found"
    expected = results
    html_files = html.get_all_html_files(project_folder)
    for file in html_files:
        has_style_attribute = html.has_style_attribute_data(file)
        if has_style_attribute:
            filename = clerk.get_file_name(file)
            results = f"{filename} has style attributes"
    assert expected == results


@pytest.mark.parametrize("file,rule,goal,expected",
                         global_color_contrast_tests)
def test_files_for_global_color_contrast(file, rule, goal, expected):
    # NOTE: make sure the rule is not a list (happens if there's only 1 file)
    if isinstance(rule, list) and len(rule) == 1:
        rule = rule[0]
    bg_color = rule.get("background-color")
    bg_color = color_tools.get_hex(bg_color)
    color = rule.get("color")
    color = color_tools.get_hex(color)
    result = color_tools.passes_color_contrast(goal, bg_color, color)
    assert result == expected


@pytest.mark.parametrize("file,passes_rules", font_selector_results)
def test_files_for_enough_font_rules(file, passes_rules):
    assert passes_rules


@pytest.mark.parametrize("file,passes_selector", font_selector_results)
def test_files_for_for_enough_font_selectors(file, passes_selector):
    assert passes_selector


@pytest.mark.parametrize("file,passes_font_families", font_selector_results)
def test_files_for_2_font_families_max(file, passes_font_families):
    assert passes_font_families


def test_files_for_table_colors(project_folder):
    css.file_applies_property_by_selector()
    assert False


def test_link_color_details_for_links_targeted(link_color_details):
    assert link_color_details


@pytest.mark.parametrize("file,sel,goal,col,bg,ratio,passes",
                         link_colors)
def test_link_color_details_for_passing_color_contrast(file, sel, goal,
                                                       col, bg, ratio,
                                                       passes):
    filename = file.split("/")[-1]
    if passes:
        results = f"Color contrast for {sel} in {filename} passes at {ratio}"
        expected = results
        assert results == expected
    else:
        results = f"Color contrast for {sel} in {filename} fails at {ratio}"
        expected = f"Color contrast for {sel} in {filename} passes."
        assert results == expected
