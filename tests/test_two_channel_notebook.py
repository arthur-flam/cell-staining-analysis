"""Smoke checks for the notebook's two-stain input and intensity columns."""

import ast
import json
import tempfile
import unittest
from pathlib import Path

import cellpose
from cellpose import io
import numpy as np
import skimage as ski


NOTEBOOK = json.loads((Path(__file__).resolve().parents[1] / "notebook.ipynb").read_text())


def notebook_function(name):
    for cell in NOTEBOOK["cells"]:
        if cell["cell_type"] != "code":
            continue
        cell_source = "".join(cell["source"])
        if f"def {name}(" not in cell_source:
            continue
        source = ast.parse(cell_source)
        for node in source.body:
            if isinstance(node, ast.FunctionDef) and node.name == name:
                namespace = {"Path": Path, "np": np, "ski": ski, "io": io, "cellpose": cellpose}
                exec(compile(ast.Module(body=[node], type_ignores=[]), "notebook.ipynb", "exec"), namespace)
                return namespace[name]
    raise AssertionError(f"Notebook function not found: {name}")


class TwoChannelNotebookTest(unittest.TestCase):
    def test_composite_uses_only_lamin_b1_and_dapi_planes(self):
        with tempfile.TemporaryDirectory() as directory:
            field = Path(directory)
            lamin_b1 = np.zeros((16, 16, 3), dtype=np.uint8)
            dapi = np.zeros_like(lamin_b1)
            lamin_b1[..., 1] = 40
            dapi[..., 2] = 80
            lamin_b1[..., 0] = 255  # No signal from the first TIFF plane is used.
            ski.io.imsave(field / "Lamin B1.tif", lamin_b1, check_contrast=False)
            ski.io.imsave(field / "dapi.tif", dapi, check_contrast=False)

            composite, normalized = notebook_function("segmentation_image")(field)
            np.testing.assert_array_equal(composite[..., 0], 0)
            np.testing.assert_array_equal(composite[..., 1], 40)
            np.testing.assert_array_equal(composite[..., 2], 80)
            self.assertTrue(np.all(normalized[..., 1:] == 1))

            masks = np.zeros((16, 16), dtype=np.uint16)
            masks[2:12, 2:12] = 1
            stats = notebook_function("cell_stats")(masks, composite)
            self.assertEqual(stats[0]["median_intensity_lamin_b1"], 40)
            self.assertEqual(stats[0]["median_intensity_dapi"], 80)
            self.assertEqual(len([name for name in stats[0] if name.startswith("median_intensity_")]), 2)


if __name__ == "__main__":
    unittest.main()
