@echo off
echo Installing dependencies...
pip install selenium requests
echo Running Python tests...
python test_brokenimages.py
echo Done.
pause