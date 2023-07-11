from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @staticmethod
    @abstractmethod
    def work():
        ...


class Worker(BaseWorker):

    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(BaseWorker):

    @staticmethod
    def work():
        print("I work very hard!!!")


class UltimateWorker(BaseWorker):

    @staticmethod
    def work():
        print("working 24/7")


class Boss(UltimateWorker):\
    pass


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        if not isinstance(worker, BaseWorker):
            raise AssertionError(f"`worker` must subclass of type {BaseWorker}")  # this is adopted to python 3

        self.worker = worker

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = Worker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = UltimateWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
