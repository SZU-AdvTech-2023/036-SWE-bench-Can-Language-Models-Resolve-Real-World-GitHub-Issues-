#!/bin/bash
python run_evaluation.py \
    --predictions_path "../inference/outputs/princeton-nlp__SWE-bench_oracle__test__princeton-nlp__SWE-Llama-13b__temp-0.0__top-p-1.0.jsonl" \
    --swe_bench_tasks "./data/swe-bench.json" \
    --log_dir "./outputs/" \
    --testbed "./testbed/" \
    --skip_existing \
    --timeout 900 \
    --verbose
