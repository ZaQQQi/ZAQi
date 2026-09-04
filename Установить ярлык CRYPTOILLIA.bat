@echo off
chcp 65001 >nul
setlocal EnableExtensions

set "DESKTOP=%USERPROFILE%\Desktop"
if not exist "%DESKTOP%" set "DESKTOP=%USERPROFILE%\OneDrive\Desktop"

set "APPDIR=%LOCALAPPDATA%\CRYPTOILLIA-bot-launcher"
mkdir "%APPDIR%" 2>nul

REM Копируем лаунчер рядом с ярлыком
copy /Y "%~dp0CRYPTOILLIA бот.vbs" "%APPDIR%\CRYPTOILLIA бот.vbs" >nul
if errorlevel 1 (
  echo Не найден файл "CRYPTOILLIA бот.vbs" рядом с этим установщиком.
  pause
  exit /b 1
)

REM Создаём ярлык на рабочем столе через PowerShell
powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$desk = [Environment]::GetFolderPath('Desktop');" ^
  "$w = New-Object -ComObject WScript.Shell;" ^
  "$s = $w.CreateShortcut((Join-Path $desk 'CRYPTOILLIA бот.lnk'));" ^
  "$s.TargetPath = $env:LOCALAPPDATA + '\CRYPTOILLIA-bot-launcher\CRYPTOILLIA бот.vbs';" ^
  "$s.WorkingDirectory = $env:LOCALAPPDATA + '\CRYPTOILLIA-bot-launcher';" ^
  "$s.WindowStyle = 7;" ^
  "$s.Description = 'Запуск Telegram и бота CRYPTOILLIA';" ^
  "$icons = @(" ^
  "  ($env:LOCALAPPDATA + '\Programs\Telegram\Telegram.exe')," ^
  "  ($env:APPDATA + '\Telegram Desktop\Telegram.exe')," ^
  "  ($env:ProgramFiles + '\Telegram Desktop\Telegram.exe')," ^
  "  (${env:ProgramFiles(x86)} + '\Telegram Desktop\Telegram.exe')" ^
  ");" ^
  "foreach ($p in $icons) { if (Test-Path $p) { $s.IconLocation = \"$p,0\"; break } };" ^
  "$s.Save();" ^
  "Write-Host ('Ярлык создан: ' + (Join-Path $desk 'CRYPTOILLIA бот.lnk'))"

echo.
echo Готово. На рабочем столе появился ярлык "CRYPTOILLIA бот".
echo По нажатию он запустит Telegram и сразу откроет бота.
echo.
pause
