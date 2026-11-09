import sys
from pathlib import Path

from generate import generate_page_recursive


def clean_public():
    docs = Path("docs")
    docs.mkdir(exist_ok=True)
    public = list(docs.rglob("*"))
    for i in reversed(public):
        print(f"Deleting: {i}")
        if Path.is_file(i):
            Path.unlink(i)
        else:
            Path.rmdir(i)
    check = list(docs.rglob("*"))
    if len(check) > 0:
        clean_public()
    else:
        print("public clean")

def copy_static():
    static = Path("static/")
    for f in static.glob("*"):
        f.copy_into(Path("docs"))
        print(f"Copying {f.as_posix()}")



def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    print(basepath)
    clean_public()
    copy_static()
    generate_page_recursive("content", "template.html", "docs", basepath)
main()