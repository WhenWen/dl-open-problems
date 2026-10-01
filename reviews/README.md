# Decision log

Record non-candidate status changes, merges and exclusions in `decisions.json`. Initial candidates are tracked in Git and do not imply a completed review.

Each decision has `id`, `date`, `problem`, `status`, `reviewers`, `self_review` (boolean), `rationale`, and `evidence` (a nonempty list of public URLs). Evidence should link to the review PR, specific source passages or public reproduction artifacts. The decision status must match the resulting card status. Additional historical decisions may remain in the log.
