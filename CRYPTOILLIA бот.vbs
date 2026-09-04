' Запускает Telegram Desktop и сразу открывает бота CRYPTOILLIA
Option Explicit

Dim botUrl, tgPath, shell, fso, candidates, i

botUrl = "https://t.me/CRYPTOILLIA_bot"
Set shell = CreateObject("WScript.Shell")
Set fso = CreateObject("Scripting.FileSystemObject")

candidates = Array( _
  shell.ExpandEnvironmentStrings("%LOCALAPPDATA%") & "\Programs\Telegram\Telegram.exe", _
  shell.ExpandEnvironmentStrings("%APPDATA%") & "\Telegram Desktop\Telegram.exe", _
  shell.ExpandEnvironmentStrings("%ProgramFiles%") & "\Telegram Desktop\Telegram.exe", _
  shell.ExpandEnvironmentStrings("%ProgramFiles(x86)%") & "\Telegram Desktop\Telegram.exe", _
  "D:\Telegram Desktop\Telegram.exe", _
  "C:\Telegram Desktop\Telegram.exe" _
)

tgPath = ""
For i = 0 To UBound(candidates)
  If fso.FileExists(candidates(i)) Then
    tgPath = candidates(i)
    Exit For
  End If
Next

If tgPath <> "" Then
  shell.Run """" & tgPath & """ """ & botUrl & """", 1, False
Else
  shell.Run "tg://resolve?domain=CRYPTOILLIA_bot", 1, False
End If
