a= input()
if a>='B' and a<='Z':
  print(chr(ord(a.lower()) - 1))
if a <='A' or a>'Z':
  print("khong ton tai")
