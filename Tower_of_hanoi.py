def hanoi(n, src, dest, aux):
    if n == 1:
        print("Move disk 1 from", src, "to", dest)
        return
    hanoi(n-1, src, aux, dest)
    print("Move disk", n, "from", src, "to", dest)
    hanoi(n-1, aux, dest, src)
hanoi(3, 'A', 'C', 'B')
