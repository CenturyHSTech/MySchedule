# About Me Page HTML Part 1 Project
Demonstrate that you are able to write and organize content for a single web page that contains a variety of HTML to display a title, section headers, paragraphs, links, text formatting, and lists.

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

1. If you have any of your project files in another folder, copy the files and paste in the `project` folder.
2. If you are starting from scratch, create a file named `index.html` in the `project` folder.
3. Follow teacher instructions on creating your web page.
4. Be sure to name your file in the title tag as well as in the body with an `h1` tag.
5. Read the [list of required elements](#required-elements) to make sure you meet minimum requirements.
6. Add your three sections: About Me, My Favorites, and My Schedule
7. Make sure each section has a section title using the `h2` element.
8. **In the *About Me* section...**
    * add at least 3 paragraphs using the `p` tag.
    * Add some text formatting.
    * Optionally, you may wish to work a link or two into your paragraphs (just know that you do need at least 2 links).
9.  **In the *My Favorites* section...**
    * Add an introductory paragraph about your favorites.
    * Add one or more lists (bullet or numbered).
    * For each list, include at least 3 list items (`li`)
10. You may leave the ***My Schedule*** empty for now, but just know that you will be adding a table.

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
    - `h1` -> one per page (ONLY)
    - `h2` -> at least 3 per page
    - `p`  -> at least 4 per page
    - `a`  -> at least 2 per page
* Formatting Elements
    - `strong` or `b` -> at least 2 per page (you can choose which one)
    - `em` or `i`     -> at least 2 per page (you choose which one)

### Minimum List Requirements
* At least 1 list (you can choose between `ol` or `ul`)
* At least 3 list items per list

### Validity Requirements
* No HTML errors are allowed

NOTE: to check for errors, be sure to upload your HTML file to the [W3C File Upload Validator](https://validator.w3.org/#validate_by_upload)


**[Environment Set Up](#environment-set-up)** | **[Coding Your Project](#coding-your-project)** | **[Required Elements](#required-elements)** | **[Back to the top](#about-me-page-html-part-1-project)**