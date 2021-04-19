registers = {"name":"Jorge",
            "last name":"Roa",
            "age": None }

registers["sex"] = "male"

x = registers["last name"]
x1 = registers.get("last name")
x2 = registers.values()
x3 = registers.keys()

for key in registers.keys():
    registers[key] = "tcp entry"
    print(registers[key])

print(registers)