These files are here to reproduce the output in the code scanners
The used commands can be used in the poetry shell, starting form the base repo-folder: 

bandit -f txt -o code_scanners_examples/bandit_report.txt code_scanners_examples/bad_security.py

safety check -r code_scanners_examples/bad_requirements.txt