#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # Universe
    u = set("abcdefghijklmnopqrstuvwxyz")

    # Set Data
    a = {"b", "f", "g", "m", "o"}
    b = {"b", "g", "h", "l", "u"}
    c = {"e", "f", "m"}
    d = {"e", "g", "l", "p", "q", "u", "v"}

    # Definition X
    x = b.union(a.intersection(c))
    print(f'X = {x}')

    # Inverses for a b and c
    ne_a = u.difference(a)
    ne_b = u.difference(b)
    ne_c = u.difference(c)

    # Definition Y
    y = (a.intersection(ne_b)).union(c.difference(b))
    print(f'Y = {y}')