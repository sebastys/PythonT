import calendar

x = calendar.month(2023,4)
fichero = open("calendario.txt",mode="w",encoding="utf-8")
fichero.write(x)
fichero.close()