# cf.
# https://qiita.com/hankehly/items/c3e0496eb04327a53ac4#6-flower%E3%83%A2%E3%83%8B%E3%82%BF%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%84%E3%83%BC%E3%83%AB%E3%82%92%E4%BD%BF%E3%81%86
# https://qiita.com/shun198/items/74883e06d3a8d2bc98c3
# https://docs.celeryq.dev/en/stable/getting-started/first-steps-with-celery.html#first-steps
# https://zenn.dev/shimakaze_soft/articles/bbd859803c63a6


###-----------------------------------------------------------------------------
worker:
	celery --app=src.jobs.worker worker --loglevel=info

worker.dev:
	python3 -m watchdog.watchmedo auto-restart -d ./src/jobs/ --pattern '*.py' --recursive -- \
		${MAKE} worker

beat:
	celery --app=src.jobs.scheduler beat --loglevel=info --schedule=./tmp/celerybeat-schedule

beat.dev:
	python3 -m watchdog.watchmedo auto-restart -d ./src/jobs/ --pattern 'scheduler.py' --recursive -- \
		${MAKE} beat

server:
	uvicorn src.server:app --host 0.0.0.0 --port 9876 --reload

###-----------------------------------------------------------------------------
call_delay:
	python -m src.test.call_delay

call_by_name:
	python -m src.test.call_by_name
