@echo off
chcp 65001 >nul
setlocal

set "BOT=https://t.me/CRYPTOILLIA_bot"
set "TG="

if exist "%LOCALAPPDATA%\Programs\Telegram\Telegram.exe" set "TG=%LOCALAPPDATA%\Programs\Telegram\Telegram.exe"
if exist "%APPDATA%\Telegram Desktop\Telegram.exe" set "TG=%APPDATA%\Telegram Desktop\Telegram.exe"
if exist "%ProgramFiles%\Telegram Desktop\Telegram.exe" set "TG=%ProgramFiles%\Telegram Desktop\Telegram.exe"
if exist "%ProgramFiles(x86)%\Telegram Desktop\Telegram.exe" set "TG=%ProgramFiles(x86)%\Telegram Desktop\Telegram.exe"
if exist "D:\Telegram Desktop\Telegram.exe" set "TG=D:\Telegram Desktop\Telegram.exe"
if exist "C:\Telegram Desktop\Telegram.exe" set "TG=C:\Telegram Desktop\Telegram.exe"

if defined TG (
  start "" "%TG%" "%BOT%"
  exit /b 0
)

REM Если Telegram.exe не найден — открываем через протокол tg://
start "" "tg://resolve?domain=CRYPTOILLIA_bot"
exit /b 0
