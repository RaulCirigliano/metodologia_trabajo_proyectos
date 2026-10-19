# Plantilla de Informe de Auditoría Web

Usar tal cual. Todo hallazgo lleva **evidencia concreta** (archivo y línea, comando y
resultado, captura o medición). Sin evidencia no es un hallazgo.

```markdown
# Auditoría web: <proyecto>  (<fecha>)

## Contexto
- Stack detectado:
- Cómo se sirve (localhost / hosting):
- Nivel aplicado: Base | Base + Publicación
- Modo: Auditar | Aplicar

## Resumen
2-4 líneas: estado general y los riesgos más importantes.

## Hallazgos
| # | Severidad | Área | Evidencia (archivo:línea / medición) | Problema de raíz | Recomendación |
|---|---|---|---|---|---|
Severidad: **Crítica** (rompe uso o seguridad) · **Alta** · **Media** · **Baja**

## Conteos de patrones (si hubo migración)
| Patrón viejo | Antes | Después | Excepciones justificadas |
|---|---|---|---|

## Sitios corregidos (solo modo Aplicar)
Lista de archivo:línea de cada cambio.

## Verificación ejecutada
Qué se corrió y qué resultó (navegador, Lighthouse, tests, validadores).

## NO VERIFICADO
Todo lo que no se pudo ejecutar o comprobar, y por qué.

## Pendiente
Lo que quedó sin hacer.

## Fuera de alcance detectado
Problemas vistos que no se pidieron; reportados, no arreglados.

## Supuestos
```
