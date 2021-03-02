while True:
    fraction = list(map(float, input().split()))
    if fraction == [0.0, 0.0]:
        break
    else:
        whole = int(fraction[0] / fraction[1])
        remainder = int(fraction[0] - fraction[1] * whole)
        print("\n", whole, remainder, "/", int(fraction[1]))
