def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    am = len(a)
    an = len(a[0])
    bm = len(b)
    bn = len(b[0])
    if an != bm:
        return -1
    rows = []
    for i in range(am):
        row = []
        for j in range(bn):
            item = sum([a[i][x] * b[x][j] for x in range(an)])
            row.append(item)
        rows.append(row)
    return rows
