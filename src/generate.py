import re
from pathlib import Path

from markdown_blocks import markdown_to_html_node


def extract_title(markdown: str) -> str:
    title = re.search(r"# .*", markdown)
    if title:
        return title.group().lstrip("# ")
    else:
        raise Exception("could not find title")  # noqa: TRY002

def generate_page(source, template, dest, basepath):
    print(f"Generating page from {source} to {dest} using {template}")
    with open(source, "r") as s:
        markdown = s.read()
    with open(template, "r") as t:
        html_template = t.read()
    html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    html_template = html_template.replace(r"{{ Title }}", title)
    html_template =  html_template.replace(r"{{ Content }}", html)
    html_template =  html_template.replace(r'href="/', f'href="{basepath}')
    html_template =  html_template.replace(r'src="/', f'src="{basepath}')
    Path(dest).parent.mkdir(parents=True, exist_ok=True)
    with open(dest, "w") as d:
        d.write(html_template)

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    files = Path(dir_path_content).rglob("*.md")
    for f in files:
        dest_path = Path(dest_dir_path).joinpath(Path(*f.parts[1:-1]), "index.html")
        generate_page(f, template_path, dest_path, basepath)