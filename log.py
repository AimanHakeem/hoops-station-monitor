from colorama import init
from termcolor import colored
init()

def log(tag, text):
	# Info tag
	if(tag == 'i'):
		print(colored('[MONITORING]', 'yellow') + text)
	# Error tag
	elif(tag == 'e'):
		print(colored('[ERROR]', 'red') + text)
	# Success tag
	elif(tag == 's'):
		print(colored('[SCRAPED]', 'green') + text)