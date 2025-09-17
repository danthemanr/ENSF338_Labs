

def main():
    with open('lab_data/pg2701.txt', 'r', encoding='utf-8') as file:
        file_list = [line for line in file]
    i = 0
    while file_list[i] != "CHAPTER 1. Loomings.\n": i += 1
    print("The value of i should be 41-1:", i)

    while i < len(file_list):
        pass
        

if __name__ == "__main__":
    main()