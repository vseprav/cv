import argparse
import os

from app.cv_generator import CVGenerator
from app.html_to_markdown import html_to_markdown
from app.markdown_to_text import markdown_to_text


def save_cv(cv, output_file):
    with open(output_file, "w") as f:
        f.write(cv)


def generate_short_cv(md_file_path):
    content = markdown_to_text(md_file_path)
    return content

def main():
    parser = argparse.ArgumentParser(description="Generate a CV from a Markdown file")
    parser.add_argument("md_file", help="Path to the Markdown file to convert to a CV")
    args = parser.parse_args()

    if not os.path.exists(args.md_file):
        print(f"Error: File {args.md_file} not found.")
        exit(1)

    cv = generate_short_cv(args.md_file)
    l_chain = CVGenerator()
    short_cv = l_chain.generate_cv(cv)
    md_file = html_to_markdown(short_cv)
    save_cv(md_file, "short_cv.md")
    print("CV generated successfully and saved to short_cv.md")

if __name__ == "__main__":
    main()
