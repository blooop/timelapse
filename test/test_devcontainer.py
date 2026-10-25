import re
import subprocess
from pathlib import Path

DEVCONTAINER = Path(__file__).resolve().parent.parent / ".devcontainer"

# docker rejects a bind mount whose source is missing ("bind source path does
# not exist", exit 125), so container creation fails on a host that lacks one.
HOME_BIND = re.compile(r"source=\$\{localEnv:HOME\}/([^,\"]+),[^\"]*type=bind")


def home_bind_sources():
    lines = (DEVCONTAINER / "devcontainer.json").read_text(encoding="utf-8").splitlines()
    live = "\n".join(line for line in lines if not line.lstrip().startswith("//"))
    return HOME_BIND.findall(live)


def test_initialize_command_creates_every_home_bind_source(tmp_path):
    sources = home_bind_sources()
    assert sources, "no ${localEnv:HOME} bind mounts found; the pattern is stale"

    subprocess.run(
        [str(DEVCONTAINER / "claude-code" / "init-host.sh")],
        env={"HOME": str(tmp_path), "PATH": "/usr/bin:/bin"},
        check=True,
    )

    missing = [s for s in sources if not (tmp_path / s).is_dir()]
    assert not missing, f"bind sources a fresh host would lack: {missing}"
