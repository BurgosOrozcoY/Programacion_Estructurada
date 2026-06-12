cEmpleados = 0
op = "No"
sueldoF = 0

while op != "Stop":

    empleado = input("Ingresar nombre: ")
    horas = int(input("Ingresar horas laboradas: "))
    sueldoH = int(input("Ingresar sueldo por hora: "))

    cEmpleados = cEmpleados + 1

    if horas == 10:
        aumento = sueldoH * 0.2
        sueldoN = (sueldoH * horas) + aumento
    elif horas == 15:
        aumento = sueldoH * 0.3
        sueldoN = (sueldoH * horas) + aumento
    elif horas == 20:
        aumento = sueldoH * 0.25
        sueldoN = (sueldoH * horas) + aumento
    elif horas > 25:
        aumento = sueldoH * 0.08
        sueldoN = (sueldoH * horas) + aumento
    else:
        aumento = 0
        sueldoN = (sueldoH * horas)

    print(f"Aumento a pagar: {aumento}")
    print(f"Sueldo neto: {sueldoN}")

    sueldoF = sueldoF + sueldoN
    print("Teclear Stop para denegar.")
    op = input("Continuar?")

print(f"Empleados ingresados: {cEmpleados}")
print(f"Monto total de sueldos netos: {sueldoF}")