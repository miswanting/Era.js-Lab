@echo off
echo Enviroment Checking...
@pip -V >nul
if %ERRORLEVEL% GTR 0 goto ErrorHunter
echo Installing...
:: https://pip.pypa.io/en/stable/user_guide/#requirements-files
pip install -r requirements.txt
pause
exit

:ErrorHunter
echo.
echo ERROR FOUND: %ERRORLEVEL%
echo Searching for HELP...
@ping -n 2 localhost > nul

goto ERR-%ERRORLEVEL%
echo Unknown Error!
echo You Can Contact Author for HELP!

:ERR-9009
echo Found!
echo.
echo ERR-9009: PIP_NOT_INSTALLED
echo We didn't recognise your pip program.
set /P c=Do you want to go through a Debug Process[y/n]?
if /I "%c%" EQU "n" echo Exiting... && pause && exit
echo Don't worry, Let's go through a Debug Process:
echo Have you installed python?
echo If not, please go to https://www.python.org/ to install one.
echo.
echo If this error still exist, please open a commandline/terminal,
echo and input "python" (without quotation mark and hit Enter)
echo to see if it running well.
echo if not, It's because you didn't put python path into System Path Enviroment.
echo.
echo If this error still exist, please open a commandline/terminal,
echo and input "python" (without quotation mark and hit Enter)
pause
exit
