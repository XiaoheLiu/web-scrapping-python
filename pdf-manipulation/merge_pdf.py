from PyPDF2 import PdfFileReader, PdfFileMerger


def merge_pdf(paths, output):
    merger = PdfFileMerger()

    for path in paths:
        merger.append(PdfFileReader(path))

    merger.write(output)


if __name__ == '__main__':
    paths = ['doc1.pdf', 'doc2.pdf']
    merge_pdf(paths, output='merged.pdf')
