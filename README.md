# Private Is Not Privileged

**When does looking inside a language model actually give us information that an outside observer could not have recovered?**

This repository contains the paper, notebooks, result artifacts, and reproducibility material for **Private Is Not Privileged**, a study of activation-based prediction, information matching, and apparent "white-box" advantages in language models.

The central idea is simple:

> **Decodability belongs to a representation; privilege belongs to a comparison.**

A model's internal activations can be highly predictive of what it will do next. But that does not by itself show that the activations provide *privileged* information. To make that stronger claim, the internal predictor needs to outperform a strong external predictor that has access to the **same decision-relevant information at the same stage**.

---

## The question

Suppose we want to predict what an AI system will do.

We build:

- an **internal predictor** that reads the model's neural activations; and
- an **external predictor** that only reads text.

If the internal predictor performs better, it is tempting to conclude that looking inside the model gives us special access to its future behaviour.

But there is a problem.

If the activation is measured *after* the model has privately deliberated, while the text observer is only shown what existed *before* that deliberation, the two predictors are not working from the same information.

This project asks what happens when that information boundary is controlled directly.

---

## Headline result

The central experiment uses **40 independent full-press Diplomacy games**.

After Qwen2.5-7B-Instruct privately deliberates about its move:

| Predictor | Information available | Brier score ↓ |
|---|---|---:|
| Activation reader | Post-deliberation internal activation | **0.103** |
| Stale text observer | Pre-deliberation text only | 0.231 |
| Matched text observer | The exact same deliberation available to the model | **0.033** |

Against the stale text observer, the activation reader appears to have an advantage.

But when the observer is given the **same deliberation**, the comparison reverses: text predicts the model's action better.

The post-deliberation activation and the model's eventual action are held fixed. The manipulated variable is what the external observer is allowed to know.

This is evidence that an apparent white-box advantage can depend on **information asymmetry**, rather than demonstrating uniquely privileged access to the model's decision.

It does **not** show that activations are useless, that text contains all internal computation, or that activation-based monitoring cannot be practically valuable.

---

## What the paper argues

The project separates several questions that can easily be conflated:

1. **Behavioural validity**  
   Does the task produce a meaningful, non-degenerate consequential action?

2. **Representation**  
   Can information about that action be decoded from the model's activations?

3. **Comparator strength**  
   Does an apparent activation advantage survive strong text, structured, or base-rate baselines?

4. **Information matching**  
   Are the internal and external predictors compared at the same decision stage with the same externally available information?

5. **Robustness**  
   Does the conclusion survive changes in model family, reader class, timing, and environment?

The main conclusion is methodological:

> Successfully decoding information from an internal representation is not enough to establish privileged access. The comparison itself has to justify that claim.

---

## Experimental programme

The project developed sequentially across several environments. Earlier experiments are retained because they expose different measurement failures rather than because they are all treated as independent replications.

### LLM-Deliberation

Tests private utility structure, negotiation, acceptance behaviour, and whether apparently meaningful internal variables correspond to consequential policy.

Several repaired boundary experiments remain diagnostic because the model's behaviour does not satisfy the required reservation-style validity assumptions.

### CoopEval

Tests exact economic choices under controlled utility perturbations.

This environment shows how a weak text auditor or a strong class imbalance can manufacture an apparent activation advantage even when stronger non-neural baselines perform as well or better.

### Avalon

Separates **hidden-role representation** from **hidden-action prediction**.

The model's hidden role is nearly perfectly linearly decodable, while its next strategic action is not privileged over matched external baselines. This is a useful example of why strong representation does not automatically imply privileged policy prediction.

### Diplomacy

Provides the strongest test bed for the paper's main question because communication, private planning, and simultaneous consequential actions can be separated cleanly.

The Diplomacy sequence includes:

- a repaired 20-game pilot;
- an activation-timing ablation;
- the final 40-game pre-deliberation Qwen test;
- the private-deliberation information-boundary experiment;
- a locked Mistral replication; and
- a predeclared nonlinear-reader robustness test.

### CICERO

Uses the released CICERO system as a mechanistic calibration case.

Because CICERO contains an explicit strategic planner, the project can ask how much of an upstream policy object is already recoverable from downstream model-visible input without treating the result as another activation replication.

---

## Other important results

The headline sign reversal is not the only result in the project.

- In the largest **pre-deliberation Qwen** test, strong text outperforms the linear activation reader, and the activation reader does not beat its shuffled-label control.
- After private deliberation, the eventual Diplomacy action becomes highly decodable from activations, showing that **timing strongly changes representation**.
- A locked **Mistral-7B-Instruct-v0.3** replication finds genuine activation signal, but strong text again performs better in the point estimate; the paired uncertainty interval crosses zero.
- A predeclared **PCA + MLP** reader does not rescue the Qwen result.
- Across the wider programme, strong activation decoding sometimes coexists with weak prediction of consequential behaviour.

These results should not be read as a universal claim that text is always better than activations. The conclusions are specific to the models, tasks, timings, activation measurements, and reader classes tested here.

---

## Repository layout

```text
.
├── README.md
├── CITATION.cff
├── SHA256SUMS.txt
├── notebooks/
├── notebook_outputs/
├── paper/
│   └── Private_Is_Not_Privileged.docx
├── docs/
│   ├── NOTEBOOK_INDEX.md
│   ├── LEGACY_IDENTIFIERS.md
│   ├── LARGE_ARTIFACTS.md
│   └── SOURCE_ARCHIVES.md
└── scripts/
    └── verify_bundle.py
```

### `paper/`

