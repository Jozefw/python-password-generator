from prettytable import PrettyTable
table = PrettyTable()
table.add_column("PokeyMan",["guy","girl"])
table.add_column("Power",["Big Strength","Speed"])
table.align="l"
print (table)