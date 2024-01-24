#!/bin/bash

# 要保留的环境名称
keep_env1="swe-bench"
keep_env2="base"

# 获取所有环境名称
envs=$(conda env list | awk '{print $1}' )

# 循环遍历并删除不需要的环境
for env in $envs; do
    if [ "$env" != "$keep_env1" ] && [ "$env" != "$keep_env2" ] && [ "$env" != "base" ]; then
        echo "Deleting $env..."
        conda env remove -n $env
    fi
done

