# Migration Map

| Existing Mark-LIII | TANIA target |
|---|---|
| main.py / JarvisLive | tania/core/engine.py + runtime adapters |
| actions/* | tania/tools/* and action compatibility layer |
| core/plugin_loader.py | TANIA tool/plugin registry |
| core/confirm.py | TANIA risk + confirmation service |
| core/undo.py | TANIA reversible action journal |
| memory/* | layered TANIA memory |
| actions/file_processor.py | multimodal document agent |
| dashboard/* | TANIA HUD / observability |
