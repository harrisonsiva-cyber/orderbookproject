import argparse # Importing argparse to use the argparse module (built-in library for parsing command-line arguments)
from cli.commands import greet # From commands.py importing the greet function

# Define the main function for the CLI scaffold
def main():
    parser = argparse.ArgumentParser(description="My CLI App")  # Creating the main argument parser with a description
    subparsers = parser.add_subparsers(dest="command") # 'dest="command" - chosen subcommand name will be stored in args.command

    greet_parser = subparsers.add_parser("greet", help="Greet a user") # Adding the 'greet' subcommand to the subparsers
    greet_parser.add_argument("--name", required=True, help="Name of the person to greet")

    args = parser.parse_args()

    if args.command == "greet":
        greet(args.name)
    else:
        parser.print_help() # If no command was provided, then show help

# Only run the main function when the script is executed correctly.
if __name__ == "__main__":
    main()

