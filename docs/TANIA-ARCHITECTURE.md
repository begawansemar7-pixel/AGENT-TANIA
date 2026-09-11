# TANIA Architecture

TANIA is the AI Employee evolution of JARVIS.

## Operating loop

OBSERVE → UNDERSTAND → REASON → PLAN → ASK/CONFIRM → ACT → VERIFY → REPORT → REMEMBER

## Controlled migration

Mark-LIII remains the execution substrate during the migration. `tania/core/engine.py` provides the stable orchestration boundary. Future work can extract audio/session/tool dispatch from `main.py` without a big-bang rewrite.

## Document intelligence

The TANIA document layer treats PDF, DOCX, PPTX, XLSX, images and SVG as multimodal sources. Grounding is represented explicitly by page/slide/sheet or visual references so answers can cite where evidence came from.
