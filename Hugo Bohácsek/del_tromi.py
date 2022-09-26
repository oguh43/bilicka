for i in range (100, 1000):
    if i % 3 == 0 and int(list(str(i))[-1]) + int(list(str(i))[-2]) < 10:
        print(f"Číselko {i} spĺňa tieto podmienky.")