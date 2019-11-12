msg = "('UserError', ('El campo  de  es obligatorio.', ''))"
print(type(msg))
ts = eval(msg)
print(type(ts))
print(ts[0])
print(ts[1][0])