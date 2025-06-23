"""
Build a small command-line app to track quiz scores,
stored in a CSV file.

"""



import csv
import os

def load_scores(path: str) -> list[tuple[str, int]]:
    scores = []
    if not os.path.exists(path):
        return scores
    try:
        with open(path, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) != 2:
                    continue
                name, score = row
                scores.append((name, int(score)))
    except Exception as e:
        print(f"Error loading scores: {e}")
    return scores

def add_score(records: list[tuple[str, int]], name: str, score: int) -> None:
    records.append((name, score))

def save_scores(path: str, records: list[tuple[str, int]]) -> None:
    try:
        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)
            for name, score in records:
                writer.writerow([name, score])
    except Exception as e:
        print(f"Error saving scores: {e}")

def top_n(records: list[tuple[str, int]], n: int) -> list[tuple[str, int]]:
    return sorted(records, key=lambda x: x[1], reverse=True)[:n]

def menu():
    path = 'scores.csv'
    records = load_scores(path)

    while True:
        print("\nMenu:\n1. Top N Scores\n2. Add New PLayer with score\n3. Exit")
        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                n = int(input("Enter N: "))
                top_scores = top_n(records, n)
                for name, score in top_scores:
                    print(f"{name}: {score}")
            elif choice == 2:
                name = input("Enter name: ")
                try:
                    score = int(input("Enter score: "))
                    add_score(records, name, score)
                    save_scores(path, records)
                except ValueError:
                    print("Invalid score. Please enter a number.")
            elif choice == 3:
                print("See You Again!")
                break
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    menu()
