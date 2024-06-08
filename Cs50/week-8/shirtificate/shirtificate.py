import fpdf

class Shirtificate(fpdf.FPDF):
    def __init__(self):
        super().__init__(orientation='P', unit='mm', format='A4')

    def header(self):
        self.set_font('Helvetica', '', 24)
        self.cell(0, 15, 'CS50 Shirtificate', 0, 1, 'C')

    def generate_shirtificate(self, name):
        self.add_page()
        self.header()
        self.image('shirtificate.png', x=105, y=50, w=0, h=100)
        self.set_font('Helvetica', '', 24)
        self.set_text_color(255)
        self.cell(0, 70, name, 0, 1, 'C')

if __name__ == '__main__':
    name = input("Enter your name: ")
    shirtificate = Shirtificate()
    shirtificate.generate_shirtificate(name)
    shirtificate.output('shirtificate.pdf')
