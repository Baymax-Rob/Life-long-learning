import re


def main():
    """Convert embedded YouTube HTML to short, shareable URLS."""
    print(parse(input("HTML: ").strip()))


def parse(s):
    """Extract a YouTube URL from a given string of embedded HTML."""
    try:
        url = re.search('(?<=embed\/).*?(?=")', s)
        return "https://youtu.be/" + url.group(0)
    except Exception:
        return None


if __name__ == "__main__":
    main()
