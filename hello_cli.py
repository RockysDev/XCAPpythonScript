import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple Python CLI script.")
    parser.add_argument("--name", type=str, help="Your name")
    args = parser.parse_args()

    if args.name:
        print(f"Hello, {args.name}!")
    else:
        print("Hello, world!")

if __name__ == "__main__":
       main()