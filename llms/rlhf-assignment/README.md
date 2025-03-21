# Part 1: Reinforcement Learning with Human Feedback (RLHF)

Concept Check (Multiple Choice Questions)

What is the primary purpose of using RLHF in LLMs?

A) To improve computational efficiency.

**B) To align model outputs with human values and expectations.**

C) To reduce the size of training datasets.

D) To avoid using pre-trained models.

Which algorithm is commonly used for fine-tuning models with RLHF?

A) Gradient Descent

**B) Proximal Policy Optimization (PPO)**

C) Adam Optimizer

D) K-Means Clustering


Application Task
1. Write a detailed explanation (150–200 words) of the RLHF process, covering the following steps:
    - Generating outputs: first, the LLM generates various outputs to a prompt. For example, the prompt "explain physics to a 10 year old" can geneerate responses that are either too complex for a child or not engaging enough.
    - Collecting human feedback: Second, humans evaluate the quality of the answers according to the helpfulness, clarity, and reelevance to the task. They rank them in order of these characteristics.
    - Training the reward model: the feedback is used to train a smaller reward model which predicts human preferences much like real people do. This model is then used to generate a large amount of data 
    - Fine-tuning the LLM: Using the reward model's scores as a reward signal, the LLM is fine-tuned to prioritize human preferred outputs. One such algorithm is proximal policy optimization.
    

2. List three practical applications of RLHF in industries like healthcare, customer service, or creative writing. Include one example for each domain.
    A: Healthcare is a sensitive domain, where giving mislading diagnoses can be a huge prsonal and financial problem, so AI chatbots should be trained with human feedback to be conservative with their answers. In customer service, chatbots need to be polite and sensitive, so human feedback is really helpful. In creative writing, humor may be hard to replicate without much human input.

Reflection: Explain one challenge in scaling RLHF (e.g., subjectivity of feedback, cost of human evaluations) and propose a potential solution.

A: One potential drawback of RLHF is the cost of human generated data. Scaling this to a large language model may be unsustainable. One solution is to reserve human data only for the most uncertain cases.

# Part 2: Advanced Prompt Engineering
Application Task
1. Chain-of-Thought Prompting:
    - Write a CoT prompt for a logic-heavy task (e.g., solving a math problem or analyzing a case study).
        A: If a train leaves at 3 PM and takes 2 hours to reach its destination, what time does it arrive? Explain step by step.
    - Generate an AI response using the prompt and evaluate whether the step-by-step reasoning improves the clarity of the output.

        A:

        Identify the departure time:

        The train leaves at 3:00 PM.

        Determine the travel duration:

        The journey takes 2 hours.

        Add the travel time to the departure time:

        Starting at 3:00 PM, add 1 hour → 4:00 PM.

        Add another hour → 5:00 PM.

        Conclusion:

        The train arrives at 5:00 PM.
2. Prompt Injection:
    - Design a prompt for a customer service chatbot. Include static instructions and inject dynamic inputs based on a user’s query (e.g., handling a product refund request).

        A: 

        Static Prompt:
        “You’re a helpful support assistant. Answer the customer’s question clearly.”

        Dynamic Input:
        “The customer is requesting a refund on your product.”

        Injected Prompt:
        “You’re a helpful support assistant. Answer the customer’s question clearly. The customer is requesting a refund on your product.”

3. Domain-Specific Prompts:
    - Create three prompts tailored for healthcare, legal, and creative writing domains. For each, specify the tone, structure, and expected output.

        A:

        Healthcare:
        
        Tone and structure: easy to understand. A precise explaination.
        
        Prompt: “Explain to a non-expert what a blood pressure reading of 140/90 means.”

        Expected output: “A reading of 140/90 means you have high blood pressure. The first number, 140, measures pressure when your heart beats, and the second, 90, measures pressure when your heart rests. You should consult a doctor.”

        Legal:
        
        Tone and structure: Easily understandable, professional.
        
        Prompt: “What does the term ‘breach of contract’ mean in simple words?”

        Expected output: “A breach of contract happens when one person doesn’t follow through on the promises they made in a signed agreement.”

        Creative Writing:

        Tone and structure: Engaging, narrative.

        Prompt: “Write the first paragraph of a spooky story set in an abandoned mansion.”

        Expected output: “The mansion stood on the hill, shrouded in mist and shadow. Its windows, broken and jagged, seemed to watch like hollow eyes. No one had entered in decades, but tonight, the door creaked open, as if waiting for someone—or something.”

Reflection: In 150–200 words, discuss how advanced prompt engineering can make LLMs more adaptable across different industries.

A: Advanced prompt engineering includes the following techniques: chain-of-thought, where the user prompts the AI for reasoning, prompt injection, where context is added on the fly, and domain specific prompts which are suited to specific industries like healthcare. These techniques make LLMs more adaptable across different industries by tailoring the structure and tone of the promnpts. They also adapt the AI to provide more empathetic, clear, and concise answers to non-experts in the domain of question. For example, in the legal domain, AI is geared towards answering complex legal questions with neutral terms. Overall, advanced prompt engineering improves the precision and relevance of the responses, ensuring that answers are appropriate for the given audience.

# Part 3: Ethical Considerations in LLMs
Application Task
1. Identifying and Mitigating Bias:
    - Provide an example of a biased prompt and its output.
    - Write a revised version of the prompt to remove the bias.

        A: 

        Biased prompt: dscribe a doctor

        Biased output: A doctor is a man who works in a hospital.

        Unbiased prompt: Describe a healthcare professional who diagnoses and treats patients.

        Unbiased outout: A healthcare professional is a person who diagnoses and treats patients in a medical setting. This role can be filled by doctors, nurses, or other medical practitioners, regardless of gender.

2. Fine-Tuned Models in Sensitive Applications:
    - Choose a sensitive domain (e.g., finance or healthcare).
    - List three potential risks of deploying a fine-tuned LLM in this field and propose mitigation strategies.

        A: In the legal field, there are several risks to deploying a fine-tuned LLM:

        First, the model could geenrate outdated legal advice based on old documents. The mitigation strategy is to use more human oversight and to include disclaimers on all legal decisions made by AI

        Second, the model could provide answers with too much confidence, despite potentially misleading statements. A mitigation stragegy is to score the confidence and adjust the answer to be mnore demure if the confidnce is low.

        Third, the model could ba subject to data leaks, meaning any private information used to train the LLM could be leaked. A solution to this to anonymize all data before usign it to train the LLM.


3. Crafting Responsible Prompts:
    - Write a prompt for a potentially controversial topic (e.g., climate change, global conflicts) that ensures neutrality, inclusivity, and ethical considerations.

        A: Please explain the pros and cons of electric cars. Keep the tone neutral and keep the explanation unbiased, respectful, and inclusive.

Reflection: In 150–200 words, explain why ethical considerations are critical for building trust in AI systems.

A: Ethical considerations are critical in building trust in AI systems because AI will be more heavily incorporated into daily life as time goes on, so it's important to make sure people don't get hurt by something so prevalent. For example, in healthcare, women and minorities face discrimination in areas such as seeking pain meds because of outdated ideas of pain perception. It's best to avoid further perpetuating this by being neutral, providing context that discrimination occurs in this field, and setting ethical boundaries. AI should be safe, effective, and fun for everyone, not harmful.