import os
import re
import json
import fitz
from datetime import datetime

def parse_amount(amount_str):
    amount_str = re.sub(r'[−—–]', '-', amount_str).strip()
    amount_str = amount_str.strip()
    if not amount_str: return 0.0
    is_negative = False
    if amount_str.endswith('-') or amount_str.startswith('-'):
        is_negative = True
        amount_str = amount_str.replace('-', '').strip()
    
    amount_str = amount_str.replace('.', '').replace(',', '.')
    try:
        val = float(amount_str)
        return -val if is_negative else val
    except ValueError:
        return 0.0

def is_payment(desc_upper, coupon=""):
    if not coupon: coupon = ""
    kw_list = [
        "SU PAGO", "PAGO AUTOMATICO", "PAGO ELECTRONICO", "PAGO HOME", "PAGO LINK",
        "PAGO POR CAJA", "PAGO EN SUCURSAL", "PAGO MIS CUENTAS", "PAGO TARJETA",
        "PAGO DE RESUMEN", "PAGO BANELCO", "PAGO DE CAJA", "PAGO EN PESOS", "PAGO PESOS",
        "PAGO DOLARES", "PAGO EN DOLARES", "PAGO CAJERO", "PAGOS LINK"
    ]
    if any(kw in desc_upper for kw in kw_list):
        return True
    if desc_upper.strip() in ["PAGO", "PAGOS", "SU PAGO"]:
        return True
    if coupon in ["000000", "999999"]:
        return True
    return False

def add_months(year, month, delta):
    month += delta
    while month > 12:
        month -= 12
        year += 1
    return year, month

