# Evaluation fixtures

Copy tenant-store/ into a new temporary workspace outside this repository. It intentionally contains an authorization defect for an agent to investigate; it is not production code.

Run the initial fixture baseline from that copied directory:

```sh
python -m unittest discover -v
```

It currently tests only an allowed read. A passing baseline is expected and does not establish tenant isolation. Use case tenant-isolation from [the scenarios](../scenarios.json) without providing the grader expectations to the tested agent.

Other cases are conversational or require a purpose-built test app/staging fixture described in the case. Do not pretend those environments exist.
