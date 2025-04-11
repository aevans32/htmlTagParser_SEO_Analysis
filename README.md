Este script analiza el texto copiado del segmento <body> del desarrollo compilado de un sitio web con la finalidad de identificar cuantos tags de titulos y subtitulos (h1, h2, h3, h4, h5, h6) son usados.

Al mismo tiempo identifica los posibles errores de acuerdo a las mejores prácticas SEO.

Los posibles errores son:
Advertencia	                                            Explicación
❌ Falta de h1	                                        Toda página debería tener un único h1 principal
❌ Más de un h1	                                        Debería haber solo uno por página
⚠️ Saltos de jerarquía	                                Ej. pasar de h2 a h5 sin h3/h4 intermedios
⚠️ Títulos en el orden incorrecto	                      Como ver un h3 antes que cualquier h2
⚠️ Encabezados vacíos	                                  Títulos sin contenido de texto visible
