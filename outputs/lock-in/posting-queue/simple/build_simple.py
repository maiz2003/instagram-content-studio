"""Build the step-by-step "guided" copy of the posting queue (separate site; the original is untouched).

Run from the repo root:
    python3 outputs/lock-in/posting-queue/simple/build_simple.py <full-site-dir> <out-dir>
<full-site-dir> is the folder built by site-build/build_site.py (it holds clips/, carousels/, setup/, stories/ and the zips).
The page data comes from posting-queue/clips.json and the Stories text from account-manager/build_guide.py.
"""
import ast, json, os, shutil, sys

full, out = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))

clips = json.load(open(os.path.join(ROOT, "outputs/lock-in/posting-queue/clips.json")))

# Stories text per day: lifted from the guide generator so the two never disagree
src = open(os.path.join(ROOT, "outputs/lock-in/account-manager/build_guide.py")).read()
tree = ast.parse(src)
STORIES = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == "STORIES")

posts = [c for c in clips if isinstance(c.get("week"), int)]
AI = {9, 11, 14, 15} | {c["n"] for c in posts if c["week"] == 3}
TRIAL = {10, 13, 17, 20}
data = {
    "posts": [{
        "n": c["n"], "day": c["day"], "title": c["title"], "kind": c["kind"], "type": c["type"],
        "caption": c["caption"], "file": c.get("file"), "zip": c.get("zip"), "slides": c.get("slides", []),
        "ai": c["n"] in AI, "trial": c["n"] in TRIAL,
    } for c in posts],
    "stories": {str(k): v for k, v in STORIES.items()},
    "setup": [c for c in clips if c["week"] == "setup"],
    "bgs": [c for c in clips if c["week"] == "stories"],
}

shutil.rmtree(out, ignore_errors=True)
shutil.copytree(full, out)
os.remove(os.path.join(out, "index.html"))
tpl = open(os.path.join(HERE, "template.html")).read()
open(os.path.join(out, "index.html"), "w").write(tpl.replace("/*DATA*/null", json.dumps(data, ensure_ascii=False)))
print("built", out, len(data["posts"]), "posts")
