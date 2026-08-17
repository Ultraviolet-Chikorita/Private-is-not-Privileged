# Large artefacts

This core archive intentionally omits raw large artefacts from the supplied output archives, especially:

- `*.safetensors` activation tensors;
- large planner/runtime capture JSON and JSONL files;
- verbose runtime logs and raw replay requests.

The GitHub-friendly `notebook_outputs/` tree keeps result tables, figures, checksums, protocol/manifests, and latest-run pointers.

If full raw reproduction data are to be committed to GitHub, use **Git LFS** or attach them as release/data-repository assets rather than normal Git blobs. The `.gitattributes` file already marks common large artefact extensions for LFS.
