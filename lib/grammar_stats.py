class GrammarStats:
    def __init__(self):
        self
        self.checked_count = 0 
        self.true_count = 0

    def check(self, text):
        self.checked_count +=1
        if text[0].isupper() and text[-1] in ["?", ".", "!"]:
            self.true_count += 1
            return True
        else:
            return False
        
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
    

    def percentage_good(self):
        # self.test_done = self.check.counter
        # self.test_true = self.check.count(True)
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.checked_count == 0:
            return "nothing has been checked"
        return int(self.true_count / self.checked_count  * 100)