# Charm: Flow Invoke

Execute an existing flow from your library.

## Invocation

```
@flow/invoke [flow-name]
```

## What It Does

- Locates the named flow in `library/flows/`
- Verifies dependencies are available
- Resolves any remaining parameters
- Executes the flow with progress reporting
- Delivers results and captures learnings

## See Also

- `@flow/create` — Design a new flow
- `@flow/adapt` — Customize a shared flow
