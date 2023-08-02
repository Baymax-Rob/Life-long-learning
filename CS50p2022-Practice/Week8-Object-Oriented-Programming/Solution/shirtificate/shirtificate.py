from fpdf import FPDF


class Shirt:
    """Creates an instance of the "I took CS50" t-shirt."""

    def __init__(self, name):
        """"""
        self.name = name
        self.tailor()

    @classmethod
    def get(cls):
        """Called to instantiate the student's shirtificate.
        Asks for user input in the form of a full name."""
        name = input("Full name: ").strip()
        return cls(name)

    def tailor(self):
        """Create a PDF with the current instance's details applied."""
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_auto_page_break(auto=False, margin=0)

        # Set font and add the text at the top of the page
        pdf.set_font("helvetica", "B", size=46)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(0, 50, border=0, align="C", txt="CS50 Shirtificate")
        pdf.ln()

        # Add and center shirt image
        pdf.image(
            "shirtificate.png",
            x=15,
            y=(297 / 4),
            w=180,
            alt_text=f"A Harvard shirt with the words: {self.name} took CS50",
        )

        # Set font and add the text on top of the shirt
        pdf.set_font("helvetica", "B", size=28)
        pdf.set_text_color(255, 255, 255)
        pdf.cell(0, 150, border=0, align="C", txt=f"{self.name} took CS50")

        # Save the the image as a PDF
        pdf.output("shirtificate.pdf")


def main():
    """"""
    Shirt.get()


if __name__ == "__main__":
    main()
