@echo off
cls
set /p exts="Enter extension of files: "
for %%i in ("*.%exts%") do (set fname=%%i) & call :rename
goto :eof
:rename
::Cuts off 1st five chars, then appends prefix
ren "%fname%" "%fname:~5%"
goto :eof
