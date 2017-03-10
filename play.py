from audio import Audio


def main():
    with Audio() as audio:
        for x in raw_input():
            audio.play((ord(x) - ord('A') + 1) * 50, 0.3)


if __name__ == "__main__":
    main()
