```
Last updated 09/17/2025
```

# Gen AI Prompt Engineering & Python
This workshop is meant to show you various ways you can potentially use the power of Generative AI to complement your programming in python to become more efficient, troubleshoot errors, learn more about weak points, and automate tedious or annoying tasks. 

## **About Me**

### Link to recording of this workshop
- [View on PanOpto]()
- [View on Youtube](https://www.youtube.com/watch?v=vE7qeXR7poY)

Erich Purpur

    Research Librarian for Science & Engineering
    epurpur@virginia.edu

I'm a part of a group called [research data services](https://data.library.virginia.edu/) and I do these things:
    
    1. Serve as Liaison to various departments in the sciences & engineering
    2. Teach workshops and classes (like this one)
    3. Help people with research projects
    4. Random other things as they come up

## Welcome to the UVA Library
* [Research Data Services](https://data.library.virginia.edu/)
* [Workshop Series](https://data.library.virginia.edu/training/)

## Upcoming Python Workshops

| Workshop | Date | Time |
| ---- | ---- | ---- |
| Intro to Python pt 1                                                |       Tuesday 9/2   |  11:00 - 12:30am
| Intro to Python pt 2                                                |       Tuesday 9/9   |  11:00 - 12:30am
| Python Data Analysis & Visualization                                |       Tuesday 9/16  |  11:00 - 12:30am
| AI Prompt Engineering for Python                                    |       Thursday 9/18 |  1:00 - 2:30pm

## Upcoming AI Workshops
| Workshop | Date | Time |
| ---- | ---- | ---- |
| Using Large Language Models Locally                                 |       Thursday 9/4   |  1:00 - 2:30pm
| AI Prompt Engineering w/ CLEAR Framework                            |       Thursday 9/11  |  1:00 - 2:30pm
| AI Prompt Engineering for Python                                    |       Thursday 9/18  |  1:00 - 2:30pm


## Generative AI background 
Generative artificial intelligence refers to a class of artificial intelligence models that have the ability to generate new content such as text, images, audio, or other types of data. These models are trained on large datasets and learn to understand patterns and structures within the data, allowing them to create new content.

One prominent example of generative AI is the GPT model (Generative Pre-Trained Transformer) which is a type of transformer architecture developed by OpenAI. GPT models are capable of generating human-like text based on the input they receive. They have been used in various applications including natural language processing, content creation, language translation, etc. Large language models, like GPT, are pre-trained on vast datasets in order to understand human-like langage patterns. Pre-Training means that massive datasets are fed into the language model containing diverse examples of human language. During this phase, the model learns to predict the next word in a sentence based on the context of the preceding words. This process helps the model capture the nuances of human language.

## AI use at UVA
Generative AI has thrown academia for a loop and while the dust has settled somewhat since ChatGPT hit the scene in late 2022, there are still a lot of questions and concerns of how to be a responsible Generative AI user. UVA has published some information about expectations, best practices, and guidelines for AI use at the university. Here are some links and resources that may be helpful:
- [UVA Honor Committee](https://honor.virginia.edu/faculty-tas/artificial-intelligence)
- [GenAI Use Guidelines](https://virginia.service-now.com/its?id=itsweb_kb_article&sys_id=8a0050d847fac610bb2b9c7b116d4317)
- [GenAI FAQ](https://genai.provost.virginia.edu/guidance-for-faculty-students)


## AI Resources at UVA
#### [Access UVA Licensed AI Resources](https://virginia.service-now.com/its?id=itsweb_kb_article&sys_id=dbe41947dbe3f91066d98f38139619db)

While most of this material is available to anyone, whether you are a part of the University of Virginia or not, these resources are available to UVA-affiliated people through our ITS department. UVA ITS maintains a page with up-to-date information of their current AI offerings. UVA is a Microsoft Campus and for that reason, I will be teaching this workshop using Microsoft's Generative AI tool, Copilot. However, results should be very similar using any other AI chatbot tool such as ChatGPT, Gemini, etc. 

**Disclaimer**
If you are a UVA-affiliated person, make sure to log into Copilot through the [UVA ITS](https://virginia.service-now.com/its?id=itsweb_kb_article&sys_id=dbe41947dbe3f91066d98f38139619db) portal. Because UVA has a site license with Microsoft, UVA's instance of Copilot will protect personal information, your chat history, etc.

## Don't Trust AI Blindly!

**From Copilot itself...**
While GPT and similar language models are powerful, there are situations where you should be cautious and not rely solely on their generated content. Situations you should not rely on generative AI include
  - factual information: GPT may not always provide accurate or up to date information. It doesn't have real-time awareness and may generate content based on outdated data or misconceptions. Verify critical information from reliable sources
  - Biases: GPT can inadvertently perpetuate biases present in its training data. Be cautious when relying on the model for sensitive or controversial topics.
  - Legal Matters: Content generated by GPT may not comply with legal or regulatory standards. Avoid relying on the model for legal, compliance, or domain expertise without consulting professionals.
  - Sensitive Personal or Confidential Information: Avoid inputing sensitive personal information into the model. GPT does not guarantee privacy.
  - Critical Decision-Making: For important decisions with consequences, human expertise should take priority.
  - Emotional or ethical considerations: GPT does not possess real emotions or ethical reasoning.
  - Technical Experise: For highly specialized or technical fields, GPT may not have the domain expertise.

To summarize, while generative AI is good for a lot of things, it is not perfect and it can be tricky to know when to use it versus when not to use it. In the rest of the workshop we will look at some use cases that I tend to use gen AI for when it comes to writing code in python. 

# GenAI is not a substitute for learning to program!
In my opinion, Generative AI is not a substitute for learning how to program. Just like any tool, you have to learn to wield it's power. I compare this to learning to drive a car. We understand that driving is a great responsibility and for that reason we have protocols in place to teach people the rules, basics, and best practices. Even then, there is a period of time where new drivers must be supervised. Just like with driving a car, with the power of GenAI comes great responsibility! 

If you blindly ask GenAI to write some code, it will do it to the best of its abilities given the information you provided. The code might even work! But what if the code you are given doesn't work? Or what if it produces unintended results? I nearly always use GenAI as I am writing code today and when I do, I am guiding it to the correct results. While GenAI makes tedious programming tasks immensely easier, it is fallible and flawed and you must supervise it. 

In order to learn how to program, you will have to struggle with it. When you at least have a grasp on the basics, then you can start to combine your programming skills with GenAI

# CLEAR Framework
In 2023, UVA Library Dean [Leo Lo](https://library.virginia.edu/news/2025/leo-lo-named-uva-librarian-and-dean-libraries) published the article: [The CLEAR path: A framework for enhancing information literacy through prompt engineering](https://www.sciencedirect.com/science/article/abs/pii/S0099133323000599). This article is a logically organized method for interacting with AI chatbots in order to get the best results possible. When writing prompts, the five points to keep in mind are...


| Letter   | Description |
| -------- | ------- |
| C | Concise. Brevity and Clarity in prompts               |
| L | Logical. Structured and coherent prompts              |
| E | Explicit. Clear output specifications                 |
| A | Adaptive. Flexibility and customization in prompts    |
| R | Reflective. Continuous evaluation and improvement of prompts    |



## Self Help

- [ChatGPT](https://chat.openai.com/)
Sign up for a free account

- [Corey Schafer - ChatGPT as a tool for programming](https://www.youtube.com/watch?v=jRAAaDll34Q)
While there are tons of youtube content creators out there, when it comes to python programming my go-to person is Corey Schafer.
