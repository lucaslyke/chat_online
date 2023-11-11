#pip install pypdf

from pypdf import PdfReader

pdf = PdfReader('livro.pdf')

pag_conteudo = {}

for indx, pdf_page in enumerate(pdf.pages):
    pag_conteudo[indx + 1] = pdf_page.extract_text()

print(pag_conteudo)
