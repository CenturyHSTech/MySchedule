# MySchedule
Demonstrate your ability to mark up and style tables.

***NOTE: this is part 1 of an on-going project***

**[Environment Set Up](#environment-set-up)** | **[Coding Your Project](#coding-your-project)** | **[Required Elements](#required-elements)**

## Environment Set up 
Getting your project up and running in VS Code.
1. Clone this project: `git clone`.
2. Open the project in VS Code (double click on `About-Me-HTML-Part-1.code-workspace`)
3. Open the terminal (View > New Terminal).
4. Install the Python extension: ***Python extension for Visual Studio Code***
5. In the terminal, type `poetry shell`.
    - You should see a line saying something like `Spawning shell within C:\Users\my_username\AppData\Local\pypoetry\Cache\virtualenvs\simple-html-page-IMtvp_MA-py3.9`
6. Note the name of your virtual environment file, which will look something like `simple-html-page-IMtvp_MA-py3.9`
7. Open the Command Palette 
    - in the menu it's: View > Command Palette
    - you could also type `Ctrl + Shift + P`
8. Type Python: Select Interpreter
    - if you see the virtual environment file, click it.
    - if you don't see it, click `Select at Workspace level`
9. Select the virtual environment file from above (it should show the word Poetry in blue on the right)
    - if you don't see it, close VS Code and re-open it and repeat steps 8 and 9.
10. Type `poetry update` and wait for everything to install.
11. In the terminal, once everything is done installing, type `pytest`
12. If that doesn't work, click the Testing icon (looks like a beaker), then click the blue `Configure Python Tests` button, then select `pytest pytest framework` and choose the `tests` folder
13. If that still doesn't work, ask your teacher to help you out.
14. Follow the steps in [Coding Your Project](#coding-your-project).
15. At key stopping points (usually once you test something in the browser and you like it), it's time to commit and push your changes like so...
    * `git add *`
    * `git commit -m "fixing/editing/adding ______"`
    * `git push origin main`
16. If you want to see if you are doing it right, check your code by typing `pytest`.
17. Once you think you're done, save your changes, make one last commit and push, and turn in your assignment by clicking the "Mark as Done" button.

**[Environment Set Up](#environment-set-up)** | **[Coding Your Project](#coding-your-project)** | **[Required Elements](#required-elements)** | **[Back to the top](#about-me-page-html-part-1-project)**

## Coding Your Project
Once the environment is set up, and you're ready to code...

1. Create a file named `index.html` in the `project` folder.
2. Follow teacher instructions on creating your web page.
3. Be sure to name your file in the title tag as well as in the body with an `h1` tag.
4. Be sure to include all required tags for any web page (see the [list of required elements](#required-elements) to make sure you meet minimum requirements).
5. Create and label two tables for your page:
    * One table for your A day schedule
    * One table for your B day schedule
6. When creating a label for your table, you may choose one of two options:
    1. you could put an `h2` before the `table` tag 
       OR
    2. you could put the label in the `caption` tag
7. For each table, make sure you meet the following requirements:
    * You must have column headers using the `th` tag.
    * You must have 4 columns: period, class, teacher, and room
    * You must have at least 6 rows:
        - one for the headers
        - one for each of the 4 periods in a day
        - one for lunch
    * The lunch row should merge across all of the columns.
    * You provide a border around...
        - the table itself
        - each cell
    * You provide a different background color and color for the table than the entire page.
    * You provide a different background color and color for the table headers.
    * Any additional colors are optional, but when applied, they must meet color contrast requirements.
    * You provide a border around the table and around each row &/or cell.
    * All cells and headers have padding applied.
    * No matter what styles you provide...
        - ***everything must be readable***
        - ***no text should be touching a border or edge of the screen***

*NOTE: as you are codign your page, be sure to check your page for errors using the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)*


**[Environment Set Up](#environment-set-up)** | **[Coding Your Project](#coding-your-project)** | **[Required Elements](#required-elements)** | **[Back to the top](#about-me-page-html-part-1-project)**

## Required Elements
### HTML Main Requirements
* Standard HTML Tags - there should be one for each page (no more no less)
    - `DOCTYPE`
    - `html`
    - `head`
    - `title`
* Other required tags (see minimum #)
    - `h1` -> one
    - `h2` or `thead` -> two
    - `table` -> two
    - `tr`  -> at least 6 per table (one for the header, and one for each period)
    - `th`  -> at least 4 per table (in the first `tr`)
    - `td` -> at least 16 per table (4 for each `tr` after the 1st.) 

### Validity Requirements
* No HTML errors are allowed

### CSS Requirements
* Do NOT use style attributes in your HTML - only use a style tag in the head or an external stylesheet.
* Colors:
    - ALL COLORS must meet [WebAIM color contrast](https://webaim.org/resources/contrastchecker/) goals at the following levels:
        * Headings must at least meet ***"WCAG AA"*** rating
        * Body text (table content and links included) must meet ***"WCAG AAA"*** rating
    - Apply a **background color** to the page (through the body or html)
    - Apply a **color** to the text (through the body or html)
    - Apply a **color** to hyperlinks (to both the link and visited - hover is optional)
    - Apply a **background color AND color** to one or more of the following elements: 
        * `table`, 
        * `tr`, OR
        * `th` and `td` (NOTE: if set it on one of these, you MUST set it on both)
    - Apply a **styled border** around the table
    - Apply a **thinner border** around the cells
    - Style the `th` elements differently from the `td` elements
    - Add **padding** to all `th` and `td` elements.
    - [OPTIONAL] add border-collapse to remove the gaps between borders (it almost always looks better)

NOTE: to check for errors, be sure to upload your HTML file to the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)


**[Environment Set Up](#environment-set-up)** | **[Coding Your Project](#coding-your-project)** | **[Required Elements](#required-elements)** | **[Back to the top](#about-me-page-html-part-1-project)**