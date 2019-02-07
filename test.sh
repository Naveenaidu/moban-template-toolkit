pip freeze
nosetests --with-coverage --cover-package moban_template_toolkit --cover-package tests tests  docs/source moban_template_toolkit && flake8 . --exclude=.moban.d,docs --builtins=unicode,xrange,long
