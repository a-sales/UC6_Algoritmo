def test(a, b):
    if a.isdigit():
        c = a + b
        print(f"a {a} - b {b} = c {c}")
    else:
        print("Erro")

test(5,3)