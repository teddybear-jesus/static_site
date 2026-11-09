from pathlib import Path


def clean_public():
    public = list(Path("public").rglob("*"))
    for i in reversed(public):
        print(f"Deleting: {i}")
        if Path.is_file(i):
            Path.unlink(i)
        else:
            Path.rmdir(i)
    check = list(Path("public").rglob("*"))
    if len(check) > 0:
        clean_public()
    else:
        print("public clean")

def copy_static():
    static = Path("static/")
    for f in static.glob("*"):
        f.copy_into(Path("public"))
        print(f"Copying {f.as_posix()}")



def main():
    clean_public()
    copy_static()
main()