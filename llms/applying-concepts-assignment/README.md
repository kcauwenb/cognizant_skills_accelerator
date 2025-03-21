# Part 1: Techniques in Prompt Optimization
Concept Check (Multiple Choice Questions):
1. B
2. B

Application Task:
- Write a basic prompt for generating a product description for a smartphone

    A: Generate a product description for a smartphone.
- Refine this prompt using the following techniques:
    1. Add role-based instructions.
    2. Include an example to guide the AI.
    3. Specify tone and length.

    A: Imagine you are a salesperson trying to sell a smartphone to a prospective customer. Here are examples of smartphone features to talk about: thinness, camera quality, durability in water. Keep the tone upbeat and positive and make it an elevator pitch--no more than 150 words.

Reflection:
In 150-200 words, explain how prompt optimization could streamline a task you frequently perform (e.g., writing emails, generating reports, brainstorming ideas).

A: Prompt optimization could streamline any task I frequently perform, namely writing emails, by  guiding the chatbot to more specific objectives of the email in question. For example, a generic prompt would be, "write an email to my professor." But this is not a good prompt because the chatbot doesn't know what I want to accomplish with this email. Maybe I want a regrade on my assignment, and I want an apologetic tone, so specifying these to the chatbot will improve the clarity of the email.

# Part 2: Debugging Prompt Failures
Concept Check (True/False):
1. T
2. F

Application Task: 
1. Write an intentionally vague or complex prompt (e.g., "Write a story about life.").

2. Analyze the AI's response
    - Identify two specific issues with the output.

    A: 
    Output: The River's Path
    Lena had always believed that life moved in straight lines-study hard, get a good job, find happiness. But as she sat by the river that ran behind her childhood home, she realized that life was more like the water before her: winding, unpredictable, and sometimes rushing in directions she never intended.

    As a child, she spent summers by this river, dipping her toes in the cool water, dreaming of the future. She had mapped out her life perfectly-she would become a scientist, make groundbreaking discoveries, and live without regrets. But life, as it often does, had different plans.

    Her father's illness had pulled her back home after years away, forcing her to pause, to care, to understand that some things couldn't be controlled. In that pause, she rediscovered forgotten joys: the warmth of morning sunrises, the laughter of old friends, the simple pleasure of watching the river flow.

    One day, as she sat on the bank, she realized something-life wasn't about rigid paths or perfect plans. It was about adapting, about finding meaning in the detours. The river didn't resist its curves; it embraced them. And perhaps, she thought, so should she.

    With a deep breath, Lena stood up, feeling lighter. The river continued to flow, and so would she.

    Analyis: The AI's response was a generic story about enjoying the simple pleasures in life as opposed to hardening it and trying to control everything, using a girl dealing with her father's death (the uncontrollable force) as an example. The first issue is that the story trivializes the father's death, implying that enjoying simple pleasures such as watching the river flow was a solution to her trauma. Second, the story isn't really a story, like it doesn't really have a plot. It mostly tells the reader what the girl does to deal with her father's death and that's it. 

3. Refine the prompt using debugging techniques (e.g., breaking the task into smaller steps, providing context).

    A: Write a story about life on a boat. Keep the tone upbeat and engaging. Pretend you are a children's author excitedly reading middle schoolers your short story. Include pirates. Keep it down to 200 words or less.

4. Test the refined prompt and compare the new output to the original.

    A:
    Output: The Swashbuckling Life of Captain Finn!

    Captain Finn wasn't your ordinary kid-he lived on a boat! Not just any boat, but The Starfish, a grand ship that sailed the world with his daring pirate crew (who, okay, were mostly his family, but still!).

    Every morning, Finn climbed the mast to spot adventure on the horizon. One day, as The Starfish glided through sparkling blue waves, Finn's little sister, First Mate Lily, shrieked, "Pirates! Real ones!"

    Sure enough, a black-sailed ship was gaining on them. "Raise the anchor! Full speed ahead!" Finn shouted. The family-crew scrambled, pulling ropes and steering hard. But the pirates were faster.

    Just as they were about to be caught, Finn had an idea. "Quick! Throw 'em the cookies!"

    Lily tossed over a tin of Mom's famous chocolate chip treasures. The pirate captain caught it, sniffed, and grinned. "Truce!" he called. "Best cookies on the sea!"

    With a friendly wave, the pirates sailed off, happily munching. Finn laughed. "See? The best captains always think on their feet!"

    And so, The Starfish sailed on, ready for its next grand adventure-because life on a boat was never, ever boring!

    Analysis: The story is funny and engaging, just like I asked of it. Its pacing is better since it's broken down into smaller paragraphs. It definitely is on topic and reads like a children's story. It is for sure better with prompt engineering.

