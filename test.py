#!/usr/bin/python3
print('Content-Type: text/html')
print('')
print(r'<html>')
print(r'<head> <title> Software Installation </title> </head>')
print(r'<body>')
print(r'<h1> Install/Uninstall Automation </h1>')
print(r'<p> choose a program to install </p>')
print(r'<form>')
print(r'<select name="program">')
print(r'<option value="elinks"> elinks </option>')
print(r'<option value="stress"> stress </option>')
print(r'</select>')
print(r'<br> <br>')
print(r'<button type="submit" name="ops" value="install" formaction="script"> Install </button>')
print(r'<button type="submit" name="ops" value="uninstall" formaction="script"> Uninstall </button>')
print(r'</form>')
print(r'</body>')
print(r'</html>')