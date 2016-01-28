@echo off
setlocal EnableExtensions EnableDelayedExpansion
cls

:: --------------------------------------------------------
::
:: HOW TO USE:
:: To use this .bat file for running and updating Sparkle-HDF5-
:: Extractor, make a copy of this file and rename it
:: something easy to remember (e.g. Sparkle-HDF5-Extractor.bat).
:: Now in the copy of this file you will want to change the
:: variable of "location" (line 24) with the path to the
:: Sparkle-HDF5-Extractor directory (where you found this file).
:: After you complete that you will want to change the
:: variable for "gitLocation" (line 28) with the path to
:: where your git.exe is stored. Once you have those set,
:: you can either create a shortcut to your newly edited
:: file or just run the .bat file. While running it with
:: this code, it will check for updates before running
:: and will ask the user if they wish to update if there
:: are any new updates.
::
:: Place your path to Sparkle-HDF5-Extractor here
set location="C:\Users\Joel\Documents\Sparkle-HDF5-Extractor\"
cd %location%
::
:: Place your path to Git here
set gitLocation="C:\Program Files (x86)\Git\bin"
SET PATH=%PATH%;%gitLocation%
::
:: --------------------------------------------------------

title Sparkle-HDF5-Extractor

:: Get versions of Sparkle-HDF5-Extractor
git remote update
for /f "delims=" %%i in ('git rev-parse @{0}') do set local=%%i
for /f "delims=" %%i in ('git rev-parse origin/master') do set remote=%%i
for /f "delims=" %%i in ('git merge-base @ origin/master') do set base=%%i

echo.

:: Check relation of various versions
if "%local%" equ "%remote%" (
    echo Sparkle-HDF5-Extractor is up to date.
    goto :runSparkle-HDF5-Extractor
) else if "%local%" equ "%base%" (
    echo A newer version of Sparkle-HDF5-Extractor is avaliable.
) else if "%remote%" equ "%base%" (
    echo Your local branch of Sparkle-HDF5-Extractor is ahead of origin/master.
    goto :runSparkle-HDF5-Extractor
)

set "answer=%globalparam1%"
goto :answerCheck

:updatePrompt
set /p "answer=Update Sparkle-HDF5-Extractor? (y or n): "
goto :answerCheck

:answerCheck
if not defined answer goto :updatePrompt

echo.

if "%answer%" == "y" (
    git pull
)

:runSparkle-HDF5-Extractor
echo.
python run.py