def process_visa(text):
    expenses = []
    lines = text.split('\n')
    current_titular = "Titular Principal"
    year_now = datetime.now().year
    month_now = int(datetime.now().strftime('%m'))
    
    dash = r"[-−—–]"
    # Visa Pattern: Day Coupon [Letter] Description [Installments] Amount
    # We require multiple spaces before the installment string to avoid matching part of the description
    pattern_compra = re.compile(r"^(?:\s*(\d{2}\s+[A-Za-z\.]+))?\s*(?P<day>\d{2})\s+(?P<coupon>\d{6})\s+(?P<desc>.+?)(?:\s{2,}(?P<inst>C\.\d{2}/\d{2}|\d{1,2}-\d{1,2}))?\s*(?:\(TNA.*?\))?\s+(?P<amount>" + dash + r"?[\d\.]+\,\d{2}\s*" + dash + r"?)\s*$")
    pattern_tax = re.compile(r"^(?:\s*(\d{2}\s+[A-Za-z\.]+))?\s*(?P<day>\d{2})\s+(?P<desc>(?:IMPUESTO|INTERESES|IIBB|IVA|DB\.RG|PERCEP|CARGO|REINTEGRO|DEVOLUCION|BONIF|DESCUENTO|CREDITO|REVERSO|AJUSTE).*?)\s+(?P<amount>" + dash + r"?[\d\.]+\,\d{2}\s*" + dash + r"?)\s*$")
    
    for line in lines:
        if "Total Consumos de " in line:
            name_part = line.split("Total Consumos de ")[1]
            current_titular = re.sub(r'\s+[-−—–]?\s*[\d\.]+\,\d{2}.*', '', name_part).strip()
            continue
            
        match_tax = pattern_tax.search(line)
        if match_tax:
            desc = match_tax.group('desc')
            desc = desc.replace("$", "").strip()
            amount_str = match_tax.group('amount')
            amount = parse_amount(amount_str)
            
            desc_upper = desc.upper()
            if amount > 0 and any(kw in desc_upper for kw in ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "]):
                amount = -amount

            if is_payment(desc_upper):
                continue

            if amount != 0:
                expenses.append({
                    "desc": desc,
                    "amount": amount,
                    "date": f"{year_now}-{month_now:02d}-01",
                    "monthKey": f"{year_now}-{month_now:02d}",
                    "installments": 1,
                    "card": "Visa",
                    "titular": current_titular, 
                    "is_tax": True
                })
            continue

        match_compra = pattern_compra.match(line)
        if match_compra:
            desc = match_compra.group('desc').strip()
            desc = re.sub(r'^[A-Z\*]\s+', '', desc)
            cuotas_str = match_compra.group('inst')
            amount_str = match_compra.group('amount')
            coupon = match_compra.group('coupon')
            amount = parse_amount(amount_str)
            
            desc_upper = desc.upper()
            if amount > 0 and any(kw in desc_upper for kw in ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "]):
                amount = -amount

            if is_payment(desc_upper, coupon):
                continue

            if amount == 0: continue
            
            current_inst = 1
            total_inst = 1
            is_installment = False
            
            if cuotas_str:
                clean_inst = cuotas_str.replace('C.', '')
                match_inst = re.search(r'(\d+)[/-](\d+)', clean_inst)
                if match_inst:
                    current_inst = int(match_inst.group(1))
                    total_inst = int(match_inst.group(2))
                    # Only project if there are multiple installments
                    if total_inst > 1:
                        is_installment = True

            if is_installment:
                remaining = total_inst - current_inst
                for i in range(remaining + 1):
                    y, m = add_months(year_now, month_now, i)
                    expenses.append({
                        "desc": desc,
                        "amount": amount,
                        "date": f"{year_now}-{month_now:02d}-01",
                        "monthKey": f"{y}-{m:02d}",
                        "installments": 1,
                        "card": "Visa",
                        "titular": current_titular,
                        "is_tax": False,
                        "installmentInfo": f"{current_inst + i}/{total_inst}"
                    })
            else:
                expenses.append({
                    "desc": desc,
                    "amount": amount,
                    "date": f"{year_now}-{month_now:02d}-01",
                    "monthKey": f"{year_now}-{month_now:02d}",
                    "installments": 1,
                    "card": "Visa",
                    "titular": current_titular,
                    "is_tax": False,
                    "installmentInfo": cuotas_str if cuotas_str else None
                })

    return expenses

def process_mastercard(text):
    expenses = []
    lines = text.split('\n')
    current_titular = "Titular Principal"
    year_now = datetime.now().year
    month_now = int(datetime.now().strftime('%m'))
    
    dash = r"[-−—–]"
    # Date Description [Installments] [Coupon] Amount
    # Using stricter spacing for installments
    pattern_compra = re.compile(r"^(?P<date>\d{2}-[A-Za-z]{3}-\d{2})\s+(?P<desc>.+?)(?:\s{2,}(?P<inst>\d{2}/\d{2}))?(?:\s+(?P<coupon>\d{4,6}))?\s+(?P<amount>" + dash + r"?[\d\.]+\,\d{2}\s*" + dash + r"?)\s*$")
    pattern_tax = re.compile(r"^\s*(?P<desc>(?:INTERESES|IMPUESTO|PERCEP\.|PERC\s|IVA|TRANSFER|SALDO PENDIENTE|REINTEGRO|DEVOLUCION|BONIF|DESCUENTO|CREDITO|REVERSO|AJUSTE).*?)\s+(?P<amount>" + dash + r"?[\d\.]*\,\d{2}\s*" + dash + r"?)(?:\s+[\d\.]*\,\d{2})?\s*$")
    
    for line in lines:
        match_tax = pattern_tax.match(line)
        if match_tax:
            desc = match_tax.group('desc').strip()
            amount_str = match_tax.group('amount')
            amount = parse_amount(amount_str)
            
            desc_upper = desc.upper()
            if amount > 0 and any(kw in desc_upper for kw in ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "]):
                amount = -amount

            if is_payment(desc_upper):
                continue

            if amount != 0:
                expenses.append({
                    "desc": desc,
                    "amount": amount,
                    "date": f"{year_now}-{month_now:02d}-01",
                    "monthKey": f"{year_now}-{month_now:02d}",
                    "installments": 1,
                    "card": "Mastercard",
                    "titular": current_titular,
                    "is_tax": True
                })
            continue

        match_compra = pattern_compra.match(line)
        if match_compra:
            desc = match_compra.group('desc').strip()
            cuotas_str = match_compra.group('inst')
            amount_str = match_compra.group('amount')
            coupon = match_compra.group('coupon')
            amount = parse_amount(amount_str)
            
            desc_upper = desc.upper()
            if amount > 0 and any(kw in desc_upper for kw in ["REINTEGRO", "DEVOLUCION", "ANULACION", "BONIF", "DESCUENTO", "CREDITO", "REVERSO", "AJUSTE", "SALDO A FAVOR", "DEV ", "REINT "]):
                amount = -amount

            if is_payment(desc_upper, coupon):
                continue

            if amount == 0: continue
            
            if 'PERSFLOW' in desc and cuotas_str:
                desc += " " + cuotas_str
                cuotas_str = None
            
            current_inst = 1
            total_inst = 1
            is_installment = False
            
            if cuotas_str:
                match_inst = re.search(r'(\d+)/(\d+)', cuotas_str)
                if match_inst:
                    current_inst = int(match_inst.group(1))
                    total_inst = int(match_inst.group(2))
                    if total_inst > 1:
                        is_installment = True

            if is_installment:
                remaining = total_inst - current_inst
                for i in range(remaining + 1):
                    y, m = add_months(year_now, month_now, i)
                    expenses.append({
                        "desc": desc,
                        "amount": amount,
                        "date": f"{year_now}-{month_now:02d}-01",
                        "monthKey": f"{y}-{m:02d}",
                        "installments": 1,
                        "card": "Mastercard",
                        "titular": current_titular,
                        "is_tax": False,
                        "installmentInfo": f"{current_inst + i}/{total_inst}"
                    })
            else:
                expenses.append({
                    "desc": desc,
                    "amount": amount,
                    "date": f"{year_now}-{month_now:02d}-01",
                    "monthKey": f"{year_now}-{month_now:02d}",
                    "installments": 1,
                    "card": "Mastercard",
                    "titular": current_titular,
                    "is_tax": False,
                    "installmentInfo": cuotas_str if cuotas_str else None
                })
            
    return expenses

def main():
    all_expenses = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            try:
                doc = fitz.open(filename)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                if 'VISA' in text.upper() or '1908' in filename:
                    expenses = process_visa(text)
                    all_expenses.extend(expenses)
                elif 'MASTERCARD' in text.upper() or '3760' in filename:
                    expenses = process_mastercard(text)
                    all_expenses.extend(expenses)
            except Exception as e:
                print(f"Error procesando {filename}: {e}")
                
    month_now_key = datetime.now().strftime('%Y-%m')
    total_visa = sum(e["amount"] for e in all_expenses if e["card"] == "Visa" and e["monthKey"] == month_now_key)
    total_master = sum(e["amount"] for e in all_expenses if e["card"] == "Mastercard" and e["monthKey"] == month_now_key)
    
    print(f"\n--- VERIFICACION DE TOTALES (MES ACTUAL) ---")
    print(f"Total Visa Extraido: ${total_visa:,.2f}")
    print(f"Total Mastercard Extraido: ${total_master:,.2f}")
    print(f"GRAN TOTAL: ${(total_visa + total_master):,.2f}\n")
                
    with open('nuevos_gastos.json', 'w', encoding='utf-8') as f:
        json.dump(all_expenses, f, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    main()
