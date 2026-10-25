import pdfplumber

def extract_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += (page.extract_text() or "") + "\n"
    return text

if __name__ == "__main__":
    t = extract_text("sample.pdf")
    print("Total characters:", len(t))
    print(t[:500])