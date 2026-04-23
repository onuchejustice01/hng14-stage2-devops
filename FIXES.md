#FIXES


| api/main.py | 8 | Redis connection used localhost and had no safety handling | Moved host to REDIS_HOST env var and improved connection setup with basic error handling |
| api/main.py | 12 | Queue name and job key format were inconsistent | Standardized to use jobs_queue and jobs:{id} format |
| api/main.py | 6 | No health check endpoint available | Added a /health endpoint for service monitoring |
| api/main.py | 17 | No error handling when fetching job status from Redis | Wrapped Redis call in try/except and handled failures properly |
| api/main.py | 19 | Returned a plain error dict instead of proper HTTP response | Replaced with FastAPI HTTPException (404) |





#WORKER 

| worker/worker.py | 4 | Redis host is hardcoded to localhost | Changed to use REDIS_HOST environment variable |
| worker/worker.py | 11 | Queue name does not match API format | Aligned queue name to jobs_queue for consistency |
| worker/worker.py | 11 | Worker blocks without graceful shutdown handling | Added signal handling for safe shutdown |
| worker/worker.py | 13 | No error handling during job processing | Wrapped processing logic in try/except |
| worker/worker.py | 7 | Redis connection lacks decode_responses and safety config | Updated Redis connection with proper config |


