def main():
    triplet = findPythagoreanTriplet(1000)
    print(triplet[0] * triplet[1] * triplet[2])

def findPythagoreanTriplet(target_sum):
    for a in range(1, target_sum // 3):
        for b in range(a + 1, target_sum // 2):
            c = target_sum - a - b
            if c <= b:
                continue
            if a ** 2 + b ** 2 == c ** 2:
                return (a, b, c)
    return None

if __name__ == "__main__":
    main()
