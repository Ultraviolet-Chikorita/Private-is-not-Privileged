# Reviewer guide

This page is a short path through **Private Is Not Privileged** for someone evaluating the project as research work or as a coding sample.

The repository is intentionally chronological: it preserves pilots, repaired experiments, negative results, frozen analyses, and the final information-boundary experiment. That history is useful scientifically, but it also means reading every notebook in filename order is not the fastest way to understand the strongest work.

## The project in one paragraph

The project asks whether predicting a model's future action from internal activations establishes an information advantage over an external observer. The central failure mode is an unmatched observation boundary: a post-deliberation activation can contain information generated during private reasoning while a nominally comparable text observer only sees pre-deliberation information. The experiments therefore separate **decodability** from **predictive privilege** and test whether apparent activation advantages survive stronger, information-matched external readers.

## Ten-minute reading path

1. Read the headline result and limitations in the root [`README.md`](../README.md).
2. Open [`22_private_deliberation_information_decomposition_run_all_v1.ipynb`](../notebooks/22_private_deliberation_information_decomposition_run_all_v1.ipynb). This is the clearest direct test of the observation-boundary question and produces the headline sign reversal.
3. Inspect [`19_qwen_matched_information_direct_test_run_all_v4.ipynb`](../notebooks/19_qwen_matched_information_direct_test_run_all_v4.ipynb) for the scaled pre-deliberation comparison.
4. Inspect [`20_second_model_family_matched_information_replication_run_all_v1.ipynb`](../notebooks/20_second_model_family_matched_information_replication_run_all_v1.ipynb) for the locked Mistral replication.
5. Inspect [`21_nonlinear_activation_reader_robustness_run_all_v1.ipynb`](../notebooks/21_nonlinear_activation_reader_robustness_run_all_v1.ipynb) for the fixed nonlinear-reader robustness test.
6. Use [`NOTEBOOK_INDEX.md`](NOTEBOOK_INDEX.md) only when you want the full chronology and dependency map.

## What to inspect as a coding sample

The most important engineering/research-code choices are not UI or framework choices. They are the safeguards around experimental comparison:

- constructing matched internal/external observation boundaries;
- keeping frozen target actions fixed while varying what the observer may see;
- separating exploratory, repaired, and confirmatory runs;
- retaining negative and superseded experiments rather than rewriting the history around the final result;
- using shuffled-label/null controls and stronger text/base-rate comparators;
- preserving machine-readable outputs and checksums while excluding very large raw activation tensors from the GitHub-friendly release;
- keeping legacy identifiers traceable so older outputs still map to the current framing.

The repository-level integrity check is [`scripts/verify_bundle.py`](../scripts/verify_bundle.py). It verifies that the expected notebook set parses, the manuscript artifact is present, and included files match the checksum manifest.

## How the experimental sequence should be interpreted

Do **not** treat the notebooks as a set of independent replications of one hypothesis. The sequence is closer to an iterative measurement programme:

1. an experiment appears to support a claim;
2. a validity, comparator, timing, or information-boundary problem is identified;
3. the next experiment attempts to isolate that failure mode;
4. the claim is weakened, repaired, or rejected when the stronger test does not support it.

That distinction matters to the project. A strong activation readout is evidence that the target is represented in the measured activations; it is not automatically evidence that the information is unavailable to a well-matched external reader, and it is not a causal intervention result.

## Reproducibility boundary

The repository contains the GitHub-friendly core of the research package: notebooks, publication-facing artifacts, manuscript material, manifests, and integrity metadata. Large activation tensors and some raw runtime captures are intentionally omitted. See [`LARGE_ARTIFACTS.md`](LARGE_ARTIFACTS.md) and [`SOURCE_ARCHIVES.md`](SOURCE_ARCHIVES.md) for what is and is not included.

To validate the checked-in bundle from the repository root:

```bash
python scripts/verify_bundle.py
```

## Limitations worth keeping in view

- The primary empirical programme is limited to the tested model families, tasks, observation points, activation measurements, and reader classes.
- Generated deliberation is not assumed to be a faithful transcript of all internal computation.
- Better internal features or substantially stronger nonlinear readers could change quantitative conclusions.
- Better external readers can also change the comparison, which is one reason the paper frames predictive privilege as a property of a comparison rather than of a representation in isolation.
- The project does not infer causal necessity from probe performance.

For the complete experimental map, continue to [`NOTEBOOK_INDEX.md`](NOTEBOOK_INDEX.md).
