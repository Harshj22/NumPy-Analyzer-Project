import numpy as np

class DataAnalytics:
    def __init__(self):
        self.array = None

    def create_array(self):
        print("Select the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            size = int(input("Enter number of elements: "))
            elements = list(map(int, input(f"Enter {size} elements: ").split()))
            self.array = np.array(elements)

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            total = rows * cols
            elements = list(map(int, input(f"Enter {total} elements: ").split()))
            self.array = np.array(elements).reshape(rows, cols)

        elif choice == 3:
            x = int(input("Enter dimension 1 size: "))
            y = int(input("Enter dimension 2 size: "))
            z = int(input("Enter dimension 3 size: "))
            total = x * y * z
            elements = list(map(int, input(f"Enter {total} elements: ").split()))
            self.array = np.array(elements).reshape(x, y, z)

        print("\nArray created successfully:")
        print(self.array)

    def indexing_slicing(self):
        print("Choose an option:")
        print("1. Indexing")
        print("2. Slicing")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            if self.array.ndim == 1:
                idx = int(input("Enter index (0-based): "))
                print("Indexed value:", self.array[idx])
            elif self.array.ndim == 2:
                i = int(input("Enter row index: "))
                j = int(input("Enter column index: "))
                print("Indexed value:", self.array[i][j])
            else:
                i = int(input("Enter i index: "))
                j = int(input("Enter j index: "))
                k = int(input("Enter k index: "))
                print("Indexed value:", self.array[i][j][k])

        elif ch == 2:
            if self.array.ndim == 1:
                r = input("Enter range start:end (e.g. 0:3): ")
                s, e = map(int, r.split(':'))
                print("Sliced Array:")
                print(self.array[s:e])
            elif self.array.ndim == 2:
                r = input("Enter the row range (start:end): ")
                c = input("Enter the column range (start:end): ")
                r1, r2 = map(int, r.split(':'))
                c1, c2 = map(int, c.split(':'))
                print("Sliced Array:")
                print(self.array[r1:r2, c1:c2])
            else:
                ri = input("Enter i range (start:end): ")
                rj = input("Enter j range (start:end): ")
                rk = input("Enter k range (start:end): ")
                i1, i2 = map(int, ri.split(':'))
                j1, j2 = map(int, rj.split(':'))
                k1, k2 = map(int, rk.split(':'))
                print("Sliced Array:")
                print(self.array[i1:i2, j1:j2, k1:k2])

    def math_operations(self):
        print("Choose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        ch = int(input("Enter your choice: "))
        size = self.array.size
        elements = list(map(int, input(f"Enter {size} elements separated by space: ").split()))
        second = np.array(elements).reshape(self.array.shape)

        print("Original Array:")
        print(self.array)
        print("Second Array:")
        print(second)

        if ch == 1:
            print("Result of Addition:")
            print(self.array + second)
        elif ch == 2:
            print("Result of Subtraction:")
            print(self.array - second)
        elif ch == 3:
            print("Result of Multiplication:")
            print(self.array * second)
        elif ch == 4:
            print("Result of Division:")
            print(self.array / second)

    def combine_split(self):
        print("Choose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            size = self.array.size
            elements = list(map(int, input(f"Enter {size} elements to combine: ").split()))
            second = np.array(elements).reshape(self.array.shape)
            combined = np.vstack((self.array, second))
            print("Combined Array (Vertical Stack):")
            print(combined)

        elif ch == 2:
            parts = int(input("Enter number of parts to split into: "))
            result = np.split(self.array, parts)
            print("Split Result:")
            for part in result:
                print(part)

    def search_sort_filter(self):
        print("Choose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            val = int(input("Enter value to search: "))
            result = np.where(self.array == val)
            print("Found at positions:", result)

        elif ch == 2:
            print("Original Array:")
            print(self.array)
            sorted_arr = np.sort(self.array)
            print("Sorted Array:")
            print(sorted_arr)

        elif ch == 3:
            cond = int(input("Filter values greater than: "))
            filtered = self.array[self.array > cond]
            print("Filtered Array:")
            print(filtered)

    def aggregates_statistics(self):
        print("Choose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Min")
        print("7. Max")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("Sum:", np.sum(self.array))
        elif ch == 2:
            print("Mean:", np.mean(self.array))
        elif ch == 3:
            print("Median:", np.median(self.array))
        elif ch == 4:
            print("Standard Deviation:", np.std(self.array))
        elif ch == 5:
            print("Variance:", np.var(self.array))
        elif ch == 6:
            print("Minimum:", np.min(self.array))
        elif ch == 7:
            print("Maximum:", np.max(self.array))

def main():
    d = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    while True:
        print("\n======Choose an option:======")
        print("1. Create a Numpy Array")
        print("2. Index / Slice Array")
        print("3. Perform Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort, or Filter Arrays")
        print("6. Compute Aggregates and Statistics")
        print("7. Exit")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            d.create_array()
        elif ch == 2:
            d.indexing_slicing()
        elif ch == 3:
            d.math_operations()
        elif ch == 4:
            d.combine_split()
        elif ch == 5:
            d.search_sort_filter()
        elif ch == 6:
            d.aggregates_statistics()
        elif ch == 7:
            print("Thank you for using the NumPy Analyzer! Goodbye!")
            break

if __name__ == "__main__":
    main()

