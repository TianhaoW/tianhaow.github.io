import os
import yaml

# Mapping of short folder names to clean titles (adjust as needed)
FOLDER_NAME_MAP = {
    'ag': 'Algebraic Geometry',
    'nt': 'Number Theory',
    'prob': 'Probability',
    'algebra': 'Algebra',
    'topo': 'Topology',
    'an': 'Analysis',
    'la': 'Linear Algebra',
}

# Root math directory (relative to this script or your repo root)
MATH_ROOT = "math"
BASE_LINK = "/math/"
OUTPUT_FILE = "_data/math_index_cardgrids.yml"

def title_from_folder(folder):
    return FOLDER_NAME_MAP.get(folder, folder.replace("_", " ").title())

def collect_topic_names(folder_path):
    topics = []
    for name in sorted(os.listdir(folder_path)):
        sub_path = os.path.join(folder_path, name)
        if os.path.isdir(sub_path) and not name.startswith("."):
            topics.append(name.replace("_", " "))
    return topics

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

def write_yaml(data, path):
    with open(path, "w") as f:
        yaml.dump(data, f, sort_keys=False, allow_unicode=True)

if __name__ == "__main__":
    data = generate_card_data()
    write_yaml(data, OUTPUT_FILE)
    print(f"✅ YAML file generated at: {OUTPUT_FILE}")