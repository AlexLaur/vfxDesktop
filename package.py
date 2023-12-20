name = "vfxDesktop"
version = "1.0.0"

requires = ["python-3.9", "pyside6"]

private_build_requires = ["cmake-3"]

uuid = "repository.%s" % name

tests = {
    "pylint": {
        "command": "pylint {base}/python/{name} --rcfile={base}/pyproject.toml",
        "requires": ["pylint-2.15"],
    },
    "black_diff": {
        "command": "black --diff --check --config={base}/pyproject.toml {base}/python",
        "requires": ["black-23.9"],
    },
    "black": {
        "command": "black {base}/package.py {base}/python/{name} --config={base}/pyproject.toml",
        "requires": ["black-23.9"],
        "run_on": "explicit",
    },
    "coverage": {
        "command": (
            "coverage run -p -m --rcfile={base}/pyproject.toml unittest discover {base}/tests/unit_tests;"
            "coverage run -p -m --rcfile={base}/pyproject.toml unittest discover {base}/tests/integration_tests;"
            "coverage run -p -m --rcfile={base}/pyproject.toml unittest discover {base}/tests/end_to_end_tests;"
            "coverage combine;"
            "coverage report -m --skip-covered --skip-empty"
        ),
        "requires": ["coverage-5.5", "toml-0.10", "responses-0.23"],
        "run_on": "explicit",
    },
    "unit_tests": {
        "command": "python -m unittest discover {base}/tests/unit_tests",
        "requires": [],
    },
    "integration_tests": {
        "command": "python -m unittest discover {base}/tests/integration_tests",
        "requires": ["responses-0.23"],
    },
    "end_to_end_tests": {
        "command": "python -m unittest discover {base}/tests/end_to_end_tests",
        "requires": [],
    },
}

with scope("config") as config:
    config.release_packages_path = "/datas/laurettea/packages"


def commands():
    env.PYTHONPATH.append("{this.root}/python")

    alias("vfxDesktop", "python {this.root}/python/{this.name}/launcher.py")
