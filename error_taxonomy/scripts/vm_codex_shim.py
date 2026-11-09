#!/usr/bin/env python3
"""Run the installed CLI with agent tools disabled; never handle credentials."""
import os
import sys

binary = os.environ["PAPERPROOF_TAXONOMY_CODEX_BIN"]
extra = [
    "--config", 'developer_instructions="Use only the audit materials supplied in this conversation. Do not call tools, read additional files, access other sessions, or browse the web."',
    "--config", 'web_search="disabled"',
    "--config", "features.shell_tool=false",
    "--config", "features.multi_agent=false",
    "--config", "features.memories=false",
    "--config", "features.hooks=false",
    "--config", "features.plugins=false",
    "--config", "features.remote_plugin=false",
    "--config", "features.apps=false",
]
os.execv(binary, [binary, *extra, *sys.argv[1:]])
