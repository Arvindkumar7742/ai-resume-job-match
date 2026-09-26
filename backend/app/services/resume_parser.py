import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    print("file_path-->>", file_path)
    document = pymupdf.open(file_path)

    print(document)
    try:
        pages = []

        for page in document:
            text = page.get_text()
            if text:
                pages.append(text)

        return "/n".join(pages).strip()
    finally:
        document.close()
