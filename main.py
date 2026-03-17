import argparse
from converter import converter

parser = argparse.ArgumentParser(
    description="A tool to convert MyBible modules on Android to Zefania"
)
parser.add_argument("--biblename", required=True, help="The name of the Bible Version.")
parser.add_argument(
    "--source", required=True, help="The path to the MyBible file/database."
)
parser.add_argument(
    "--output", required=True, help="The path to the output Zefania file to generate."
)

args = parser.parse_args()


converter(args.biblename, args.source, args.output)
