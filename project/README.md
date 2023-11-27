# Simple HTML Page
Put your html file/s in here.

# Requirements
## HTML Main Requirements
* Standard HTML Tags - there should be one for each page (no more no less)
    - `DOCTYPE`
    - `html`
    - `head`
    - `title`
* Other required tags (see minimum #)
    - `h1` -> one per page (ONLY)
    - `h2` or `caption` -> 2
    - `table` -> 2
    - `tr` -> at least 12
    - `th` -> 8 (4 per table)
    - `td` -> 34 (16 per class, plus 1 for each lunch)

## CSS Requirements
* Be sure to add a font-pair (I recommend from Google Fonts)
    - one applied to the entire document (through the `html` or `body` tag)
    - a different one applied to the headers you use in your document
* Do NOT use style attributes in your HTML - only use a style tag in the head or an external stylesheet.
* Colors:
    - ALL COLORS must meet [WebAIM color contrast](https://webaim.org/resources/contrastchecker/) goals at the following levels:
        * Headings must at least meet ***"WCAG AA"*** rating
        * Body text (table content and links included) must meet ***"WCAG AAA"*** rating
    - Apply a **background color** to the page (through the body or html)
    - Apply a **color** to the text (through the body or html)
    - Apply a **color** to hyperlinks (to both the link and visited - hover is optional)
    - Apply a **background color AND/OR color** to one or more of the following elements and make sure it passes color contrast: 
        * `table`, 
        * `tr`, OR
        * `th` and `td` (NOTE: if set it on one of these, you MUST set it on both)
* Additional CSS table styles
    - Apply a **styled border** around the `table`
    - Apply a **thinner border** around the cells (`td` and `th`)
    - Style the `th` elements differently from the `td` elements
    - Add **padding** to all `th` and `td` elements.
    - [OPTIONAL] add border-collapse to remove the gaps between borders (it almost always looks better)

## Validity Requirements
* No HTML errors are allowed

NOTE: to check for errors, be sure to upload your HTML file to the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)
