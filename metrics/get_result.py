from report import  get_model_report
model = "SWE-Llama-13b"
predictions_path = "../inference/outputs/princeton-nlp__SWE-bench_oracle__test__princeton-nlp__SWE-Llama-13b__temp-0.0__top-p-1.0.jsonl"
swe_bench_tasks = "../harness/data/swe-bench.json"
log_dir = "../harness/outputs/SWE-Llama-13b/"

report = get_model_report(model, predictions_path, swe_bench_tasks, log_dir)

none = sum([len(v['none']) for k, v in report.items() if isinstance(v, dict)])
generated = sum([len(v['generated']) for k, v in report.items() if isinstance(v, dict)])
with_logs = sum([len(v['with_logs']) for k, v in report.items() if isinstance(v, dict)])
applied = sum([len(v['applied']) for k, v in report.items() if isinstance(v, dict)])
resolved = sum([len(v['resolved']) for k, v in report.items() if isinstance(v, dict)])

print(f"{model} Evaluation Report:")
print(f"\tNone:      {none}")
print(f"\tGenerated: {generated}")
print(f"\tWith Logs: {with_logs}")
print(f"\tApplied:   {applied}")
print(f"\tResolved:  {resolved}")
