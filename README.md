<!-- This is a README file for an online tutorial. -->

# Python Data Visualization of Top Car Horsepower with Bokeh

## Repository Description

This repository contains the code for generating an interactive horizontal bar chart displaying the highest horsepower cars in the world as an HTML page.

## Steps to Create a Virtual Environment with Pipenv

- Install Python to get access to `pip` tool
- Run `pip install pipenv` to get access to `pipenv` command
- Run `pipenv shell` to create or activate the virtual environment
- `Pipfile` file created
- Run `pipenv install bokeh pandas` to install the packages in the virtual environment
- `Pipfile.lock` file created
- Run `python main.py` to generate the HTML output file

## Steps to Remove a Virtual Environment

- Run `pipenv --venv` to check where the virtual environment folder is located (inside `.virtualenvs`)
- Remove the entire directory (`pyvenv.cfg` file inside) with the same name as the virtual environment
- Restart IDE (e.g., Visual Studio Code)

## References

- [YouTube](https://www.youtube.com/watch?v=2TR_6VaVSOs)
- [bokeh.palettes documentation](https://docs.bokeh.org/en/latest/docs/reference/palettes.html)
- [bokeh.embed documentation](https://docs.bokeh.org/en/latest/docs/reference/embed.html#bokeh.embed.components)
- [bokeh.models.tools documentation](https://docs.bokeh.org/en/2.4.2/docs/reference/models/tools.html#hovertool)
