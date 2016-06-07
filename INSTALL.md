# Installation

Before starting, make sure you have the graphviz headers on your system (we need them to build sphinx.ext.graphviz). Also you should have python, pip and virtualenv.

For now, you can only build out the docs:

    virtualenv .venv
    . .venv/bin/activate
    pip install -r requirements.txt
    cd docs
    make html

There will be more to do when there is more than docs here.