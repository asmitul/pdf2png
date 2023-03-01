# pip install pdf2image
# poppler


from pdf2image import convert_from_path
from pathlib import Path


def main() -> None:
    BASE_DIR = Path.cwd()
    print(BASE_DIR)
    pdf_file = f"{BASE_DIR}\sample_1-39.pdf"
    print(pdf_file)
    images = convert_from_path(pdf_file)

    for i in range(len(images)):

        # Save pages as images in the pdf
        images[i].save('sample_1-39-' + str(i) + '.png', 'PNG')


if __name__ == "__main__":
    main()
