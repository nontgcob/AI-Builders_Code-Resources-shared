# T2E Vocabulary Exam Generator
This readme.md file is an explanation of this entire folder that it's in.

## Quick Links
- Demo: https://huggingface.co/spaces/nontGcob/T2E_Vocabulary_Exam_Generator
- Documentation: https://mario-world.medium.com/text-to-exam-generator-nlp-using-machine-learning-71da8dd93a4a

These are the files that are important in this folder
- Exploratory_Data_Analysis.ipynb
	- This code runs through the entire dataset that we have and analyse the part of speech of all the lexical vocabulary, the max/min/average vocabulary length, and the number of times a word is presented
- Test_&_Fine_tune_&_Retest.ipynb
	- This code tests the accuracy of the pre-trained model which is our baseline. It fine-tunes the model. And then, it tests the fine-tuned model again to check whether the accuracy has increased or not.
- Error_Analysis.ipynb
	- This code analyses the prediction by analysing the type number of correct and wrong vocabulary predictions, the types of the part of speech of the correct and wrong vocab predictions, and the average vocabulary length of the correct and wrong vocab predictions.