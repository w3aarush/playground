from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained('bert-base-uncased')

text = "The king and the queen are happy."
tokenizer.tokenize(text, add_special_tokens=True)
print(text)