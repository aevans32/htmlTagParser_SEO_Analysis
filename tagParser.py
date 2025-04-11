import argparse
from bs4 import BeautifulSoup
from collections import Counter
import sys

def analizar_encabezados(html_path):
    try:
        # Cargar el archivo HTML renderizado
        with open(html_path, "r", encoding="utf-8") as file:
            soup = BeautifulSoup(file, "html.parser")
    except FileNotFoundError:
        print(f"Error: El archivo {html_path} no se encuentra.")
        sys.exit(1)

    header_counts = Counter()
    logical_hierarchy = []
    warnings = []

    # Verificar si el archivo HTML tiene encabezados
    all_headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

    last_level = 0
    for tag in all_headers:
        level = int(tag.name[1])
        text = tag.get_text(strip=True)
        header_counts[tag.name] += 1
        logical_hierarchy.append((" " * (level - 1)) + f"{tag.name.upper()}: {text if text else '[VACÍO]'}")

        # Detectar encabezados vacíos
        if not text:
            warnings.append(f"Advertencia: <{tag.name.upper()}> vacío")

        # Detectar salto de jerarquía (más de un nivel)
        if last_level and level > last_level + 1:
            warnings.append(f"Advertencia: Salto de jerarquía <{tag.name.upper()}> sigue a <H{last_level}>")

        # Detectar encabezados fuera de orden
        if level < last_level and level != 1:
            # H1 puede estar antes o después sin ser error
            if f"h{level}" not in header_counts:
                warnings.append(f"Advertencia: <{tag.name.upper()}> aparece antes de un encabezado del mismo nivel o superior")

        last_level = level

    # Reglas globales SEO
    if header_counts['h1'] == 0:
        warnings.append("Advertencia: No se encontró ningún <H1>.") 
    elif header_counts['h1'] > 1:
        warnings.append("Advertencia: Hay más de un <H1> en la página (debería haber sólo uno).")

    
    # Guardar el resultado en un archivo
    output_file = html_path.rsplit(".", 1)[0] + "_output.txt"
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("=== Encabezados encontrados ===\n")
        for header in sorted(header_counts.keys()):
            out.write(f"{header.upper()}: {header_counts[header]}\n")

        out.write("\n=== Jerarquía lógica ===\n")
        for line in logical_hierarchy:
            out.write(line + "\n")

        out.write("\n=== Advertencias SEO ===\n")
        if warnings:
            for warning in warnings:
                out.write(warning + "\n")
        else:
            out.write("No se encontraron advertencias SEO.\n")

    print(f"Análisis completado. Resultados guardados en {output_file}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analiza encabezados en un archivo HTML.")
    parser.add_argument("html_path", help="Ruta al archivo HTML o.txt a analizar.")
    args = parser.parse_args()

    analizar_encabezados(args.html_path)
