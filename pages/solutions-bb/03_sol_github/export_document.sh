#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
pandoc document.md -o document.docx
pandoc document.md --standalone --pdf-engine=weasyprint -o document.pdf
