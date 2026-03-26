import os
import shutil

from markdown.extract_title import extract_title
from markdown.markdown import markdown_to_html_node


def main():
    copy_files_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")


def copy_files_recursive(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    os.mkdir(dest_dir)

    for item in os.listdir(source_dir):
        from_path = os.path.join(source_dir, item)
        to_path = os.path.join(dest_dir, item)

        if os.path.isfile(from_path):
            shutil.copy(from_path, to_path)
        else:
            copy_files_recursive(from_path, to_path)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    for item in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)

        if os.path.isfile(from_path):
            if from_path.endswith(".md"):
                # Mengubah ekstensi .md menjadi .html untuk file tujuan
                dest_path = dest_path.replace(".md", ".html")
                generate_page(from_path, template_path, dest_path)
        else:
            # Jika item adalah direktori, buat direktori tujuan dan panggil rekursif
            if not os.path.exists(dest_path):
                os.makedirs(dest_path, exist_ok=True)
            generate_pages_recursive(from_path, template_path, dest_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as f:
        content_from = f.read()
    with open(template_path, "r") as f:
        content_template = f.read()

    node = markdown_to_html_node(content_from)
    html = node.to_html()
    title = extract_title(content_from)

    # Ganti placeholder di template dengan konten yang sudah diparsing
    content_template = content_template.replace("{{ Title }}", title)
    content_template = content_template.replace("{{ Content }}", html)

    # Pastikan direktori tujuan ada sebelum menulis file
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "" and not os.path.exists(dest_dir):
        os.makedirs(dest_dir, exist_ok=True)

    with open(dest_path, "w") as file:
        file.write(content_template)


if __name__ == "__main__":
    main()
