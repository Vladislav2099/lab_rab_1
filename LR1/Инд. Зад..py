# -*- coding: utf-8 -*-

if __name__ == "__main__":
    # Определим универсальное множество
    u = set("abcdefghijklmnopqrstuvwxyz")

    a = {"c", "e", "h", "n"}
    b = {"e", "f", "k", "n", "x"}
    c = {"o", "p", "w"}
    d = {"b", "e", "g"}
    x = (a.difference(b)).difference(c.union(d))
    print(f"x = {x}")

    # Найдем дополнения множеств
    dn = u.difference(d)
    cn = u.difference(c)

    y = (a.intersection(dn)).union(cn.difference(dn))
    print(f"y = {y}")
