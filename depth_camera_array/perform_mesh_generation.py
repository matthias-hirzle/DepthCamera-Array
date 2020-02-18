import argparse


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser('Performes a mesh generation to the given coordinates')
    parser.add_argument('--coordinates', type=str, help='Path to file containing coordinates')  # TODO how does it look like
    parser.add_argument('--output', type=str, help='Path to output file')
    return parser.parse_args()


def main():
    args = parse_args()


if __name__ == '__main__':
    main()