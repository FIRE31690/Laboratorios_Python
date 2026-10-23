python = {"Ana", "Carlos", "Laura", "Sara"}
java = {"Laura", "Sara", "David", "Pablo"}
print("Al menos uno:", python | java)
print("Ambos:", python & java)
print("Solo Python:", python - java)
print("Solo Java:", java - python)
print("Uno solo:", python ^ java)
