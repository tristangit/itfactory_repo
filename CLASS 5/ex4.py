def val_max(l):
    v_max = l[0]
    for i in range(len(l)):
        if l[i] > v_max:
            v_max = l[i]
    print(v_max)
    return v_max


l = [4, 5, -5, 0, 9, 15, 19, -21]
val_max(l)