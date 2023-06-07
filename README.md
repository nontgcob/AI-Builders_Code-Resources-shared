# T2E Vocabulary Exam Generator
T2E Vocabulary Exam Generator as the name suggest, is an open souce program that allows user, in this case being teachers, to generate English vocabulary exam right from their browser. We aim to help reduce the pain point of teacher having to spend his/her/their precious time and effort to make the entire vocabulary exam or quiz. To try it out, click the Demo link in the Quick Links section below.

This readme.md file is an explanation of this folder that it's in.

## Quick Links
- Demo: https://huggingface.co/spaces/nontGcob/T2E_Vocabulary_Exam_Generator
- Documentation: https://mario-world.medium.com/text-to-exam-generator-nlp-using-machine-learning-71da8dd93a4a

## Important File Explanation
- Exploratory_Data_Analysis.ipynb
	- This code runs through the entire dataset that we have and analyse the part of speech of all the lexical vocabulary, the max/min/average vocabulary length, and the number of times a word is presented
- Test_&_Fine_tune_&_Retest.ipynb
	- This code tests the accuracy of the pre-trained model which is our baseline. It fine-tunes the model. And then, it tests the fine-tuned model again to check whether the accuracy has increased or not.
- Error_Analysis.ipynb
	- This code analyses the prediction by analysing the type number of correct and wrong vocabulary predictions, the types of the part of speech of the correct and wrong vocab predictions, and the average vocabulary length of the correct and wrong vocab predictions.

## Note
Please keep in mind that in order to run the .ipynb file in this folder, you must also download the "simple_trained_wsd_pipeline" and "semcor_samples_4-samples.json" as well which are not included in the folder due to the file size limitation of the code that can be uploaded to GitHub. For more information and the explanation of the entire process of this machine learning project, visit the Documentation link that is attached above in the Quick Links section.

## Contact me
- Name: Nutnornont Chamadol
- Email: nontc49@gmail.com
- Visit my personal website https://nontgcob.com/ to learn more about me.

## The MIT License (MIT)

Copyright (c) 2023 Nutnornont Chamadol

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.