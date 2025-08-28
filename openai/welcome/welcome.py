import os

from dotenv import load_dotenv

load_dotenv()
print("hello world")

def main():
    print("This is the main function.")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()
