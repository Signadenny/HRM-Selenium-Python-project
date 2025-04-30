import subprocess
import yaml
import sys

def run_test_suite(suite_name):
    with open("config/test_suite.yaml") as f:
        config = yaml.safe_load(f)

    if suite_name not in config["suites"]:
        print(f"❌ Test suite '{suite_name}' not found.")
        sys.exit(1)

    marker = config["suites"][suite_name]["markers"]
    report_file = f"reports/{suite_name}_report.html"

    # Construct pytest command
    cmd = [
        "pytest",
        "-v", "-s",
        f"-m", marker,
        "--reruns", "1",
        "--reruns-delay", "2",
        f"--html={report_file}",
        "--self-contained-html"
    ]

    print(f"🚀 Running test suite: {suite_name}")
    print(f"🧪 Marker: {marker}")
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❌ Please provide a suite name. Example: python run_suite.py smoke")
    else:
        run_test_suite(sys.argv[1])