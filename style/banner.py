import os
from os import system

RC, GC, YC, CC, DF = '\033[1;31m', '\033[1;32m', '\033[1;33m', '\033[1;36m', '\033[1;37m'

def banner():
	system('clear')
	print(f'''
      {GC}╭━━╮╱╱╭╮╱╱╱╱╱╱╭┳╮
      ╰╮╭┻┳━┫╰┳━┳╮╭━╋┫╰╮ 
      ╱┃┃┻┫━┫┃┃╋┃╰┫╋┃┃╭┫
      ╱╰┻━┻━┻┻┫╭┻━┻━┻┻━╯
      ╱╱╱╱╱╱╱╱╰╯ {DF}
''')



