from logica.logica import (
    lista_medicamentos,
    generar_indice_seguro,
    auditar_valor_inventario,
    generar_menu_proveedores
)

def mostrar_menu_proveedores(menu: dict):

    print("\n" + "═"*60)
    print("PANEL DE PROVEEDORES")
    print("═"*60)

    for laboratorio, medicamentos in sorted(menu.items()):

        print(f"\nLABORATORIO: {laboratorio}")

        for med in medicamentos:

            alerta = med.get("alerta_logistica")

            print(
                f"{med['nombre']} | "
                f"Lote: {med['codigo_lote']} | "
                f"Stock: {med['stock']} | "
                f"Alerta: {alerta} | "
                f"Tipo: {med['tipo']} | "
                f"Precio unitario: ${med['costo_unitario']}"
            )


def mostrar_auditoria(lista):

    print("\n" + "═"*60)
    print("AUDITORÍA INVENTARIO (> $50,000)")
    print("═"*60)

    if not lista:
        print("No hay medicamentos que superen el umbral")
        return

    for med in lista:

        print(
            f"{med['nombre']} | "
            f"Lote: {med.get('codigo_lote', 'N/A')} | "
            f"Lab: {med.get('laboratorio', 'N/A')} | "
            f"Costo total: ${med['costo_total']}"
        )

def main():

    indice, descartados = generar_indice_seguro(lista_medicamentos)

    print("\nÍNDICE GENERADO")
    print("Medicamentos válidos:", len(indice))
    print("Descartados:", descartados)

    auditoria = auditar_valor_inventario(indice)
    mostrar_auditoria(auditoria)

    menu = generar_menu_proveedores(indice)
    mostrar_menu_proveedores(menu)

if __name__ == "__main__":
    main()