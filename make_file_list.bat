@echo off
setlocal enabledelayedexpansion
set "outputFile=files_list.txt"

:: Change the code page to UTF-8 to handle Cyrillic characters
chcp 65001

if exist "%outputFile%" (
    del "%outputFile%"
)

echo Processing files, please wait...
set /a processedFiles=0
set /a displayCounter=0
for /r %%i in (*) do (
    attrib "%%i" | find "SH" >nul || (
        echo %%i >> "%outputFile%"
        set /a processedFiles+=1
        set /a displayCounter+=1

        if !displayCounter! geq 10 (
            cls
            echo Processing files, please wait...
            echo Files processed: !processedFiles!
            set displayCounter=0
        )
    )
)

cls
echo Processing files, please wait...
echo Files processed: %processedFiles%
echo File list generated in %outputFile%.
pause
