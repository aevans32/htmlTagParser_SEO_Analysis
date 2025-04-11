# 🧠 SEO Header Analyzer

Este script en Python analiza el HTML renderizado de una página web para identificar cuántas veces se usan las etiquetas `<h1>`, `<h2>`, `<h3>`, `<h4>`, `<h5>` y `<h6>`. También detecta si estas etiquetas están siendo usadas en un orden lógico o si hay saltos que podrían afectar la estructura SEO de la página.

## ✅ Funcionalidades

- Cuenta las veces que se usa cada tipo de encabezado (`h1` a `h6`)
- Construye una jerarquía lógica en función del orden de aparición y del nivel de los encabezados
- Genera advertencias SEO automáticas, como:
  - ❌ Falta de `<h1>`
  - ❌ Múltiples `<h1>` en la misma página
  - ⚠️ Encabezados vacíos
  - ⚠️ Saltos en la jerarquía de encabezado (`h2` → `h5`)
  - ⚠️ Orden de aparición incoherente (`h3` antes de `h2`)

## 📦 Requisitos

  - Python 3.x
  - BeautifulSoup4

## 🧪 Uso

```bash
python tagParser.py archivo.html
