lista_medicamentos = [
    {"codigo_lote": "L-101", "nombre": "Amoxicilina",            "costo_unitario": 15.0, "stock": 100, "laboratorio": "Bayer",  "tipo": "nacional",  "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-102", "nombre": "Insulina",               "costo_unitario": 80.0, "stock": 50,  "laboratorio": "Novo",   "tipo": "importado", "vencido": False, "cadena_frio": True},
    {"codigo_lote": "L-103", "nombre": "Ibuprofeno",             "costo_unitario": 5.0,  "stock": 0,   "laboratorio": "Bago",   "tipo": "nacional",  "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-104", "nombre": "Vacuna Antigripal",      "costo_unitario": 120.0,"stock": 200, "laboratorio": "Sanofi", "tipo": "importado", "vencido": False, "cadena_frio": True},
    {"codigo_lote": "L-105", "nombre": "Paracetamol",            "costo_unitario": 2.0,  "stock": 500, "laboratorio": "Bago",   "tipo": "nacional",  "vencido": True,  "cadena_frio": False},
    {"codigo_lote": "L-106", "nombre": "Tratamiento Oncológico", "costo_unitario": 5000.0,"stock": 12, "laboratorio": "Roche",  "tipo": "importado", "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-107", "nombre": "Suero Fisiológico",      "costo_unitario": 10.0, "stock": 80,  "laboratorio": "Bayer",  "tipo": "nacional",  "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-108", "nombre": "Antibiótico Premium",    "costo_unitario": 300.0,"stock": 150, "laboratorio": "Pfizer", "tipo": "importado", "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-109", "nombre": "Vitamina C",             "costo_unitario": 12.0, "stock": 40,  "laboratorio": "Bayer",  "tipo": "nacional",  "vencido": False, "cadena_frio": False},
    {"codigo_lote": "L-110", "nombre": "Antiviral", "costo_unitario": 45.0, "stock": 60,  "laboratorio": "Roche",  "tipo": "nacional",  "vencido": False, "cadena_frio": False},
]

# A
def generar_indice_seguro(lista_medicamentos):
    diccionario_indice = {}
    cantidad_descartados = 0

    for medicamento in lista_medicamentos:
        vencido = medicamento.get("vencido", False)
        stock = medicamento.get("stock", 0)
        codigo_lote = medicamento.get("codigo_lote")

        if vencido or stock == 0:
            cantidad_descartados += 1
        else:
            diccionario_indice[codigo_lote] = medicamento

    return diccionario_indice, cantidad_descartados
# B
def auditar_valor_inventario(indice_medicamentos):
    lista_auditada = []

    for lote, datos in indice_medicamentos.items():

        tipo = datos.get("tipo", "nacional").lower()
        stock = datos.get("stock", 0)
        costo_unit = datos.get("costo_unitario", 0)

        if tipo == "importado":
            costo_total = stock * costo_unit * 1.15
        else:
            costo_total = stock * costo_unit

        if costo_total > 50000:
            item_auditado = dict(datos)
            item_auditado["costo_total"] = round(costo_total, 2)
            lista_auditada.append(item_auditado)

    lista_ordenada = sorted(
        lista_auditada,
        key=lambda x: (x['tipo'], -x['costo_total'])
    )

    return lista_ordenada

# C
def generar_menu_proveedores(indice_medicamentos):
    menu = {}

    for codigo_lote, med in indice_medicamentos.items():

        laboratorio = med.get("laboratorio", "Desconocido")

        med_copia = dict(med)
        med_copia.pop("laboratorio", None)

        if med_copia.get("cadena_frio"):
            med_copia["alerta_logistica"] = "Prioridad Alta"
        else:
            med_copia["alerta_logistica"] = "Estándar"

        menu.setdefault(laboratorio, []).append(med_copia)

    return menu