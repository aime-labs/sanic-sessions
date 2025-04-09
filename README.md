# Sanic Session Management
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> ⚠️ **This package is a forked and updated version of [`sanic-session` 0.8.0](https://pypi.org/project/sanic-session/0.8.0/).**  
> It includes important fixes such as resolving the "Cookies Initializing" warning.  
> Updated and maintained by **Khaled Abdel Moezz** from **AIME GmbH**.

`sanic_sessions` is a session management extension for [Sanic](https://sanic.dev) that integrates server-backed sessions with a convenient API.

`sanic_sessions` provides a number of *session interfaces* for storing client session data. The available interfaces include:

- **Redis** (supports both `aioredis` and `asyncio_redis`)
- **Memcache** (via `aiomcache`)
- **MongoDB** (via `sanic_motor` and `pymongo`)
- **In-Memory** (suitable for testing and development environments)

---

## Installation

Install with `pip` (additional options available for different drivers — check documentation):

```bash
pip install sanic_sessions
```

---

## Usage Examples

### In-Memory Session Example

A simple example using the in-memory session interface:

```python
from sanic import Sanic
from sanic.response import text
from sanic_sessions import Session, InMemorySessionInterface

app = Sanic(name="ExampleApp")
session = Session(app, interface=InMemorySessionInterface())

@app.route("/")
async def index(request):
    # Interact with the session like a normal dict
    if not request.ctx.session.get('foo'):
        request.ctx.session['foo'] = 0

    request.ctx.session['foo'] += 1
    return text(str(request.ctx.session["foo"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

---

### Memcache Session Example

```python
from sanic import Sanic
from sanic.response import text
from sanic_sessions import Session
from sanic_sessions.memcache import MemcacheSessionInterface
import aiomcache

app = Sanic(name="MemcacheExample")

# Set up a Memcache client
memcache_client = aiomcache.Client("127.0.0.1", 11211)

# Bind Memcache session interface
session = Session(app, interface=MemcacheSessionInterface(
    cookie_name="session_id",
    memcache_connection=memcache_client,
    expiry=3600  # 1 hour
))

@app.route("/")
async def index(request):
    if not request.ctx.session.get('visits'):
        request.ctx.session['visits'] = 0

    request.ctx.session['visits'] += 1
    return text(f"Memcache session visit: {request.ctx.session['visits']}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

> 💡 **Note:** To use Memcache sessions, make sure:
>
> - `aiomcache` is installed:
>   ```bash
>   pip install aiomcache
>   ```
> - Memcached server is running locally:
>   ```bash
>   sudo apt install memcached
>   sudo systemctl start memcached
>   sudo systemctl status memcached
>   ```


---

### Redis Session Example

```python
from sanic import Sanic
from sanic.response import text
from sanic_sessions import Session
from sanic_sessions.redis import RedisSessionInterface
from redis.asyncio import Redis

app = Sanic(name="RedisExample")

# Setup Redis connection
@app.before_server_start
async def setup_redis(app, _):
    app.ctx.redis = Redis(host="127.0.0.1", port=6379)
    await app.ctx.redis.ping()
    print("✅ Redis connection established")

@app.after_server_stop
async def close_redis(app, _):
    await app.ctx.redis.close()

# Attach Redis session interface
session = Session(app, interface=RedisSessionInterface(
    redis_getter=lambda: app.ctx.redis,
    cookie_name="redis_session",
    expiry=3600
))

@app.route("/")
async def index(request):
    if not request.ctx.session.get('hits'):
        request.ctx.session['hits'] = 0

    request.ctx.session['hits'] += 1
    return text(f"Redis session hits: {request.ctx.session['hits']}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

> 💡 **Note:** Make sure `redis` is installed and running:
>
> - Install Python driver:
>   ```bash
>   pip install redis
>   ```
> - Start Redis server:
>   ```bash
>   sudo apt install redis
>   sudo systemctl start redis
>   sudo systemctl status redis
>   ```

