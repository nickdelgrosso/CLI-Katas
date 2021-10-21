# Creating Python Programs for The Shell Terminal

## The Shell Terminal

The "Shell" is the text terminal that is designed to directly control your operating system and filesystem.
For that reason, it makes it straightforward to do specific types of tasks.

Most commands on the shell have the same syntax:

```
command subcommand argument1 argument2 --optionalargument optionalargumentvalue 
```

The most important thing to know, though, is how to get help:

```command --help```

  - Changing the current directory:
    - `cd Desktop`
    - `cd ..`
    - `cd /users/Nick/Desktop/SecretPythonProject/scripts`
  - Making new directories:
    - `mkdir NewFolder`
  - Running Programs:
    - Pycharm: `pycharm`
      - `pycharm --help`
    - Jupyter Lab: `jupyter lab`
      - `jupyter lab --help`
    - Python: `python`
      - `python --help`
    - Get Python version: `python --version`
    - Install Python packages `pip install numpy`
      - `pip --help` 
      - `pip install --help`
    

## Argparse

Python's built-in `argparse` package makes it so you can write Python scripts that have shell terminal
arguments, too!  

Docs: https://docs.python.org/3/library/argparse.html

## Exercises

Use the included `download_data.py` program to download datasets, for use
in the `plot_hist.py` and `profile_csv.py` scripts! Then modify those scripts
so they accept inputs in the terminal, too!

**Note**: You'll likely need to `pip install` some packages in order to get these to work.  
Look for the import errors to see which packages need installing.






