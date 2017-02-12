import ast

with open('user.py', 'r') as f:
	c = ast.parse(f.read()).body[3]
	print(dir(c))
	print(c.bases)
	print(dir(c.bases[1]))
	print(dir(c.bases[0].ctx))
	print(c.bases[0].ctx._fields)
	#print(c.bases[1].id)