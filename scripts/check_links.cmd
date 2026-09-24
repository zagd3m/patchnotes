@echo off
rem PowerShell/CMD entry point for scripts\check_links (jekyll build + lychee).
rem bash is NOT on PATH with a stock Git for Windows install — try PATH first,
rem then the standard install location.
set "SCRIPT=%~dp0check_links"
where bash >nul 2>nul
if %errorlevel%==0 (
  bash "%SCRIPT%" %*
) else if exist "C:\Program Files\Git\bin\bash.exe" (
  "C:\Program Files\Git\bin\bash.exe" "%SCRIPT%" %*
) else (
  echo check_links: bash not found ^(Git for Windows required^) 1>&2
  exit /b 1
)
