import pymupdf


def extract_text_from_pdf(file_path: str) -> str:
    document = pymupdf.open(file_path)

    try:
        pages = []

        for page in document:
            text = page.get_text()
            if text:
                pages.append(text)

        return "/n".join(pages).strip()
    finally:
        document.close()
