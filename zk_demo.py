import time
from kazoo.client import KazooClient


def zk_start():
    zk = KazooClient(hosts='localhost:2181')
    zk.start()
    return zk


def zk_stop(zk):
    zk.stop()


def test_seq(zk):
    PATH = "/seq"
    if not zk.exists(PATH):
        zk.create(PATH)

    q = 100
    start = time.time()
    for i in range(q):
        zk.set(PATH, b"0")

    print q / (time.time() - start)




if __name__ == "__main__":
    zk = zk_start()
    try:
        test_seq(zk)
    except Exception, e:
        print e
    finally:
        zk_stop(zk)
