import asyncio
import atexit

from .listener import (
    AbstractListener as abstract, run as run_loop, get_loop,
    shutdown_loop, all_listeners, thread, update_thread_loop, set_loop
)

from .. import utils

__all__ = ('disable', 'start', 'run', 'attach_to_loop')


def disable() -> None:
    try:
        shutdown_loop(get_loop())
        thread.join()
    except (RuntimeError, ValueError):
        pass

    try:
        listeners = utils.get_instances_of(abstract)
    except Exception:
        listeners = all_listeners

    for scan in listeners:
        scan.close()


def attach_to_loop(loop: asyncio.AbstractEventLoop) -> None:
    update_thread_loop(thread, loop)

    set_loop(loop)

    for listener in all_listeners:
        listener.attach_to_loop(loop)


def run(loop: asyncio.AbstractEventLoop) -> None:
    run_loop(loop)


def start() -> None:
    thread.start()


atexit.register(disable)
