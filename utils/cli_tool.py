
import sys

def cli(args):
    """Simulate a basic command-line interface tool."""
    if len(args) < 2:
        print("Usage: cli_tool <command>")
        return
    print(f"Executing command: {args[1]}")

if __name__ == "__main__":
    cli(sys.argv)
