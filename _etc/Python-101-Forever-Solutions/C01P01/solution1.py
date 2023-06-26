def iban_formatter(iban):
    raw_iban = iban.replace(" ", "")
    arr_iban = []
    tmp_iban = ""
    for i in raw_iban:
        tmp_iban += i
        if len(tmp_iban) == 4: 
            arr_iban.append(tmp_iban)
            tmp_iban = ""
        elif len(arr_iban) >= 5 and len(tmp_iban) == 2:
            arr_iban.append(tmp_iban) 
    return " ".join(arr_iban)     


print(iban_formatter("BG80      BNBG 9661 1020 3456 78    ") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG80BNBG96611020345678") == "BG80 BNBG 9661 1020 3456 78")
print(iban_formatter("BG91UNCR70001864961754") == "BG91 UNCR 7000 1864 9617 54")
print(iban_formatter("BG14TTBB94005362446381") =="BG14 TTBB 9400 5362 4463 81")
 
