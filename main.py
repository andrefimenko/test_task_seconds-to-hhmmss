a = 49873751

def res(a):
    s = a % 60
    if s < 10:
        s = f"0{s}"
    m = a // 60 % 60
    if m < 10:
        m = f"0{m}"
    h = a // 60 // 60
    if h < 10:
        h = f"0{h}"
    return f"{h}:{m}:{s}"

print(res(a))