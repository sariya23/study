import PyPDF2
import random
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import string


class PDFHelper:
    def extract_text_from_page(self, file_path, page):
        with open(file_path, 'rb') as f:
            pdf_file_obj = PyPDF2.PdfReader(f)
            try:
                page_object = pdf_file_obj.pages[page]
                return page_object.extract_text()
            except IndexError:
                raise IndexError('Страницы с таким номером нет')

    def add_encryption(self, input_pdf, output_pdf, password):
        pdf_writer = PyPDF2.PdfWriter()
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

        pdf_writer.encrypt(user_password=password, owner_pwd=None,
                           use_128bit=True)

        with open(output_pdf, 'wb') as fh:
            pdf_writer.write(fh)

    def PDF_merge(self, pdfs: list[str], output: str):
        """
        :param pdfs: Список с путями до pdf файлов
        :param output: Название результирующего файла
        """
        pdf_merger = PyPDF2.PdfMerger()
        for pdf in pdfs:
            pdf_merger.append(pdf)
            with open(output, 'wb') as f:
                pdf_merger.write(f)

    def generate_random_text(self, length):
        return ''.join(random.choice(string.ascii_letters + string.digits + ' ') for _ in range(length))

    def create_pdf_file(self, file_name, text):
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter
        c.drawString(100, height - 100, text)
        c.showPage()
        c.save()

    def c(self, n):
        for i in range(1, n + 1):
            file_name = f"file_{i}.pdf"
            random_text = self.generate_random_text(500)  # Замените 500 на желаемую длину текста
            self.create_pdf_file(file_name, random_text)
            print(f"Создан файл {file_name}")


if __name__ == '__main__':
    p = PDFHelper()
    print(p.extract_text_from_page('frst.pdf', 0))
    p.add_encryption('frst.pdf', 'encrupt_pdf.pdf', '123')
    p.PDF_merge(['frst.pdf', 'scnd.pdf'], 'result.pdf')
    p.c(2)
