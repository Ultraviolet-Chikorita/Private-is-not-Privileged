# Private Is Not Privileged — reproducibility bundle

This repository accompanies **Private Is Not Privileged** and packages the runnable notebook sequence, publication-facing result artefacts, and the current manuscript.

## Current framing

The notebooks are not organised as a search for an old `H1`/`H_priv` object. The project now treats the experiments as a sequential validation programme that separates:

1. **behavioural validity** — whether the task produces a meaningful, non-degenerate consequential target;
2. **representation** — whether activations carry target-specific held-out signal beyond negative controls;
3. **comparator strength** — whether a neural advantage survives stronger text/structured/base-rate alternatives;
4. **timing and information matching** — whether channels are compared at the same decision stage with the same externally available information;
5. **robustness and calibration** — whether conclusions survive model-family or reader changes, or are clarified by mechanistic audits.

Legacy strings such as `h1`, `H1`, or `H_priv` remain in some executable code, paths, tables, and frozen artefact names. They are retained deliberately so that old outputs and hashes remain traceable. Notebook-facing descriptions use the current framing.

## Repository layout

```text
.
├── README.md
├── CITATION.cff
├── SHA256SUMS.txt
├── .gitignore
├── .gitattributes
├── notebooks/          # 30 notebooks, with current-facing description cells
├── notebook_outputs/   # GitHub-friendly result tables, figures, manifests, checksums
├── paper/              # current British-English manuscript with Word equation objects
├── docs/
│   ├── NOTEBOOK_INDEX.md
│   ├── LEGACY_IDENTIFIERS.md
│   ├── LARGE_ARTIFACTS.md
│   └── SOURCE_ARCHIVES.md
└── scripts/
    └── verify_bundle.py
```

## Why large raw artefacts are not inside this ZIP

The original notebook-output archive contains large activation tensors and raw runtime captures, including individual files tens of megabytes in size. Those files make the archive unreliable to transfer through chat and are better handled through Git LFS, a release asset, or a data repository. This GitHub-ready core therefore includes publication-facing **results, figures, manifests, checksums, and latest-run pointers**, while documenting the omitted source archives and large binary classes in `docs/LARGE_ARTIFACTS.md`.

The supplied source archives themselves remain unchanged outside this core bundle.

## Notebook 19–22 interpretation

- **19** — scaled Qwen matched-information direct test.
- **20** — second-model-family (Mistral) matched-information replication.
- **21** — fixed nonlinear activation-reader robustness test.
- **22** — private-deliberation information-boundary decomposition.

These names describe what the notebooks test now; they do not imply that a legacy hypothesis label is being discovered.

## Verification

From the repository root:

```bash
python scripts/verify_bundle.py
```

The script checks that all notebooks parse, the expected paper is present, and the included files agree with `SHA256SUMS.txt`.
