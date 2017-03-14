import sys

from audio import Audio
from singleread import singleread


def main():
    with Audio() as audio:
        for x in singleread() if "-u" in sys.argv else raw_input():
            audio.play((ord(x) - ord('A') + 1) * 50, 0.3)


if __name__ == "__main__":
    main()
