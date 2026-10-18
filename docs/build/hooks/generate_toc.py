import html
import markdown
import posixpath
from urllib.parse import quote

from mkdocs.config import Config
from mkdocs.structure.files import File, Files, InclusionLevel
from mkdocs.structure.nav import Section, get_navigation
from mkdocs.structure.pages import Page


def _page_toc(page: Page) -> tuple[bool, str]:
    with open(page.file.abs_src_path, encoding="utf-8") as source:
        content = source.read()

    parser = markdown.Markdown(
        extensions=[
            "admonition",
            "attr_list",
            "fenced_code",
            "md_in_html",
            "meta",
            "tables",
            "toc",
            "pymdownx.highlight",
            "pymdownx.superfences",
            "pymdownx.arithmatex",
        ],
        extension_configs={"toc": {"toc_depth": "2-3"}},
    )
    parser.convert(content)

    pdf_values = parser.Meta.get("pdf", ["false"])
    is_pdf_page = bool(pdf_values) and pdf_values[0].strip().lower() == "true"
    if not is_pdf_page:
        return False, ""

    page_url = posixpath.relpath(page.file.url, "generated_site_toc/")
    page_url = quote(page_url, safe="/")
    toc = parser.toc.replace('href="#', f'href="{page_url}#')
    return True, toc


def _nav_to_html(items: list) -> tuple[str, int]:
    output = []
    included_pages = 0

    for item in items:
        if isinstance(item, Page):
            include, page_toc = _page_toc(item)
            if not include:
                continue

            title = item.title or item.file.src_path
            page_url = quote(
                posixpath.relpath(item.file.url, "generated_site_toc/"),
                safe="/",
            )
            output.append(
                f'<li><a href="{html.escape(page_url, quote=True)}">'
                f"{html.escape(title)}</a>{page_toc}</li>"
            )
            included_pages += 1
        elif isinstance(item, Section):
            children, child_pages = _nav_to_html(item.children)
            if child_pages:
                output.append(
                    f"<li>{html.escape(item.title or '')}{children}</li>"
                )
                included_pages += child_pages

    if not output:
        return "", 0

    return "<ul>\n" + "\n".join(output) + "\n</ul>", included_pages


def on_files(files: Files, config: Config) -> Files:
    nav = get_navigation(files, config)
    toc, included_pages = _nav_to_html(nav)
    if not included_pages:
        raise ValueError("Cannot generate the PDF table of contents: no PDF pages found.")

    content = f"---\npdf: true\n---\n\n# Contents\n\n{toc}\n"
    toc_file = File.generated(
        config,
        "generated_site_toc.md",
        content=content,
        inclusion=InclusionLevel.INCLUDED,
    )
    files.append(toc_file)
    config.nav.insert(0, {"": "generated_site_toc.md"})
    return files
