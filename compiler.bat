@echo off
set NLM=^


set NL=^^^%NLM%%NLM%^%NLM%%NLM%
echo using flags: "--onefile, -w"
set /p file= .py file name? %NL%
pyinstaller --onefile -w %file% 
set /p end= %NL%Done, press ENTER to quit