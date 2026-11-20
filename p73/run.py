"""Platform trial P-73 (combsmith/software-factory#1030): what the Checks API takes of one check run's annotations.

Each request's body is written to out/req-N.json and GitHub's answer, by `gh api --include`, to raw/resp-N. Nothing is
printed: the job redacts raw/ with software-factory's tools.redact_trial before anything is uploaded."""
import json, os, pathlib, subprocess

REPO, SHA = os.environ["GH_REPO"], os.environ["HEAD_SHA"]
out, raw = pathlib.Path("out"), pathlib.Path("raw")
out.mkdir(exist_ok=True); raw.mkdir(exist_ok=True)
n = 0


def note(i, path="p73/a.py", line=1, message=None):
    return {"path": path, "start_line": line, "end_line": line, "annotation_level": "notice",
            "message": message if message is not None else "P-73 annotation %d" % i, "title": "p73 %d" % i}


def ask(method, path, body, label):
    global n
    n += 1
    (out / ("req-%d.json" % n)).write_text(json.dumps({"label": label, "method": method, "path": path, "body": body}))
    with open(raw / ("resp-%d" % n), "wb") as f:
        subprocess.run(["gh", "api", "--include", "-X", method, path, "--input", "-"], input=json.dumps(body).encode(),
                       stdout=f, stderr=subprocess.DEVNULL)
    return n


def made(k):
    """The id of the check run answer k made, from its body after the headers, or None."""
    text = (raw / ("resp-%d" % k)).read_bytes().decode("utf-8", "replace")
    try:
        return json.loads(text.split("\r\n\r\n", 1)[-1].split("\n\n", 1)[-1]).get("id")
    except ValueError:
        return None


def run(name, notes):
    return {"name": name, "head_sha": SHA, "status": "completed", "conclusion": "neutral",
            "output": {"title": name, "summary": "Platform trial P-73.", "annotations": notes}}


runs = "/repos/%s/check-runs" % REPO
ask("POST", runs, run("p73-one", [note(1)]), "one annotation")
fifty = ask("POST", runs, run("p73-fifty", [note(i) for i in range(1, 51)]), "fifty annotations")
ask("POST", runs, run("p73-fifty-one", [note(i) for i in range(1, 52)]), "fifty-one annotations")
rid = made(fifty)
if rid is not None:
    for batch in range(3):
        ask("PATCH", "%s/%d" % (runs, rid), {"output": {"title": "p73-fifty", "summary": "Platform trial P-73.",
            "annotations": [note(50 * (batch + 1) + i) for i in range(1, 51)]}}, "fifty more, update %d" % (batch + 1))
    for page in (1, 2, 3):
        ask("GET", "%s/%d/annotations?per_page=100&page=%d" % (runs, rid, page), None, "annotations page %d" % page)
for size in (65536, 65535):
    k = ask("POST", runs, run("p73-message-%d" % size, [note(1, message="m" * size)]), "a message of %d characters" % size)
    got = made(k)
    if got is not None:
        ask("GET", "%s/%d/annotations" % (runs, got), None, "read back the message of %d" % size)
k = ask("POST", runs, run("p73-off-diff", [note(1, path="README.md")]), "an annotation off the diff")
got = made(k)
if got is not None:
    ask("GET", "%s/%d/annotations" % (runs, got), None, "read back the annotation off the diff")
bare = note(1); bare.pop("start_line"); bare.pop("end_line")
ask("POST", runs, run("p73-no-line", [bare]), "an annotation with no line")
