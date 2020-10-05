from abc import ABC, abstractmethod


class Printer(ABC):

    @abstractmethod
    def print(self, content): pass

    @abstractmethod
    def scan(self, content): pass

    @abstractmethod
    def photocopy(self, content): pass

    @abstractmethod
    def fax(self, content): pass

    @abstractmethod
    def print_duplex(self, content): pass


# Above we have created the fat interface which perform everything

# But some of the printer may not perform some methods. This will break LSP(Liskov substitution principle).

# So to handle this we will break Big fat interface with smaller relevant interfaces.


class IPrinter(ABC):
    @abstractmethod
    def print(self, content): pass

    @abstractmethod
    def scan(self, content): pass

    @abstractmethod
    def photocopy(self, content): pass


class FaxContent(ABC):

    @abstractmethod
    def fax(self, content): pass


class PrintDuplexContent(ABC):
    @abstractmethod
    def print_duplex_content(self, content): pass
