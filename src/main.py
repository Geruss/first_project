#!/bin/env python3

def print_author():
	from dotenv import load_dotenv
	import os
	load_dotenv()
	author = os.getenv("AUTHOR")
	print(f"project's author: {author}")

print_author()
