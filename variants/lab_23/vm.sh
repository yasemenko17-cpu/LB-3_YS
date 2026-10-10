#!/usr/bin/env bash
if [ "$#" -gt 0 ]; then
    echo "Помилка: аргументи не потрібні" >&2
    exit 1
fi

qemu-img create -f qcow2 data.qcow2 20G
echo "Диск моніторингу створено"
exit 0