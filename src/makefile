
.PHONY: watcher serve dev
export AOC_SESSION="53616c7465645f5fe2c4fb50de8f7577b7540ac2d73dd82ec3e589a86ffa97337e10f280445c1c5420f1af358e40ac9d8a72a5ee410c883646888de601b99634"

watcher:
	@ tailwindcss -i app.css -o ./public/app.css --watch

run:
	@ env AOC_SESSION="53616c7465645f5fe2c4fb50de8f7577b7540ac2d73dd82ec3e589a86ffa97337e10f280445c1c5420f1af358e40ac9d8a72a5ee410c883646888de601b99634" uv run ./main.py

dev:
	@ tmux split-window -h 'make watcher' \; \
    split-window -v 'make run' \; \
    select-pane -t 0 \; \



