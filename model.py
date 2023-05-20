def model(passage, level):
  # pip install spacy
  # pip install transformers
  # pip install torch
  # pip install en_core_web_sm
  # python -m spacy download en_core_web_sm
  # pip install spacy-download
  # pip install nltk

  # Importing libraries
  from nltk.corpus import wordnet
  import spacy
  import nltk
  import transformers
  import pandas as pd
  import json
  import random
  import torch

  nltk.download('wordnet')
  nltk.download('omw-1.4')

  # Passing file directories into variables
  # text_input = "./text_input.txt"
  cefr_vocab = "cefr-vocab.csv"

  # Create and open the text file
  # with open(text_input, "a") as file:
  #   file.write(".") # Add a full stop at the end to make sure there is a full stop at the end of the text for the model to understand where to stop the sentence


  # Ask the user for the CEFR level
  # while True:
    # cefr_level = input("Which CEFR level you want to test?: ").upper()
    # if "A1" in cefr_level or "A2" in cefr_level or "B1" in cefr_level or "B2" in cefr_level or "C1" in cefr_level or "C2" in cefr_level:
    #   break
    # else:
    #   continue
  cefr_level = level

  # Read from the input file
  # with open(text_input, "r") as file:
  #   txt = str(file.readlines()).replace("[", "").replace("'", "").replace("]", "")
  txt = passage + "."

  if "." in txt:
    txt = (txt.split("."))
  else:
    txt = txt

  # Part Of Speech tagging (POS tagging)
  nlp = spacy.load("en_core_web_sm")

  text_dict = {}
  for n in txt:
    n = n.strip()
    ex1 = nlp(n)

    for word in ex1:
      sentence_question_tag = n.replace(word.text, f"[{word.text}]")
      text_dict[f"{word.lemma_} = {sentence_question_tag}"] = word.pos_

  # Collect the tagging results (filter in just NOUN, PROPN, VERB, ADJ, or ADV only)
  collector = {}
  for key, value in text_dict.items():
    if "NOUN" in value or "PROPN" in value or "VERB" in value or "ADJ" in value or "ADV" in value:
      collector[key] = value

  # Collect the CEFR level of the words collected before
  reference = pd.read_csv(cefr_vocab)

  matching = {}
  for row_idx in range(reference.shape[0]):
    row = reference.iloc[row_idx]
    key = f"{row.headword}, {row.pos}"
    matching[key] = row.CEFR

  # Convert pos of the word into all lowercase to match another data set with CEFR level
  for key1, value1 in collector.items():
    if value1 == "NOUN":
      collector[key1] = "noun"
    if value1 == "VERB":
      collector[key1] = "verb"
    if value1 == "ADJ":
      collector[key1] = "adjective"
    if value1 == "ADV":
      collector[key1] = "adverb"

  # Matching 2 datasets together by the word and the pos
  ready2filter = {}
  for key, value in matching.items():
    first_key, second_key = key.split(", ")
    for key2, value2 in collector.items():
      key2 = key2.split(" = ")
      if first_key == key2[0].lower():
        if second_key == value2:
          ready2filter[f"{key} = {key2[1]}"] = value

  # Filter in just the vocab that has the selected CEFR level that the user provided at the beginning
  filtered0 = {}
  for key, value in ready2filter.items():
      if value == cefr_level:
          filtered0[key] = value

  # Rearrange the Python dictionary structure
  filtered = {}
  for key, value in filtered0.items():
      key_parts = key.split(', ')
      new_key = key_parts[0]
      new_value = key_parts[1]
      filtered[new_key] = new_value

  # Grab the definition of each vocab from the wordnet English dictionary
  def_filtered = {}
  for key3, value3 in filtered.items():
    syns = wordnet.synsets(key3)
    partofspeech, context = value3.split(" = ")
    def_filtered[f"{key3} = {context}"] = []

    # pos conversion
    if partofspeech == "noun":
      partofspeech = "n"
    if partofspeech == "verb":
      partofspeech = "v"
    if partofspeech == "adjective":
      partofspeech = "s"
    if partofspeech == "adverb":
      partofspeech = "r"

    # print("def_filtered 0:", def_filtered)

    # Adding the definitions into the Python dictionary, def_filtered (syns variable does the job of finding the relevant word aka synonyms)
    for s in syns:
        # print('s:', s)
        # print("syns:", syns)
        def_filtered[f"{key3} = {context}"].append(s.definition())
        # print("def_filtered 1:", def_filtered)

  # Use Nvidia CUDA core if available
  if torch.cuda.is_available():
      device=0
  else:
      device='cpu'

  # Declare the (trained) model that will be used
  classifier = transformers.pipeline("zero-shot-classification", model="simple_trained_wsd_pipeline", device=device)

  # Process Python dictionary, def_filtered
  correct_def = {}
  for key4, value4 in def_filtered.items():
    vocab, context = key4.split(" = ")
    sequence_to_classify = context
    candidate_labels = value4
    correct_def[key4] = []
    hypothesis_template = 'The meaning of [' + vocab + '] is {}.'

    output = classifier(sequence_to_classify, candidate_labels, hypothesis_template=hypothesis_template)

    # Process the score of each definition and add it to the Python dictionary, correct_def
    for label, score in zip(output['labels'], output['scores']):
        correct_def[key4].append(f"{score:.5f}, {label}")

  return correct_def

  # with open(T2E_exam, "r") as file:
  #    exam = file.readlines()
  # print(exam)
  # return(exam)


# passage = "Computer is good"
# level = "A1"
# print(model(passage, level))