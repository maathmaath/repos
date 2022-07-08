@echo off
:x
set /p Input=Would you want to clear a printer queue? (y/n):
echo %Input%
if '%Input%'=='y' goto y
if '%Input%'=='n' goto :eof

:y
powershell -Command "echo 'List of available printers:';get-printer | format-list Name,JobCount,PrinterStatus;"^
			"$printername = read-host 'Please enter the printer name whose queue needs to be cleared';"^
			"echo 'Clearing the queue for the printer:' $printername;"^
			"& {Get-PrintJob -ComputerName $env:computername -PrinterName $printername |  Remove-PrintJob};"

echo.
goto x
