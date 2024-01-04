import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))) 
sys.path.append(os.path.dirname(__file__))
from common import common_methods


def main():
    input_a = int(os.getenv('A'))
    input_b = int(os.getenv('B'))
    add = common_methods.addition_of_two_variables(input_a, input_b)
    print(f"addition of {input_a} and {input_b} is: {add} ")
    with open(os.getenv("GITHUB_OUTPUT"), 'a') as fp:
        fp.write("sum={}".format(add))


if __name__ == "__main__":
    main()

