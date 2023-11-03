#!/usr/bin/env python3
"""Generate forms for human evaluation."""

from jinja2 import FileSystemLoader, Environment

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("pair_comparison.html.jinja2")

    html = template.render(
        page_title="Encuesta | Proyecto INVERSO",
        form_url="http://localhost:8888",
        form_id=1,
        questions=[
            {
                "title": "Pregunta 1",
                "images": [
                    {"name": "A", "path": "imgs/test_1.png"},
                    {"name": "B", "path": "imgs/test_2.png"}
                ],
                "name": "q1"
            },
            {
                "title": "Pregunta 2",
                "images": [
                    {"name": "A", "path": "imgs/test_3.png"},
                    {"name": "B", "path": "imgs/test_4.png"}
                ],
                "name": "q2"
            },
        ]
    )
    print(html)


if __name__ == "__main__":
    main()
