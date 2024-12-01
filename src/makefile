
.PHONY: watcher serve dev

watcher:
	@ tailwindcss -i app.css -o ./public/app.css --watch

serve:
	@ uv run ./main.py

dev:
	@ tmux split-window -h 'make watcher' \; \
    split-window -v 'make serve' \; \
    select-pane -t 0 \; \

