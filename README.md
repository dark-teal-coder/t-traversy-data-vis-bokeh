<!-- README file for YouTube tutorials -->
<!-- [YouTube](https://www.youtube.com/watch?v=2TR_6VaVSOs) -->

# Python Data Visualization of Top Car Horsepower with Bokeh

## Metadata

- <ins>Project Owner</ins>: [@dark-teal-coder](github.com/dark-teal-coder)
- <ins>First Published Date</ins>: 2022-10-08

## Project

- **Title**: *Python Data Visualization of Top Car Horsepower with Bokeh*
- **Difficulty**:
  - [ ] Beginner
  - [x] Intermediate
  - [ ] Advanced
- **Scale**:
  - [x] Small
  - [ ] Medium
  - [ ] Large

## Repository Description

This repository contains the code for generating an interactive horizontal bar chart displaying the highest horsepower cars in the world as an HTML page (`index.html`).

## Installation 

### Python Development Tools

- Python 3
  - [Download and install Python 3 from python.org](https://www.python.org/downloads). 
- Python Package Installer/Manager `pip`
  - If you installed Python from [python.org](https://www.python.org), you should already have `pip`. If it is not installed, you can use the command `py -m ensurepip --default-pip` to bootstrap it from the standard library. If you are using Linux, you will have to [install the package manager separately](https://packaging.python.org/en/latest/guides/installing-using-linux-tools/). You can find out more about the `pip` tool [here](https://pip.pypa.io/en/stable/getting-started/). 
- Text Editor and Integrated Development Environment (IDE)
  - [Download and install the text editor Notepad++](https://notepad-plus-plus.org/downloads). 
  - [Download and install the IDE Visual Studio Code (VS Code)](https://code.visualstudio.com/download). 
  - [Install the web-based app Jupyter Notebook with pip](https://jupyter.org/install#jupyter-notebook)
  - [Install the web-based IDE JupyterLab with pip](https://jupyter.org/install#jupyterlab)
  - [Install Anaconda to get Jupyter Notebook](https://docs.jupyter.org/en/latest/install/notebook-classic.html#installing-jupyter-using-anaconda-and-conda)
- Command-line interface (CLI) 
  - You can [install the open-source PowerShell on Windows, Linux and macOS](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) if you do not have or want to use a pre-installed CLI on your local machine. 

### Python Libraries

Check if you have Python installed using the command `python --version`, or simply, `python version`, in the CLI. [Git-clone the project repository from Github](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) to the local machine. Use the command `py -m pip install package_name` to install the necessary Python libraries. Check out [pip documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to learn more about `pip install`. Check the top part of the `.py` script file for the list of libraries required. For example, you may need `requests` and `beautifulsoup4` libraries if you see the following lines in the top part of the script file: 
```
import requests
from bs4 import BeautifulSoup
```
If `pip` fails to locate the relevant packages, you may find it at [Python Package Index (PyPI)](https://pypi.org/). Use `python file_name.py` to run the script in a CLI. Or, use an IDE, such as VS Code, to run the script. There will usually be a [Run] button in the top right corner of the opened script file. 

## Instructions

### To Get All the Files in the Current Repository

- Click [Code]
- Click [Download ZIP]
- Extract the .zip file to the working directory

### To Fork a Repo and Clone it Locally

To access all of the files, fork this repo and then clone it locally.

For more information, please refer to [Fork a repo](https://docs.github.com/en/get-started/quickstart/fork-a-repo).

### To Create and Use a Virtual Environment with Pipenv

- Install Python to get access to `pip` tool
- Run `pip install pipenv` to get access to `pipenv` command
- Run `pipenv shell` to create or activate the virtual environment (`Pipfile` file created)
- Run `pipenv install bokeh pandas` to install the packages in the virtual environment (`Pipfile.lock` file created)

### To Run the Program

1. Click \[Run\] in an integrated development environment (IDE) (e.g., Visual Studio Code)
2. Run `python main.py` in a command-line interface (CLI)

### To Remove a Virtual Environment

- Run `pipenv --venv` to check where the virtual environment folder is located (inside `.virtualenvs`)
- Remove the entire directory (`pyvenv.cfg` file inside) with the same name as the virtual environment
- Restart IDE

## Credits 

### Contributors 

- [@dark-teal-coder](github.com/dark-teal-coder)

### References 

- [bokeh.palettes documentation](https://docs.bokeh.org/en/latest/docs/reference/palettes.html)
- [bokeh.embed documentation](https://docs.bokeh.org/en/latest/docs/reference/embed.html#bokeh.embed.components)
- [bokeh.models.tools documentation](https://docs.bokeh.org/en/2.4.2/docs/reference/models/tools.html#hovertool)

&nbsp;

*1st Completion Date: Oct 16, 2022*&emsp;
