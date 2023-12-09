"""
Test CSS Requirements.
"""
import pytest
import file_clerk.clerk as clerk
from webcode_tk import css_tools as css
from webcode_tk import html_tools as html

project_path = "project/"
html_files = html.get_all_html_files(project_path)
styles_by_html_files = css.get_styles_by_html_files(project_path)
global_color_rules = []
for file in html_files:
    global_color_rules.append(css.get_global_colors(file))
global_color_contrast_tests = []
no_style_attribute_tests = []


def get_all_color_rule_results(project_path):
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
        file = clerk.get_file_name(path)
        data = rule[path]
        if isinstance(data, list):
            if len(data) == 1:
                data = data[0]
        selector = data.get("selector")
        ratio = data.get("contrast_ratio")
        passes = data.get("passes_normal_aaa")
        global_color_contrast_tests.append(
            (file, selector, ratio, passes)
        )


def prep_additional_table_styles(files):
    # going to check by element (table and cells)
    additional_table_data = []
    for file in files:
        filepath = file.get("file")
        filename = clerk.get_file_name(filepath)
        stylesheets = file.get("stylesheets")
        possible_table_selectors = html.get_possible_selectors_by_tag(
            filepath, "table"
        )
        possible_th_selectors = html.get_possible_selectors_by_tag(
            filepath, "th"
        )
        possible_td_selectors = html.get_possible_selectors_by_tag(
            filepath, "td"
        )
        possible_multiple_selectors = ["table,th,td", "table,td,th",
                                       "table,th", "table,td", "th,td",
                                       "td,th"]
        for selector in possible_table_selectors:
            for th in possible_th_selectors:
                combined = selector + ", " + th
                if combined not in possible_multiple_selectors:
                    possible_multiple_selectors.append(combined)
                for td in possible_td_selectors:
                    combined = combined + ", " + td
                    if combined not in possible_multiple_selectors:
                        possible_multiple_selectors.append(combined)
            for td in possible_td_selectors:
                combined = selector + ", " + td
                if combined not in possible_multiple_selectors:
                    possible_multiple_selectors.append(combined)
                for th in possible_th_selectors:
                    combined = combined + ", " + th
                    if combined not in possible_multiple_selectors:
                        possible_multiple_selectors.append(combined)
        for sheet in stylesheets:
            td_styles = ""
            th_styles = ""
            table_border = False
            td_padding = False
            th_padding = False
            td_border = False
            th_border = False
            for rule in sheet.rulesets:
                selector = rule.selector

                # check table border
                if selector in possible_table_selectors:
                    # check for table border
                    declaration_text = rule.declaration_block.text
                    if "border" in declaration_text:
                        table_border = True

                # check th styles (padding & overall)
                if selector in possible_th_selectors:
                    th_styles = rule.declaration_block.text
                    th_padding = "padding" in th_styles
                    th_border = "border" in th_styles

                # check td styles (padding & overall)
                if selector in possible_td_selectors:
                    td_styles = rule.declaration_block.text
                    if not td_padding:
                        td_padding = "padding" in td_styles
                    if not td_border:
                        td_border = "border" in td_styles

                for group in possible_multiple_selectors:
                    if selector == group:
                        group_styles = rule.declaration_block.text
                        # only check the styles if they have not
                        # previously been applied (it doesn't hurt to
                        # change False to False, but it would hurt to
                        # go from True to False)
                        if not table_border:
                            table_border = "border" in group_styles
                        if not td_padding:
                            td_padding = "padding" in group_styles
                        if not td_border:
                            td_border = "border" in group_styles
                        if not th_padding:
                            th_padding = "padding" in group_styles
                        if not th_border:
                            th_border = "border" in group_styles

            # Check table border
            if table_border:
                message = "applies a border to table"
            else:
                message = "does not apply a border to the table"
            additional_table_data.append((filename, "table_border", message))

            # Check for passing or not
            if th_styles and td_styles:
                # both must be present for this check
                if th_styles != td_styles:
                    message = "has different th and td styles applied"
                else:
                    message = "has same styles applied to th and td"
            else:
                message = "does not apply any styles to the th nor"
                message += " td tags"
                if th_styles:
                    message = "only applies styles to the th tag"
                if td_styles:
                    message = "only applies styles to the td tag"
            additional_table_data.append((filename, "cell_styles",
                                          message))

            # check for padding applied
            if th_padding and th_padding:
                message = "applies padding to both th and td tags"
            elif th_padding:
                message = "applies padding to only th tag"
            elif td_padding:
                message = "applies padding to the td tag"
            else:
                message = "applies padding to neither th nor td tag"
            additional_table_data.append((filename, "cell_padding", message))

            # Check for borders applied
            if th_border and td_border:
                message = "applies border to both th and td tag"
            elif th_border:
                message = "applies border to only th tag"
            elif th_border:
                message = "applies border to only the td tag"
            else:
                message = "applies border to neither th nor td tag"
            additional_table_data.append((filename, "cell_border", message))
    return additional_table_data


