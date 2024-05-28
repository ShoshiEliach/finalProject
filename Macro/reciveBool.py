import sys

boolean_values=[False,False,False,False]
def main():
    boolean_values = [line.strip() == 'True' for line in sys.stdin]

    print("Received boolean values:", boolean_values)

if __name__ == "__main__":
    main()
