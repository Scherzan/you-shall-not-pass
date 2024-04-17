These files are here to reproduce the output in the code scanners
The used commands can be used in the poetry shell, starting form the base repo-folder: 

pylint code_scanners_examples/bad_linting.py 

radon cc code_scanners_examples/bad_complexity.py 

safety check -r code_scanners_examples/bad_requirements.txt