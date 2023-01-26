menu={
  "helado":20
}

dinero = int(input(""))
for i in range(len(menu)):
  print(f"{i+1}. {menu}")
  print("\n")
orden = str(input("selecione algo del menu: "))

def cambio():
  times = orden.split(",")
  exchange = (menu[times[0]]*int(times[1])) - dinero
  return exchange
print(f"{cambio()}$")
