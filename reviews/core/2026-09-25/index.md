# SST core review — September 25, 2026

Imported historical reports:

- [Core correctness review](SST_CORE_CORRECTNESS_REVIEW.md): eleven reproduced findings, coverage limits, repair directions, and retained probe source.
- [Element-impact follow-up](SST_CORE_ELEMENTS_IMPACT.md): actual element reproductions and narrower exposure claims.
- [Finding tracker](findings.json): IDs, historical severity/observations, current reassessment results and fields for fix evidence.
- [Import provenance](provenance.json): original paths, hashes, reviewed revisions, and the link-only import transformation.

The review covered core `f54d79af27c8756b50dbb9e8eb356eb5dcbee4d9` and elements `9a3de5e2e9ea343b49bb09ffc18bccc2b61c5ba1`. These differ from the current devel runtime-validation revisions. The imported reports remain historical observations. The [October 6 reassessment](../2026-10-06/index.md) reproduces all eleven findings on recorded devel revisions. Generic passing regressions do not close a finding without its targeted reproducer.

## Finding status

| ID | Historical priority | Feature | Current tracking status |
|---|---|---|---|
| F01 | P1 | Clock activation during a callback | Reproduced on tested devel |
| F02 | P1 | Shared/scoped parameters | Reproduced on tested devel |
| F03 | P1 | Discrete distributions | Reproduced on tested devel |
| F04 | P1, conditional | Polymorphic unique_ptr serialization | Reproduced on tested devel |
| F05 | P2 | StandardMem locked-write responses | Reproduced on tested devel |
| F06 | P2 | Subcomponent statistic configuration | Reproduced on tested devel |
| F07 | P2 | Batched histogram samples | Reproduced on tested devel |
| F08 | P2 | Histogram origin | Reproduced on tested devel |
| F09 | P2 | Floating-point histogram range | Reproduced on tested devel |
| F10 | P2 | Floating-point accumulator maximum | Reproduced on tested devel |
| F11 | P2, limited current exposure | Accumulator variance API | Reproduced on tested devel |

Update findings.json after a focused reassessment: record tested source revision, command/artifact, observed result, and fix/regression evidence when applicable. Preserve the imported reports and original provenance; put subsequent review results in a new dated record.

Source links in the copies point to the reviewed commits rather than whichever branch happens to be checked out. The original Markdown files remain in sst-core untouched. Temporary paths mentioned in the old reports are historical artifact locations; their continued existence has not been verified. The retained code is available in the reports for reconstruction.

The [current runtime report](../../../RUNTIME_VALIDATION.md) is a separate validation campaign.
