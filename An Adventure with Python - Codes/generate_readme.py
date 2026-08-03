from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parent
README_FILE = ROOT / "README.md"
SCRIPT_NAME = Path(__file__).name

BOOK_TITLE = "An Adventure with Python"
BOOK_DESCRIPTION = (
    f"A journey-based collection of Python exercises and real-world examples — directly from the book “{BOOK_TITLE}”."
)

IGNORED_DIRECTORIES = {
    ".git",
    ".github",
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".venv",
    "venv",
    "env",
}

IGNORED_FILES = {
    README_FILE.name,
    SCRIPT_NAME,
}


def natural_key(value: str) -> list[int | str]:
    """Sort names naturally: S02 before S10."""
    return [
        int(part) if part.isdigit() else part.casefold()
        for part in re.split(r"(\d+)", value)
    ]


def should_ignore(path: Path) -> bool:
    relative_path = path.relative_to(ROOT)

    return (
        path.name in IGNORED_FILES
        or any(part in IGNORED_DIRECTORIES for part in relative_path.parts)
        or any(part.startswith(".") for part in relative_path.parts)
    )


def python_files(directory: Path) -> list[Path]:
    files = [
        path
        for path in directory.iterdir()
        if (
            path.is_file()
            and path.suffix.lower() == ".py"
            and not should_ignore(path)
        )
    ]

    return sorted(files, key=lambda path: natural_key(path.name))


def directories(directory: Path) -> list[Path]:
    folders = [
        path
        for path in directory.iterdir()
        if path.is_dir() and not should_ignore(path)
    ]

    return sorted(folders, key=lambda path: natural_key(path.name))


def contains_python_files(directory: Path) -> bool:
    return any(
        path.is_file()
        and path.suffix.lower() == ".py"
        and not should_ignore(path)
        for path in directory.rglob("*")
    )


def format_directory_name(name: str) -> str:
    """
    Convert directory names into readable titles.

    S04              -> Chapter 4
    P03              -> Part 3
    S04.5-SHADOW-LIB -> Chapter 4 — Shadow Library Exercises
    """

    shadow_match = re.fullmatch(
        r"S(\d+)\.5-SHADOW-LIB",
        name,
        flags=re.IGNORECASE,
    )

    chapter_match = re.fullmatch(
        r"S(\d+)",
        name,
        flags=re.IGNORECASE,
    )

    part_match = re.fullmatch(
        r"P(\d+)",
        name,
        flags=re.IGNORECASE,
    )

    if shadow_match:
        chapter_number = int(shadow_match.group(1))
        return f"Chapter {chapter_number} — Shadow Library Exercises"

    if chapter_match:
        chapter_number = int(chapter_match.group(1))
        return f"Chapter {chapter_number}"

    if part_match:
        part_number = int(part_match.group(1))
        return f"Part {part_number}"

    return name.replace("-", " ").replace("_", " ").title()


def format_file_name(name: str) -> str:
    """
    Convert a Python filename into a readable exercise title.

    1.score_record_indexing.py
    -> 1. Score Record Indexing
    """

    stem = Path(name).stem
    match = re.match(r"^(\d+)[._-]*(.*)$", stem)

    if match:
        number, title = match.groups()
        title = re.sub(r"[_-]+", " ", title).strip()

        if title:
            return f"{number}. {title.title()}"

        return number

    return re.sub(r"[_-]+", " ", stem).strip().title()


def relative_link(path: Path) -> str:
    relative_path = path.relative_to(ROOT).as_posix()
    return quote(relative_path, safe="/")


def render_files(directory: Path) -> list[str]:
    lines = []

    for file in python_files(directory):
        title = format_file_name(file.name)
        link = relative_link(file)

        lines.append(f"- [`{title}`]({link})")

    return lines


def render_directory(directory: Path, heading_level: int) -> list[str]:
    lines = []

    # Python files directly inside the current folder
    lines.extend(render_files(directory))

    # Nested folders such as P01, P02, ...
    for child in directories(directory):
        if not contains_python_files(child):
            continue

        title = format_directory_name(child.name)
        heading = "#" * min(heading_level, 6)

        if lines:
            lines.append("")

        lines.append(f"{heading} {title}")
        lines.append("")
        lines.extend(render_directory(child, heading_level + 1))

    return lines


def all_python_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.py")
        if not should_ignore(path)
    ]


def generate_readme() -> str:
    chapter_directories = [
        directory
        for directory in directories(ROOT)
        if contains_python_files(directory)
    ]

    total_files = len(all_python_files())

    lines = [
        f"# 🧙‍♂️ {BOOK_TITLE}",
        "",
        f"> {BOOK_DESCRIPTION}",
        "",
        "---",
        "",
        "## 🚀 About This Repository",
        "",
        (
            "This repository contains all code examples and exercises from the book "
            f"“{BOOK_TITLE}”.\n\n"
            "The content is carefully structured to guide you step-by-step — from your very first "
            "line of code to building more advanced, real-world projects.\n\n"
            "Each chapter represents a stage in your journey, and each part contains focused "
            "exercises to strengthen your skills."
        ),
        "",
        "---",
        "",
        "## 🧭 Repository Structure",
        "",
        "- 📁 `Sxx` → Chapter number",
        "- 📂 `Pxx` → Part inside each chapter",
        "- 🧪 `Sxx.5-SHADOW-LIB` → Bonus & challenge exercises",
        "- 🐍 `.py` → Python scripts",
        "",
        "📌 Example:",
        "```",
        "S03/P02/1.numvars_init.py",
        "```",
        "",
        "---",
        "",
        "## 📚 Contents",
        "",
    ]

    if not chapter_directories:
        lines.append("_No Python files were found._")
    else:
        for chapter in chapter_directories:
            chapter_title = format_directory_name(chapter.name)

            lines.append(f"### 📘 {chapter_title}")
            lines.append("")
            lines.extend(render_directory(chapter, heading_level=4))
            lines.append("")

    lines.extend(
        [
            "---",
            "",
            "## ▶️ Running the Examples",
            "",
            "Run any file from the project root:",
            "",
            "```bash",
            "cd path/to/file",
            "python filename.py",
            "```",
            "",
            "### Example:",
            "",
            "```bash",
            "cd S06/P03",
            "python 1.score_record_indexing.py",
            "```",
            "",
            "---",
            "",
            "## 📊 Summary",
            "",
            f"- 📚 Chapters / Sections: **{len(chapter_directories)}**",
            f"- 🐍 Python files: **{total_files}**",
            "",
            "---",
            "",
            "## 💡 Learning Philosophy",
            "",
            "- Learn by doing 🛠️",
            "- Build real intuition 🧠",
            "- Practice through exercises ⚔️",
            "- Stay curious and consistent 🚀",
            "",
            "---",
            "",
            "## 👨‍💻 Author",
            "",
            "**Mahdi Ghaemi**",
            "",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    README_FILE.write_text(
        generate_readme(),
        encoding="utf-8",
    )

    print(f"README generated successfully: {README_FILE}")
    print(f"Python files found: {len(all_python_files())}")


if __name__ == "__main__":
    main()
