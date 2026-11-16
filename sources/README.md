# Source snapshots

Full external PDFs and HTML are ignored, not redistributed. The current publisher PDF and arXiv HTML can be retrieved with `python -B tools/fetch_sources.py`; the exact audited SHA-256 values and URLs are in [SOURCES.md](../SOURCES.md) and [the download receipt](../verification/source-downloads.json). Check bytes against the frozen receipt rather than assuming a moving URL is unchanged.

The original v5 PDF is pinned in the original Quantum source commit identified by [evidence/provenance.json](../evidence/provenance.json). `tools/import_evidence.py` restores it if that source repository is available. Alternatively retrieve arXiv v5 from its versioned primary URL and compare its hash. Full source access is useful for external correspondence review, but is not required to run the self-contained exact diagnostic or build the manuscript.

The raw version-notes fetch failed HTTP 403; browser inspection succeeded. Do not fabricate a local HTML snapshot from the browser summary. All source content retains its original attribution and license.