prep_global_color_tests(global_color_contrast_tests,
                        global_color_rules)
font_families_tests = get_unique_font_families(project_path)
font_rules_results = get_font_rules_data(font_families_tests)
font_selector_results = get_font_selector_data(font_families_tests)
font_family_results = get_font_family_data(font_families_tests)
all_color_rules_results = get_all_color_rule_results(project_path)
style_attributes_data = set_style_attribute_tests(project_path)
if not style_attributes_data:
    style_attributes_data = [(file, "no tag", "applies style attribute")]
link_colors = css.get_link_color_data(project_path)
additional_table_data = prep_additional_table_styles(styles_by_html_files)


@pytest.fixture
def project_folder():
    return project_path


@pytest.fixture
def all_color_data():
    return all_color_rules_results


@pytest.fixture
def html_styles():
    return styles_by_html_files


@pytest.fixture
def html_docs():
    return html_files


@pytest.fixture
def link_color_details():
    return link_colors


@pytest.mark.parametrize("file,tag,value", style_attributes_data)
def test_files_for_style_attribute_data(file, tag, value):
    if tag == "no tag" and value == "applies style attribute":
        results = f"{file} passes with no style attributes."
        expected = results
        assert results == expected
    else:
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


@pytest.mark.parametrize("file,selector,ratio,results",
                         global_color_contrast_tests)
def test_files_for_global_color_contrast(file, selector, ratio, results):
    result = f"Color contrast for {selector} passes with {ratio} ratio."
    expected = result
    if not results:
        results = f"Color contrast for {file} failed."
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


def test_files_for_table_colors(html_docs, all_color_data):
    # assume true until proven otherwise
    sets_table_color = True
    passes_contrast = True
    for doc in html_docs:
        table_selectors = html.get_possible_selectors_by_tag(
            doc, "table"
            )
        for datum in all_color_data:
            if doc == datum[0]:
                target = datum[1]
                if target in table_selectors:
                    # we targetted the table
                    sets_table_color = sets_table_color and True
                    passes_contrast = passes_contrast and datum[6]
    assert sets_table_color and passes_contrast


def test_files_for_table_items(html_docs, all_color_data):
    # Assume they pass until otherwise
    passes_rows = True
    passes_cells = True

    # just in case there are multiple applications
    passes_tr_color = []
    passes_td_and_th = []
    row_data = []
    cell_data = []
    for doc in html_docs:
        tr_selectors = html.get_possible_selectors_by_tag(
            doc, "tr"
            )
        html.add_if_not_in(row_data, (doc, tr_selectors))
        th_selectors = html.get_possible_selectors_by_tag(
            doc, "th"
            )
        td_selectors = html.get_possible_selectors_by_tag(
            doc, "td"
            )
        cell_selectors = th_selectors + td_selectors
        html.add_if_not_in(cell_data, (doc, cell_selectors))
    for data in all_color_data:
        selector = data[1]
        # Check for rows
        for row in row_data:
            if selector in row[1]:
                passes_tr_color.append(data[6])

        # Check for th or tds
        for row in cell_data:
            if selector in row[1]:
                passes_td_and_th.append(data[6])

        # Check for multiple selectors
        if "," in selector:
            selectors = selector.split(",")
            for sel in selectors:
                for row in row_data:
                    if sel in row[1]:
                        passes_tr_color.append(data[6])
                for row in cell_data:
                    if sel in row[1]:
                        passes_td_and_th.append(data[6])
    for test in passes_tr_color:
        passes_rows = passes_rows and test
    for test in passes_td_and_th:
        passes_cells = passes_cells and test
    assert passes_rows or passes_cells


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


@pytest.mark.parametrize("file,test,result", additional_table_data)
def test_for_additional_table_data(file, test, result):
    results = f"{file} {result}"
    if test == "table_border":
        expected = f"{file} applies a border to table"
    if test == "cell_styles":
        expected = f"{file} has different th and td styles applied"
    if test == "cell_padding":
        expected = f"{file} applies padding to both th and td tags"
    if test == "cell_border":
        expected = f"{file} applies border to both th and td tag"
    assert results == expected
