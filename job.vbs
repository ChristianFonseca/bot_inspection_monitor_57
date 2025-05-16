Set WshShell = CreateObject("WScript.Shell")
' Segundo parámetro = 0 → ventana oculta, tercer parámetro = False → no espera a que termine
WshShell.Run """F:\kick\bot_inspection_monitor_57\local\job.bat""", 0, True
