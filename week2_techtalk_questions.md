# Week2 weekend homework
For your weekend homework, please answer one of the questions from the list below and be prepared to present this topic on Monday.

1. What is a class? What is an object? What is the difference between a class and an object? 

2. What happens when you call __init__?

3. What are instant methods and class methods? How are instant and class methods used and how are they different from one another? 

4. Explain and provide examples of inheritance in object oriented programming.

5. What are modules? Provide an example.

6. What is self? Why do all classes and methods need self?

7. What is ```if __name__ == "__main__"?'``` What is it's purpose?

8. What is lambda? What does it do and why do we use it? 

In addition, as a group, please answer the following questions:

```
What is a function? What is a method? What is the difference (if any) between a function and a method?
```

### FAQs:
1. Can I choose more than one question?

	Yes! But you must choose at least one.

3. What do we do after we answer the group question?

	Pick a representative to present it on Monday.

4. If I get picked as the group representative, do I still have to pick a function to explain?
	
	Yes.

5. How do I pick which topic I want to do?

	```py
	import random

	topics=set()
	while len(topics) != 10:
		topics.add(random.choice(dir(globals()['__builtins__'])))
	```

	(This is actually a joke, don't literally do this. I mean you can, but you can just pick a topic(s) that you'd like)

6. How long does the presentation have to be?
	
	It’s a 5 minute or less presentation. You don’t have to present exactly five minutes worth of material but we’re capping it at 5 minutes to try to get you in the habit of explaining yourself succinctly.

7. What do I do if I have questions?

	Ask! Or slack any of the TAs or Billy

**TL;DR**
 HW is to choose and explain a built in function from the list provided. Get together as a group and answer the questions about functions and methods. Be ready to explain your chosen topic(s) on Monday.
