import re

text = """
            INTERESES DE FINANCIACION                                                                    222,59                
            INTERESES COMPENSATORIOS                                                                    4691,51                
            INTERESES PUNITORIOS                                                                         763,32                
            IMPUESTO DE SELLOS                                                                          7354,85           0,03 
            PERCEPCION IVA DTO 354/18                                                                    727,62                
            PERCEP.AFIP RG 4815 30%                                                                     1039,45                
            PERC IIBB SERV DIG BS AS                                                                      69,30                
"""

pattern_tax = re.compile(r"^\s*(INTERESES|IMPUESTO|PERCEP\.|PERC\s|IVA|TRANSFER|SALDO PENDIENTE)(.*?)\s+([\d\.]*\,\d{2})(?:\s+[\d\.]*\,\d{2})?$", re.MULTILINE)

for line in text.split('\n'):
    if line.strip():
        match = pattern_tax.match(line)
        if match:
            print(f"MATCH: {match.group(0)}")
        else:
            print(f"NO MATCH: {line}")
