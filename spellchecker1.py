from neuspell import BertChecker

checker = BertChecker()
checker.from_pretrained()
print(checker.correct("I amm goinng to the dllabhada."))  # Output: "I am going to the school."