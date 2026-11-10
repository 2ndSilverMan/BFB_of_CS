"""Execute only the explicitly listed, repository-authored Python examples.

This is not a sandbox for untrusted Markdown and does not execute other
languages, arbitrary repository files, downloaded code, or network requests.
The examples are small standard-library calculations with assertions.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
EXAMPLE_DOCS = (
    "Hardware-and-Embedded/Circuits-and-Electronics.md",
    "Hardware-and-Embedded/HDL-and-FPGA.md",
    "Hardware-and-Embedded/Microcontrollers-and-Interfaces.md",
    "Hardware-and-Embedded/Embedded-Real-Time-Design.md",
    "Graphics-and-Interaction/Graphics/Geometry-and-Cameras.md",
    "Graphics-and-Interaction/Graphics/Rendering-Fundamentals.md",
    "Graphics-and-Interaction/Graphics/Data-Visualization.md",
    "Graphics-and-Interaction/HCI/Usability-Evaluation.md",
    "Computing-and-Society/Computing-Social-and-Environmental-Impact.md",
    "Research-Practice/Research-Design-and-Validity.md",
    "Research-Practice/Research-Reproducibility.md",
)


class NewDomainExampleTests(unittest.TestCase):
    def test_python_examples(self):
        for relative in EXAMPLE_DOCS:
            source = (ROOT / relative).read_text(encoding="utf-8")
            blocks = re.findall(r"^```python\s*\n(.*?)^```\s*$",
                                source, re.MULTILINE | re.DOTALL)
            with self.subTest(document=relative):
                self.assertTrue(blocks, "expected at least one Python example")
            for index, code in enumerate(blocks, 1):
                with self.subTest(document=relative, block=index):
                    # Each block is intentionally standalone; assertions stay on.
                    result = subprocess.run(
                        [sys.executable, "-I", "-c", code],
                        capture_output=True, text=True, timeout=10,
                        cwd=ROOT,
                    )
                    self.assertEqual(
                        result.returncode, 0,
                        f"{relative} block {index}:\n{result.stdout}\n{result.stderr}",
                    )


if __name__ == "__main__":
    unittest.main(verbosity=2)
