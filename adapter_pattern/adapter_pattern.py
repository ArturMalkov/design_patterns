"""
Adapter is a construct which adapts an existing interface X to conform to the required interface Y.
Structural design pattern.
Deals with creating adapter_pattern ensuring interaction between previously incompatible object and system (makes interfaces compatible).
Adapter pattern is a wrapper - converts the interface of one class into another interface that clients (other pieces of code) expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.
Getting the interface you want from the interface you have.
IMPORTANT: adapter_pattern mustn't change the underlying behavior of the adaptee - the idea is to get access to that behaviour.
"""

import re
from abc import ABC, abstractmethod

text = """
In software engineering, a design pattern is a general repeatable solution to a commonly occurring problem in software design. 
A design pattern isn't a finished design that can be transformed directly into code.
It is a description or template for how to solve a problem that can be used in many different situations.
"""


class System:
    def __init__(self, text):
        tmp = re.sub(r"\W", " ", text.lower())
        tmp = re.sub(r" +", " ", tmp).strip()
        self.text = tmp

    def get_processed_text(self, processor):
        result = processor.process_text(self.text)
        print(*result, sep="\n")


class TextProcessor(ABC):
    @abstractmethod
    def process_text(self, text):
        pass


class WordCounter:
    def count_words(self, text):
        self.__words = dict()
        for word in text.split():
            self.__words[word] = self.__words.get(word, 0) + 1

    def get_count(self, word):
        return self.__words.get(word, 0)

    def get_all_words(self):
        return self.__words.copy()


class WordCounterAdapter(TextProcessor):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def process_text(self, text):
        self.adaptee.count_words(text)
        words = self.adaptee.get_all_words().keys()
        return sorted(words,
                      key=lambda x: self.adaptee.get_count(x),
                      reverse=True)


system = System(text)
counter = WordCounter()

adapter = WordCounterAdapter(counter)
system.get_processed_text(adapter)