Case Study Activity:
Evaluate the following prompt:
"Describe a scientific concept in detail."

- What's wrong with this prompt?
    
    A: The scientific concept is not named and the AI doesn't know any context.
- Write a revised version using specific instructions and role-based guidance.

    A: Describe the theory of relativity in detail. Specifically, describe how it devised and who devised it. Keep it simple, such that a high school student taking physics could understand.

Reflection:
Describe a real-world situation where a poorly crafted prompt could cause problems. How would you apply debugging techniques to resolve this?

A: A medical nurse advice chatbot could give poor advice if poorly prompted, leading to serious harm or injury. One thing you could do is describe your problem in detail and provide context for your ailment. Also, I would hope the chatbot is predisposed to reccommending a real doctor's advice for things it's unsure about. The user could also provide their doctor's name so the chatbot could get context about what care they're already getting and tailor its answers accordingly.

# Part 3: Evaluating Prompt Effectiveness
Concept Check (Fill in the Blank):

1. To evaluate prompt effectiveness, key metrics include relevance, clarity, completeness

2. A response's relevance measures how well it aligns with the task's requirements, while completeness assesses whether all parts of the request are addressed. 

Application Task:

1. Create a prompt to generate a short email inviting coworkers to a weekend team-building event.

    A: Generate a short email inviting my coworkers to a weekend team-building event. The event details are:
    - Place: The Grotto climbing center
    - Time: Saturday, March 22 at 11:00am
    - Activity: team climbing obstacle course
    Some info about my company:
    - Name: Technitalent
    - Type: Technical consulting firm

    Please keep the email to less than 200 words and have a professional and friendly tone.

    Output:

    Subject: Join Us for a Team-Building Climbing Adventure!

    Hi Team,

    Let's take teamwork to new heights-literally! You're invited to a fun and challenging team-building event at The Grotto Climbing Center on Saturday, March 22, at 11:00 AM.

    We'll be tackling a team climbing obstacle course, designed to test our collaboration, problem-solving, and a little bit of courage-all in a supportive and exciting environment. No prior climbing experience is needed; just bring your enthusiasm!

    This is a great chance to connect outside the office, build trust, and enjoy a weekend adventure together. Please RSVP by Wednesday, March 20, so we can finalize the details.

    Looking forward to seeing you there!

    Best,

    [Your Name]

    Technitalent
    


2. Use these metrics to evaluate the AI's response:
    - Relevance: 
    - Completeness: 4
    - Clarity: 5
    - Accuracy: 5
    - Creativity: 5
    - Efficiency: 5

3. Score the response for each metric on a 1-5 scale. Reflect on how you could refine the prompt to improve any weak areas.

    A: See scores above. I think my prompt was pretty good and generated an email close to what I would've sent in real life. The only adjustment I would've made to the prompt is a request for a more detailed signature.

Activity:
Evaluate and improve the following prompt:
"Generate a summary of this document."

- Identify what's missing or unclear.

    A: The document name/file, desired summary length, and user comprehension level is unclear.

- Rewrite the prompt to include:
    - Specific instructions.
    - Context or examples.
    - A required length or focus.
    
    A: Generate a summary of Wuthering Heights by Emily Bronte. For some context, I'm reading this book for 12th grade English Literature, and we are asked to write an essay describing the theme of revenge in that book. So I would like a short summary of the book, less than 300 words, to better understand it.

Reflection:
In 150-200 words, describe how evaluating prompt effectiveness can improve productivity or reduce errors in your work or studies.

A: If I'm using AI to assist with my schoolwork, giving it vague prompts without context and clear instructions will make it generate nonspecific answers. If I improve the prompt in the areas of specificity, clarity, and accuracy, I will not make as many errors in my AI assisted work.