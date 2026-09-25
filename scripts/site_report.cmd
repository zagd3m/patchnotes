@echo off
rem PowerShell/CMD entry point for scripts\site_report (live-site verification).
set "SCRIPT=%~dp0site_report"
where bash >nul 2>nul
if %errorlevel%==0 (
  bash "%SCRIPT%" %*
) else if exist "C:\Program Files\Git\bin\bash.exe" (
  "C:\Program Files\Git\bin\bash.exe" "%SCRIPT%" %*
) else (
  echo site_report: bash not found ^(Git for Windows required^) 1>&2
  exit /b 1
)
