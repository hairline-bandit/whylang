param ($file)

Start-Process "python" -ArgumentList "main.py $file" -Wait -NoNewWindow
Start-Process "python" -ArgumentList "randomnameforthis.py" -Wait -NoNewWindow

Remove-Item "randomnameforthis.py"