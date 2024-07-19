from transformers import AutoTokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments

model_name = "unicamp-dl/ptt5-base-portuguese-vocab"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)