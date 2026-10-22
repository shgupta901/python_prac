def dag_fixture():
    return [
        {"id": "a", "parents": []},
        {"id": "b", "parents": ["a"]},
        {"id": "c", "parents": ["a"]},
        {"id": "m", "parents": ["b", "c"]},
        {"id": "d", "parents": ["m"]}
    ]


def ancestors(commits, commit_id):
    commit_lookup = {commit["id"]: commit for commit in commits}

    if commit_id not in commit_lookup:
        return []

    stack = list(commit_lookup[commit_id]["parents"])
    seen = set()

    while stack:
        current_id = stack.pop()

        if current_id in seen:
            continue

        seen.add(current_id)

        if current_id in commit_lookup:
            stack.extend(commit_lookup[current_id]["parents"])

    return sorted(seen)


def is_ancestor(commits, a, b):
    if a == b:
        return False

    return a in ancestors(commits, b)
