ENDPOINT  := http://localhost:4576
QUEUE_URL := http://sqs.ap-northeast-1.localhost.localstack.cloud:4566/000000000000/celery

l:
	aws sqs list-queues \
		--endpoint-url ${ENDPOINT}

r:
	aws sqs receive-message --queue-url ${QUEUE_URL} \
		--endpoint-url ${ENDPOINT}
