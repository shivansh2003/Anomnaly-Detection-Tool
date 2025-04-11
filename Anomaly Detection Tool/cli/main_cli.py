# --------------------------- cli/main_cli.py ---------------------------
import argparse
from controller import run_tool
from utils.logger import log_info
log_info("Inside CLI main() function")


def main():
    parser = argparse.ArgumentParser(description='Network Traffic Analyzer Tool')
    parser.add_argument('--interface', type=str, help='Network interface to capture traffic on')
    parser.add_argument('--duration', type=int, help='Duration of capture in seconds', default=60)
    args = parser.parse_args()
    run_tool(args.interface, args.duration)

if __name__ == '__main__':
    main()