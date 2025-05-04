import os
import yaml
import re
from pathlib import Path

# Mapping folder names to display titles
FOLDER_NAME_MAP = {
    'ag': 'Algebraic Geometry',
    'nt': 'Number Theory',
    'prob': 'Probability',
    'algebra': 'Algebra',
    'topo': 'Topology',
    'an': 'Analysis',
    'la': 'Linear Algebra',
}

MATH_ROOT = "math"
BASE_LINK = "/math/"
CARDGRID_YML = "_data/math_index_cardgrids.yml"
MENUBAR_YML = "_data/math_menubar.yml"

def title_from_folder(folder):
    return FOLDER_NAME_MAP.get(folder, folder.replace("_", " ").title())

def title_from_filename(filename):
    stem = Path(filename).stem
    name = re.sub(r'^\d+_', '', stem)
    return name.replace("_", " ").title()

def slug_from_filename(filename):
    stem = Path(filename).stem
    return re.sub(r'^\d+_', '', stem)

def slug_from_folder(folder_name):
    return re.sub(r'^\d+_', '', folder_name)

def title_from_path(path_name):
    name = re.sub(r'^\d+_', '', path_name)
    return name.replace("_", " ").title()

def sort_by_prefix_number(paths):
    def extract_number(path_obj):
        match = re.match(r'^(\d+)_', path_obj.name)
        return int(match.group(1)) if match else float('inf')
    return sorted(paths, key=extract_number)

# ---- CARD GRID GENERATOR ----

def generate_card_data():
    cards = []
    for folder in sorted(os.listdir(MATH_ROOT)):
        full_path = os.path.join(MATH_ROOT, folder)
        if not os.path.isdir(full_path) or folder.startswith("."):
            continue

        title = title_from_folder(folder)
        link = BASE_LINK + folder + "/"
        topics = collect_topic_names(full_path)
        description = ", ".join(topics) if topics else None

        cards.append({
            "title": title,
            "link": link,
            "description": description
        })

    return {"items": cards}

def collect_topic_names(folder_path):
    topics = []
    for name in sorted(os.listdir(folder_path)):
        sub_path = os.path.join(folder_path, name)
        if os.path.isdir(sub_path) and not name.startswith("."):
            topics.append(title_from_path(name))
    return topics

# ---- MENUBAR GENERATOR ----

def generate_menubar_structure():
    structure = [{
        "label": "Math Notes",
        "items": []
    }]

    for category in sorted(os.listdir(MATH_ROOT)):
        cat_path = os.path.join(MATH_ROOT, category)
        if not os.path.isdir(cat_path) or category.startswith("."):
            continue

        category_entry = {
            "name": title_from_folder(category),
            "link": f"/math/{category}/",
            "items": []
        }

        for topic_path in sort_by_prefix_number([p for p in Path(cat_path).iterdir() if p.is_dir()]):
            topic_slug = slug_from_folder(topic_path.name)
            topic_title = title_from_path(topic_path.name)
            topic_entry = {
                "name": topic_title,
                "link": f"/math/{category}/{topic_slug}/",
                "items": []
            }

            note_files = [f for f in topic_path.glob("*.md") if f.name != "index.md"]
            for note_file in sort_by_prefix_number(note_files):
                note_name = title_from_filename(note_file.name)
                if note_name.lower() == "index":
                    continue
                slug = slug_from_filename(note_file.name)
                note_entry = {
                    "name": note_name,
                    "link": f"/math/{category}/{topic_slug}/{slug}"
                }
                topic_entry["items"].append(note_entry)

            category_entry["items"].append(topic_entry)

        structure[0]["items"].append(category_entry)

    return structure

# ---- INDEX.MD GENERATORS ----

def write_index_file(path, content):
    os.makedirs(path.parent, exist_ok=True)
    with open(path, "w") as f:
        f.write(content)

def generate_topic_index(topic_path: Path, category: str, topic_folder: str) -> str:
    topic_slug = slug_from_folder(topic_folder)
    topic_title = title_from_path(topic_folder)
    files = [f for f in topic_path.glob("*.md") if f.name != "index.md"]
    if not files:
        return (
            "---\n"
            "hide_hero: true\n"
            "menubar: math_menubar\n"
            f"permalink: /math/{category}/{topic_slug}/\n"
            "---\n\n"
            f"## {topic_title}\n"
        )

    files = sort_by_prefix_number(files)
    lines = [
        "---",
        "hide_hero: true",
        "menubar: math_menubar",
        f"permalink: /math/{category}/{topic_slug}/",
        "---\n",
        f"## {topic_title}",
    ]

    for f in files:
        title = title_from_filename(f.name)
        lines.append(f"- [{title}]({f.name})")

    return "\n".join(lines)

def generate_category_index(cat_path: Path, category: str) -> str:
    lines = [
        "---",
        "hide_hero: true",
        "menubar: math_menubar",
        f"permalink: /math/{category}/",
        "---\n",
        f"# {title_from_folder(category)}",
    ]

    for topic_path in sort_by_prefix_number([p for p in cat_path.iterdir() if p.is_dir()]):
        topic_slug = slug_from_folder(topic_path.name)
        topic_title = title_from_path(topic_path.name)
        lines.append(f"\n## {topic_title}")
        files = [f for f in topic_path.glob("*.md") if f.name != "index.md"]
        if not files:
            continue
        files = sort_by_prefix_number(files)
        for f in files:
            title = title_from_filename(f.name)
            lines.append(f"- [{title}](./{topic_path.name}/{f.name})")

    return "\n".join(lines)

# ---- YAML WRITER ----

def write_yaml(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)


# ---- MAIN ----

if __name__ == "__main__":
    # Generate card grid
    card_data = generate_card_data()
    write_yaml(card_data, CARDGRID_YML)
    print(f"✅ Card grid YAML written to: {CARDGRID_YML}")

    # Generate sidebar menu
    menubar_data = generate_menubar_structure()
    write_yaml(menubar_data, MENUBAR_YML)
    print(f"✅ Menubar YAML written to: {MENUBAR_YML}")

    # Generate index.md files
    for cat_path in Path(MATH_ROOT).iterdir():
        if not cat_path.is_dir():
            continue
        category = cat_path.name

        # Per-topic index.md
        for topic_path in cat_path.iterdir():
            if not topic_path.is_dir():
                continue
            topic = topic_path.name
            topic_md = generate_topic_index(topic_path, category, topic)
            write_index_file(topic_path / "index.md", topic_md)

        # Category-level index.md
        cat_md = generate_category_index(cat_path, category)
        write_index_file(cat_path / "index.md", cat_md)

    print(f"✅ index.md files written under each category and topic folder")
