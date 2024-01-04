import os
from common import common_methods


def main():
    input_a = os.getenv('A')
    input_b = os.getenv('B')
    add = common_methods.addition_of_two_variables(input_a, input_b)
    print(f"addition of {input_a} and {input_b} is: {add} ")
    with open(os.getenv("GITHUB_OUTPUT"), 'a') as fp:
        fp.write("sum={}".format(add))


if __name__ == "__main__":
    main()

