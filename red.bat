@echo off
pytest -v -s -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser edge
rem pytest -v -s -m "sanity" --html=./Reports/report.html testCases/ --browser chrome


rem keyword is for command


pause