import html2text


def html_to_markdown(html_content):
    """
    Converts HTML content to markdown format.
    """
    markdown_content = html2text.html2text(html_content)
    return markdown_content
