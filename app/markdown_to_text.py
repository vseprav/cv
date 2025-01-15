import markdown

def markdown_to_text(md_file_path):
    """
    Converts a markdown file to HTML (plain text).
    """
    with open(md_file_path, 'r') as file:
        md_content = file.read()
    html_content = markdown.markdown(md_content)
    return html_content
