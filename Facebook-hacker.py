v = '\033[0;34m'
f = '\033[0;35m'
print(v + '''

  ______             _                 _     
 |  ____|           | |               | |    
 | |__ __ _  ___ ___| |__   ___   ___ | | __ 
 |  __/ _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ / 
 | | | (_| | (_|  __/ |_) | (_) | (_) |   <  
 |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\ 

                                             Facebook hacker                                              
''')
print(f + ''' 
 [1]     show a breakthrough 
  ''')
import requests
chinput=input("choose a number :")
if chinput=='1':
	import subprocess
	SOS_filename = "example.py"  
	subprocess.run(["python SOS", "SOS", SOS_filename], shell=True)





