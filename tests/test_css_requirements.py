"""
Test CSS Requirements.
"""
import pytest
import re
from webcode_tk import css_tools as css
from webcode_tk import color_tools
from webcode_tk import html_tools as html
from file_clerk import clerk


style_tag_re = r'<(\w+)\s[^>]*?style=([\"|\']).*?\2\s?[^>]*?(\/?)>'
project_path = "project/"
html_files = html.get_all_html_files(project_path)
styles_by_html_files = css.get_styles_by_html_files(project_path)
global_color_rules = css.get_global_colors(project_path)
global_color_contrast_tests = []
no_style_attribute_tests = []


def get_all_color_rules():
    all_the_rules = []
    for file in styles_by_html_files:
        stylesheets = file.get("stylesheets")
        for sheet in stylesheets:
            for ruleset in sheet.rulesets:
                declaration_block = ruleset.declaration_block
                declarations = declaration_block.declarations
                for declaration in declarations:
                    property = declaration.property
                    if property == "color" or "background" in property:
                        filename = file.get("file")
                        selector = ruleset.selector
                        value = declaration.value
                        if property == "background":
                            background_color = get_background_color(
                                declaration)
                            if not background_color:
                                continue
                            else:
                                value = background_color
                        all_the_rules.append((filename, selector, property,
                                              value))
        all_the_rules = condense_the_rules(all_the_rules)
    return all_the_rules


def condense_the_rules(rules):
    condensed = []
    for rule in rules:
        file, sel, prop, val = rule
        color = {}
        background = {}
        declaration = get_bg_or_color(prop)
        if declaration.get("type") == "color":
            color = declaration
        elif declaration.get("type") == "background":
            background = declaration
        if not condensed:
            condensed.append([file, sel, color, background, val])
        else:
            for rule in condensed:
                cur_file, cur_sel, cur_col, cur_bg_col, cur_val = rule
                if file == cur_file and sel == cur_sel:
                    # add the property that is missing (if it is missing)
                    print("It's time to work.")


def get_bg_or_color(prop):
    declaration = {"type": {},
                   "declaration": {}}
    if prop == "color":
        declaration["type"] = "color"
        declaration["declaration"] = {"color": prop}
    if "background" in prop:
        declaration["type"] = "background"
        declaration["declaration"] = {"background": prop}
    return declaration


def get_background_color(declaration):
    values = declaration.value.split()
    for val in values:
        color = color_tools.is_color_value(val)
        if color:
            return val
        is_keyword = val in color_tools.color_keywords.get_all_keywords()
        if is_keyword:
            return val
    return None


all_color_rules = get_all_color_rules()


def set_global_color_contrast(global_color_rules, global_color_contrast_tests,
                              file):
    goal = "Normal AAA"
    rules = global_color_rules.get(file)
    if len(rules) == 1:
        rule = rules[0]
        bg = rule.get("background-color")
        bg = color_tools.get_hex(bg)
        color = rule.get("color")
        color = color_tools.get_hex(color)
    if not bg or not color:
        passes = False
    else:
        passes = color_tools.passes_color_contrast(goal, bg, color)
    global_color_contrast_tests.append((file, rule, goal, passes))


def set_style_attribute_tests(path):
    html_code = clerk.file_to_string(path)
    tags_with_style_attrs = re.findall(style_tag_re, html_code)
    if not tags_with_style_attrs:
        no_style_attribute_tests.append((path, "All good", True))
    for tag in tags_with_style_attrs:
        element = tag[0]
        no_style_attribute_tests.append((path, element, False))


for file in html_files:
    set_global_color_contrast(global_color_rules, global_color_contrast_tests,
                              file)
    set_style_attribute_tests(file)


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


font_families_tests = get_unique_font_families(project_path)
font_rules_results = get_font_rules_data(font_families_tests)
font_selector_results = get_font_selector_data(font_families_tests)
font_family_results = get_font_family_data(font_families_tests)


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


@pytest.mark.parametrize("file,element,passes", no_style_attribute_tests)
def test_for_no_style_attributes(file, element, passes):
    assert passes
