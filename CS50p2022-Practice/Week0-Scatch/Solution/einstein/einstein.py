
def main():
    """Let's convert matter to energy!"""
    mass = input("Enter a mass in kilograms: ").strip()
    print(convert(int(mass)))

def convert(mass):
    """Convert kilograms to joules"""
    joules = mass * (300000000**2)
    return joules

if __name__ == "__main__":
    main()