import argparse
import sys

from src.generator import generate
from src.spec_parser import parse_spec
from src.validator import validate


def main(args=None):
    """
    The main entry point for the spec_pilot program. This function can be used as a library or as a pip install.

    :param args: The list of arguments passed to the command line.
    """
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser(description="spec_pilot - A tool for parsing and generating API documentation.")
    parser.add_argument("input_file", help="The path to the input OpenAPI specification file.")
    parser.add_argument("output_dir", help="The path to the output directory where the generated documentation will be saved.")
    parser.add_argument("--validate", action="store_true", help="Validate the input OpenAPI specification file.")
    parser.add_argument("--version", action="version", version="spec_pilot 1.0.0")

    args = parser.parse_args(args)

    # Validate the input OpenAPI specification file
    if args.validate:
        validation_errors = validate(args.input_file)
        if validation_errors:
            print("Validation errors found:")
            for error in validation_errors:
                print(f"- {error}")
            sys.exit(1)

    # Parse the input OpenAPI specification file
    parsed_spec = parse_spec(args.input_file)

    # Generate the API documentation
    generate(parsed_spec, args.output_dir)

    print("API documentation generated successfully!")


if __name__ == "__main__":
    main()