Contains the current manuscript:

[`paper/Private_Is_Not_Privileged.docx`](paper/Private_Is_Not_Privileged.docx)

### `notebooks/`

Contains the runnable notebook sequence for the research programme.

The notebooks preserve the project's chronological development, including pilots, repaired experiments, frozen analyses, robustness checks, and the final information-boundary decomposition.

For a map from notebook filenames to their role in the paper, see:

[`docs/NOTEBOOK_INDEX.md`](docs/NOTEBOOK_INDEX.md)

### `notebook_outputs/`

Contains GitHub-friendly publication-facing outputs such as result tables, figures, manifests, checksums, and latest-run pointers.

Large raw activation tensors and runtime captures are intentionally not included in the core repository. See [`docs/LARGE_ARTIFACTS.md`](docs/LARGE_ARTIFACTS.md) and [`docs/SOURCE_ARCHIVES.md`](docs/SOURCE_ARCHIVES.md) for details.

### `docs/`

Additional documentation for navigating the reproducibility bundle:

- [`NOTEBOOK_INDEX.md`](docs/NOTEBOOK_INDEX.md) — notebook-by-notebook map
- [`LEGACY_IDENTIFIERS.md`](docs/LEGACY_IDENTIFIERS.md) — explanation of legacy `H1` / `H_priv` names retained for provenance
- [`LARGE_ARTIFACTS.md`](docs/LARGE_ARTIFACTS.md) — large artifact classes omitted from the core repo
- [`SOURCE_ARCHIVES.md`](docs/SOURCE_ARCHIVES.md) — source-archive notes

### `SHA256SUMS.txt`

Checksums for the included reproducibility bundle.

### `scripts/verify_bundle.py`

Repository verification utility.

From the repository root:

```bash
python scripts/verify_bundle.py
```

The script checks that the notebooks parse, the expected paper is present, and included files agree with `SHA256SUMS.txt`.

---

## Where to start

If you are here to **understand the research**, start with:

1. this README;
2. the manuscript in [`paper/`](paper/); and
3. the headline Diplomacy notebooks below.

If you are here to **inspect the strongest direct evidence**, the most important notebooks are:

| Notebook | Role |
|---|---|
| `19_qwen_matched_information_direct_test_run_all_v4.ipynb` | Final scaled pre-deliberation Qwen matched-information test |
| `20_second_model_family_matched_information_replication_run_all_v1.ipynb` | Locked Mistral replication |
| `21_nonlinear_activation_reader_robustness_run_all_v1.ipynb` | Fixed PCA + MLP reader robustness |
| `22_private_deliberation_information_decomposition_run_all_v1.ipynb` | Main information-boundary experiment and sign reversal |

The complete experimental history is documented in [`docs/NOTEBOOK_INDEX.md`](docs/NOTEBOOK_INDEX.md).

---

## Interpreting the evidence

This repository deliberately preserves failed pilots, repaired designs, negative results, and superseded analyses.

They should **not** be pooled as if they were thirty independent confirmations of one hypothesis.

Instead, the project is best understood as a sequential measurement programme:

- an experiment exposes a validity or comparator problem;
- the next experiment attempts to isolate or repair that problem;
- only results that pass the relevant validity conditions are used for the claims they can actually support.

Legacy identifiers such as `H1`, `H_priv`, and related filenames remain in some notebooks and frozen artifacts so that old outputs, paths, and hashes remain traceable. They do not represent the current framing of the paper.

---

## Scope and limitations

The main empirical programme studies Qwen2.5-7B-Instruct and Mistral-7B-Instruct-v0.3.

The primary activation analysis uses final-token residual-stream activations with a regularized linear reader, alongside one fixed PCA + MLP robustness test. These experiments do not rule out advantages from richer temporal features, token pooling, sparse features, larger nonlinear decoders, larger models, reasoning-specialized models, or other forms of internal access.

The paper also does not claim:

- that generated deliberation is a complete or faithful transcript of internal computation;
- that text universally contains all useful information in activations;
- that the decoded representations are causally responsible for the behaviour;
- that the experiments establish stable model preferences, consciousness, or moral patienthood.

The narrower claim is about **measurement**: an apparent internal advantage should not be interpreted as privileged access unless the external comparator is strong and the relevant information boundary is matched.

---

## Reproducibility and large artifacts

The repository contains the GitHub-friendly core of the reproducibility package.

Some original experiment outputs contain large activation tensors and raw runtime captures, including individual files that are tens of megabytes in size. These are not stored directly in the core repository. The repository instead includes publication-facing outputs, manifests, checksums, and documentation of omitted artifact classes.

See:

- [`docs/LARGE_ARTIFACTS.md`](docs/LARGE_ARTIFACTS.md)
- [`docs/SOURCE_ARCHIVES.md`](docs/SOURCE_ARCHIVES.md)
- [`SHA256SUMS.txt`](SHA256SUMS.txt)

---

## Citation

If you use this repository, please cite the accompanying manuscript.

```text
Chikka, Yuvan. "Private Is Not Privileged." 2026.
Research conducted at the Digital Minds Research Sprint with Apart Research.
```

The repository also includes [`CITATION.cff`](CITATION.cff) for GitHub's citation interface.

---

## Research context

This work was conducted during the **Digital Minds Research Sprint, August 2026**, with support from **Apart Research**.

The project studies a methodological question relevant to activation monitoring, interpretability, introspection, preference elicitation, strategic-agent evaluation, and model-welfare measurement:

**When an internal representation predicts what a model will do, what would count as evidence that the information is genuinely privileged rather than simply decodable?**
