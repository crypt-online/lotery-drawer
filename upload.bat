del dist\*.*?
py setup.py sdist bdist_wheel
py -m twine upload --repository pypi dist/* --config-file .twine