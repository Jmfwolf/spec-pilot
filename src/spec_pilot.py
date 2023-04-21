import argparse
from generator import generator
from spec_parser import spec_parser
from validator import aws_validator

def main():
    parser = argparse.ArgumentParser(description='Generate and validate AWS API Gateway specifications.')
    parser.add_argument('command', choices=['generate', 'validate'], help='command to run')
    parser.add_argument('--input', '-i', required=True, help='input file path')
    parser.add_argument('--output', '-o', required=True, help='output file path')
    parser.add_argument('--region', '-r', help='AWS region')
    args = parser.parse_args()

    if args.command == 'generate':
        spec_parser.parse(args.input)
        generator.generate(args.output)
    elif args.command == 'validate':
        aws_validator.validate(args.input, args.region)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
