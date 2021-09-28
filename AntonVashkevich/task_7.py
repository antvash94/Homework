class Pagination:
    def __init__(self, text, symbols):
        self.text = text
        self.symbols = symbols
        self.pages = [text[i:i+symbols] for i in range(0, len(text), symbols)]

    def page_count(self):
        return len(self.pages)

    def item_count(self):
        return len(self.text)

    def count_items_on_page(self, number):
        if number not in range(self.page_count()):
            raise IndexError("Invalid index. Page is missing")
        return len(self.pages[number])

    def display_page(self, number):
        if number not in range(self.page_count()):
            raise IndexError("Invalid index. Page is missing")
        return self.pages[number]

    def find_page(self, word):
        if word in self.text:
            result = set()
            index_list = [(i, i+len(word)) for i in range(len(self.text)) if self.text.startswith(word, i)]
            for index in index_list:
                for i in range(index[0],index[1]+1):
                    result.add(i//self.symbols)
            return sorted(list(result))
        raise Exception(f"{word}' is missing on the pages")





pages = Pagination('Your beautiful text', 5)

print(pages.find_page("beautiful"))