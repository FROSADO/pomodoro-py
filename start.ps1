$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = Join-Path $ScriptDir "venv\Scripts\pythonw.exe"
$MainScript = Join-Path $ScriptDir "main.py"

Start-Process -FilePath $PythonExe -ArgumentList $MainScript -WindowStyle Hidden

