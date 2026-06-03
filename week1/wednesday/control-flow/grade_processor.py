def main(score):
    highest = score[0]
    lowest = highest
    avg = 0
    total = 0
    valid_size = 0
    distribution = {
        "A":0,
        "B":0,
        "C":0,
        "D":0,
        "F":0
    }

    for i in score:
        if i == -999:
            break
        if i < 0:
            continue
        elif i >= 90:
            print(f"score {i} --> grade A") 
            distribution["A"] += 1 
        elif i >= 80:
            print(f"score {i} --> grade B") 
            distribution["B"] += 1
        elif i >= 70:
            print(f"score {i} --> grade C") 
            distribution["C"] += 1
        elif i >= 60:
            print(f"score {i} --> grade D") 
            distribution["D"] += 1
        else:
            print(f"score {i} --> grade F") 
            distribution["F"] += 1
       
        if i > highest:
            highest = i
        if i < lowest:
            lowest = i
        valid_size += 1
        total += i
        avg = total/valid_size
    print("="*30)
    print(f"Highest score: {highest}")
    print("="*30)
    print(f"Lowest score: {lowest}")
    print("="*30)
    print(f"Average score: {avg}")
    print("="*30)
    print(f"Distribution of scores:\nA:{distribution['A']}\nB:{distribution['B']}\nC:{distribution['C']}\nD:{distribution['D']}\nF:{distribution['F']}")
    print("="*30)


if __name__ == "__main__":
    main([88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85])
