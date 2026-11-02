# ----------------------------------------
#Part 1. Budget calculation
# ----------------------------------------
#import python package
from rich.console import Console
from rich.table import Table
console = Console()
#define each variable
precio_base = 8.0
edad_persona = input("Indica la edad, por favor:")
edad_persona = int(edad_persona)
cantidad_persona = input("Indica la cantidad de personas, por favor:")
cantidad_persona = int(cantidad_persona)
presupuesto = input("Indica el presupuesto, por favor:")
presupuesto = float(presupuesto)

#define calculation rules
if edad_persona < 12:
    porcentaje_descuento = 50

elif edad_persona >= 65:
    porcentaje_descuento = 25
else:
    porcentaje_descuento = 0

#calculate the real price with discount
descuento_persona = precio_base * porcentaje_descuento / 100
precio_entrada = precio_base - descuento_persona
precio_total = precio_entrada * cantidad_persona

#comparison between precio_total and presupuesto
dinero_sobra = presupuesto - precio_total
if dinero_sobra >= 0:
    console.print(f"El presupuesto es suficiente, sobra {dinero_sobra:.2f} euros 🥳", style="green")
else:
    console.print(f"El presupuesto no es suficiente, falta {abs(dinero_sobra):.2f} euros 😢,", style ="red")

# ----------------------------------------
#Part 2. Table presentation with Rich
# ----------------------------------------
tabla = Table(title="Resumen de compras", title_style="bold black")
tabla.add_column("Concepto")
tabla.add_column("Valor")
tabla.add_row("Edad", f"{edad_persona} años")
tabla.add_row("Cantidad de entradas", f"{cantidad_persona}")
tabla.add_row("Precio base", f"{precio_base:.2f} EUR")
tabla.add_row("Porcentaje de descuento", f"{porcentaje_descuento} %")
tabla.add_row("Descuento por entrada", f"{descuento_persona:.2f} EUR")
tabla.add_row("Precio final por entrada", f"{precio_entrada:.2f} EUR")
tabla.add_row("Presupuesto", f"{presupuesto:.2f} EUR")
tabla.add_row("Total", f"{precio_total:.2f} EUR")
console.print(tabla)