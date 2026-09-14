# Private Is Not Privileged

**When does looking inside a language model actually provide information that a well-matched outside observer could not recover?**

This repository contains the paper, executed research notebooks, result artifacts, and reproducibility material for a study of activation-based prediction, information matching, and apparent white-box advantages in language models.

> **Core distinction:** decodability belongs to a representation; predictive privilege belongs to a comparison.

A model's internal activations can be highly predictive of what it will do next. That does not by itself establish privileged information. To support the stronger claim, the internal reader needs to outperform a strong external reader that receives the relevant externally available information at the same observation boundary.

## Start here

- **Research/code reviewer:** [`docs/REVIEWER_GUIDE.md`](docs/REVIEWER_GUIDE.md)
- **Notebook-by-notebook map:** [`docs/NOTEBOOK_INDEX.md`](docs/NOTEBOOK_INDEX.md)
- **Large-artifact policy:** [`docs/LARGE_ARTIFACTS.md`](docs/LARGE_ARTIFACTS.md)
- **Source/reproducibility notes:** [`docs/SOURCE_ARCHIVES.md`](docs/SOURCE_ARCHIVES.md)
- **Bundle integrity check:** [`scripts/verify_bundle.py`](scripts/verify_bundle.py)

If you only inspect the decisive experiments, start with notebooks **19-22**. Notebook 22 is the clearest direct test of the information-boundary question.

## Headline experiment

The central experiment uses 40 independent full-press Diplomacy games. After Qwen2.5-7B-Instruct privately deliberates about its move:

| Predictor | Information available | Brier score ↓ |
| --- | --- | ---: |
| Activation reader | Post-deliberation internal activation | **0.103** |
| Stale text observer | Pre-deliberation text only | 0.231 |
| Matched text observer | The same deliberation available to the model | **0.033** |

Against the stale observer, the activation reader appears to have an advantage. Once the external observer receives the relevant deliberation, the comparison reverses.

The post-deliberation activation and target action are held fixed; what changes is the information available to the external reader. The result therefore supports a measurement claim: an apparent white-box advantage can be produced by an information-boundary mismatch.

It does **not** show that activations are useless, that text contains all internal computation, or that internal monitoring cannot be practically valuable.

## Experimental logic

The project separates questions that are easy to conflate:

1. **Behavioral validity** - does the task produce a meaningful consequential action?
2. **Representation** - is information about that action decodable from activations?
3. **Comparator strength** - does the apparent advantage survive strong text, structured, and base-rate baselines?
4. **Information matching** - are the internal and external readers compared at the same decision stage?
5. **Robustness** - does the conclusion survive changes in model family, reader class, timing, and environment?

The repository preserves failed pilots, repaired designs, negative results, and superseded analyses on purpose. The notebooks should not be pooled as independent confirmations of one hypothesis. They document an iterative measurement programme in which later experiments were motivated by failure modes exposed by earlier ones.

## Strongest direct evidence

| Notebook | Role |
| --- | --- |
| [`19_qwen_matched_information_direct_test_run_all_v4.ipynb`](notebooks/19_qwen_matched_information_direct_test_run_all_v4.ipynb) | scaled pre-deliberation Qwen matched-information test |
| [`20_second_model_family_matched_information_replication_run_all_v1.ipynb`](notebooks/20_second_model_family_matched_information_replication_run_all_v1.ipynb) | locked Mistral replication |
| [`21_nonlinear_activation_reader_robustness_run_all_v1.ipynb`](notebooks/21_nonlinear_activation_reader_robustness_run_all_v1.ipynb) | fixed PCA + MLP activation-reader robustness |
| [`22_private_deliberation_information_decomposition_run_all_v1.ipynb`](notebooks/22_private_deliberation_information_decomposition_run_all_v1.ipynb) | main observation-boundary experiment and sign reversal |

The full chronology and dependency map is in [`docs/NOTEBOOK_INDEX.md`](docs/NOTEBOOK_INDEX.md).

## Wider experimental programme

The research developed across several environments, each exposing a different measurement problem:

- **LLM-Deliberation** - tests whether apparently meaningful internal variables correspond to valid consequential behavior.
- **CoopEval** - exposes how weak text auditors and class imbalance can manufacture apparent activation advantages.
- **Avalon** - separates hidden-role representation from hidden-action prediction.
- **Diplomacy** - provides the strongest information-boundary tests because communication, private planning, and consequential simultaneous actions can be separated.
- **CICERO** - serves as a mechanistic calibration case with an explicit upstream strategic planner.

Across the programme, strong activation decodability sometimes coexists with weak or absent predictive privilege over matched external baselines.

## Repository layout

```text
.
├── README.md
├── CITATION.cff
├── SHA256SUMS.txt
├── notebooks/             executed experimental sequence
├── notebook_outputs/      publication-facing tables, figures and manifests
├── paper/                 manuscript artifact
├── docs/
│   ├── REVIEWER_GUIDE.md
│   ├── NOTEBOOK_INDEX.md
│   ├── LEGACY_IDENTIFIERS.md
│   ├── LARGE_ARTIFACTS.md
│   └── SOURCE_ARCHIVES.md
└── scripts/
    └── verify_bundle.py
```

Large activation tensors and some raw runtime captures are intentionally omitted from the GitHub-friendly core. Publication-facing outputs, manifests, checksums, and provenance documentation are retained so the boundary is explicit rather than silently incomplete.

## Verify the checked-in bundle

From the repository root:

```bash
python scripts/verify_bundle.py
```

The verifier checks that the expected notebook set parses, the manuscript artifact is present, and included files agree with `SHA256SUMS.txt`.

## Scope and limitations

The main empirical programme studies Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3 using the activation measurements and reader classes described in the manuscript. The work does not rule out advantages from richer temporal features, token pooling, sparse features, substantially larger nonlinear decoders, different models, or other forms of internal access.

The paper also does not assume generated deliberation is a complete or faithful transcript of internal computation, infer causal necessity from probe performance, or claim text is universally superior to activations.

The narrower methodological claim is that **an apparent internal advantage should not be interpreted as privileged access unless the external comparator is strong and the relevant information boundary is matched**.

## Research context and citation

This work was conducted during the **Digital Minds Research Sprint, August 2026**, with support from **Apart Research**.

If you use this repository, cite the accompanying manuscript. A machine-readable citation is provided in [`CITATION.cff`](CITATION.cff).
