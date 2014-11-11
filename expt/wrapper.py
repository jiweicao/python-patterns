"""
Hold:
Hold object O has subject S as an attribute(property) — that’s all
* use self.s.method, or O.S.method
* simple, direct, immediate, but … pretty strong coupling, often on the wrong axis
"""

"""
Wrap:
hold (often via private name) plus delegation (so you directly use O.method)
* explicit (def method(slef…)… self.s.method)
* automatic (delegation in __getattr__)
* gets coupling right (Law of Demeter)

"""
class RestrictingWrapper(object):
    def __init__(self, w, block):
        self._w = w
        self._block = block

    def __getattr__(self, n):
        # strict wrapper
        if n in self._block:
            raise AttributeError, n
        return getattr(self._w, n)


"""
* Subclassing is a problem, though:
class Foo(Singleton): pass
class Bar(Singleton): pass
f = Foo()
b = Bar()
problem is intrinsic to Singleton
"""
class Singleton(object):
    def __new__(cls, *a, **k):
        if not hasattr(cls, '_inst'):
            cls._inst = super(Singleton, cls).__new__(cls, *a, **k)
        return cls._inst

"""
Monostate("Borg")

Subclassing is no problem, just:
class Foo(Borg): pass
class Bar(Foo): pass
class Baz(Foo): __shared_state = {}

data overriding to the rescue!
"""
class Borg:
    __shared_state = {}

    def __new__(cls, *a, **k):
        obj = super(Borg, cls).__new__(cls, *a, **k)
        obj.__dict__ = cls._shared_state
        return obj

    def __str__(self):
        return self.state

"""
Template Method: self-delegation
"""
class AbstractBase(object):
  def orgMethod(self):
    self.doThis()
    self.doThat()
class Concrete(AbstractBase):
  def doThis(self): ...
  def doThat(self): ...


"""
A choice for hooks
"""
class TheBase(object):
    def doThis(self):
        # provide a default (often a no-op)
        pass
    
    def doThat(self):
        # or , force subclass to implement
        # (might also just be missing...)
        raise NotImplementedError

# origin: https://hg.python.org/cpython/file/2.7/Lib/Queue.py
class Queue:
    ...
    def put(self, item):
        self.not_full.acquire()
        try:
            while self._full():
                self.not_full.wait()
            self._put(item)
            self.not_empty.notify()
        finally:
            self.not_full.release()

    def _put(self, item):

class LifoQueueA(Queue):
    def _put(self, item):
      self.queue.appendleft(item)

class LifoQueueB(Queue):
    def _init(self, maxsize):
        self.maxsize = maxsize
        self.queue = list()
    def _get(self):
        return self.queue.pop()

