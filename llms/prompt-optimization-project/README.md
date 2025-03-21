# Part 1: Optimizing Prompts
Task: Start with a basic prompt and refine it using the optimization techniques learned in this module.

1. Choose a task for the AI:
    - Example: **Write a product description**, generate a story, or explain a concept.

2. Create three versions of the prompt:
    - Basic Prompt: A simple version with minimal guidance.

        A: Write a product description for a car.
    - Refined Prompt: Add clarity, context, or examples to improve results.

        A: Write a product description for a 2025 Nissan Altima. Include information about fuel efficiency, comfort, reliability, and spaciousness inside. Keep it under 150 words.
    - Role-Based Prompt: Assign the AI a specific persona to further refine the output.

        A: Imagine you're a car salesman and pitch me an advertisement for a 2025 Nissan Altima. Include information about fuel efficiency, comfort, reliability, and spaciousness inside. Keep it under 150 words.

3. Test all three prompts with an AI tool and compare the results.
    
    A:

    Prompt outputs:

    Prompt 1: 2025 Falcon X GT – Power Meets Precision

    Experience the perfect fusion of performance, luxury, and innovation with the 2025 Falcon X GT. Designed for those who demand more from their drive, this high-performance sports sedan boasts a 3.5L twin-turbo V6 engine delivering 480 horsepower, propelling you from 0 to 60 mph in just 3.9 seconds.

    Inside, the Falcon X GT offers a driver-focused cockpit with a 12.3-inch digital display, premium leather seating, and an AI-powered infotainment system with seamless voice control. Safety and convenience are at the forefront, featuring adaptive cruise control, lane-keeping assist, and 360-degree parking cameras.

    With its aerodynamic design, bold LED lighting, and lightweight carbon-fiber accents, the Falcon X GT is as striking as it is powerful. Whether on the open road or city streets, this car is built to turn heads and thrill at every turn.

    Unleash the future of driving – the 2025 Falcon X GT is waiting for you.

    Prompt 2: 2025 Nissan Altima – Efficiency Meets Comfort

    The 2025 Nissan Altima blends fuel efficiency, reliability, and modern comfort into a sleek midsize sedan. Powered by a 2.5L 4-cylinder engine, it delivers an impressive 39 MPG highway, making every drive economical. The spacious interior offers premium seating for five, with available Zero Gravity front seats for enhanced comfort on long trips.

    Designed for confidence, the Altima features Nissan’s Safety Shield 360, including automatic emergency braking and lane departure warning. The available Intelligent All-Wheel Drive ensures stability in all conditions.

    With a refined cabin, an 8-inch touchscreen with Apple CarPlay® and Android Auto™, and ample cargo space, the Altima is perfect for commuters and families alike. Experience a sedan that’s as practical as it is stylish.

    Drive smarter. Drive the 2025 Nissan Altima.

    Prompt 3: 🚗 Upgrade Your Drive with the 2025 Nissan Altima! 🚗

    Looking for a sedan that’s fuel-efficient, comfortable, and built to last? The 2025 Nissan Altima delivers it all! With an impressive 39 MPG on the highway, you’ll spend less time at the pump and more time enjoying the road.

    Inside, experience spacious seating for five, premium materials, and Zero Gravity front seats designed for all-day comfort. Whether it's your daily commute or a weekend getaway, the Altima keeps you riding in style.

    Safety? Nissan’s Safety Shield 360 has you covered with automatic emergency braking, lane departure warning, and available Intelligent All-Wheel Drive for ultimate confidence on the road.

    With cutting-edge tech, Apple CarPlay® and Android Auto™, and a sleek, aerodynamic design, the 2025 Nissan Altima is the smart choice for drivers who want it all.

    🔥 Efficiency. Comfort. Reliability. Drive the future today! 🔥

    Analysis: Looking at prompt 1, the AI is really good at writing a detailed description by guessing a random car. It doesn't even need to ask the user which car to write about to start writing away. Prompt 2 included a product name and points to highlight, which the AI delivered on with an impersonal tone. When changed to portray a car salesman, prompt 3 produced basically the same thing as prompt 2, but with a more friendly tone. To be fair, it reads more like an advertisement script than a car sales pitch. I would hardly hear people talking like this in real life.

# Part 2: Debugging Prompt Failures
Task: Identify and fix a problematic prompt to improve its output.

1. Write a complex or intentionally vague prompt to see how the AI responds.
    - Example: "Explain quantum physics and include jokes."
    
        Response: Quantum Physics: The Science That Breaks Your Brain (and Reality!)

        Quantum physics is the branch of science that studies the tiniest building blocks of the universe—things like electrons, photons, and other subatomic particles. Unlike the predictable world of classical physics, quantum mechanics follows rules that seem downright bizarre.

        🌀 Superposition: Being Two Places at Once?
        In quantum mechanics, particles can exist in multiple states at the same time until observed. This is called superposition.
        💡 Think of Schrödinger’s cat: it’s both alive and dead—until you check!
        Joke: Why did Schrödinger's cat stay single? Because every time someone checked on it, the relationship status changed!

        🎲 Quantum Entanglement: Spooky Action at a Distance
        Two particles can become "entangled," meaning their states are linked no matter how far apart they are. Change one, and the other changes instantly—even across galaxies!
        Joke: If you don’t believe in quantum entanglement, you and I are no longer friends. But if you do, then we are best friends—instantly!

        🔄 Heisenberg Uncertainty Principle: You Can’t Have It All
        The more precisely you know a particle’s position, the less you know about its speed, and vice versa. You just can’t measure both at the same time.
        Joke: Heisenberg gets pulled over. The cop says, “Do you know how fast you were going?” Heisenberg replies, “No, but I know exactly where I am!”

        Quantum physics may be weird, but it’s what makes modern tech possible—lasers, MRI machines, and even your smartphone. Who knew uncertainty could be so useful?

2. Analyze the response:
    - What went wrong? (e.g., vague, missing context, too complex)
        
        A: I think the aim of the prompt was to obtain a simple explanation of quantum physics with some humor injected in. This response is awkward in a way that the jokes are specified by the phrase "joke: ". It interrupts the flow of the explanation. The prompt was both vague and complex because it asked AI to explain a huge field with many concepts in a humorous way, which led to a vague explanation for each big concept.
3. Debug the prompt:
    - Break it into smaller steps, add examples, or clarify the request.

        A: Explain the following concepts in order: Superposition, Quantum Entanglement, Heisenberg Uncertainty Principle. Pretend you're Bill Nye the Science guy and inject humor into your explanation. Make it natural, for example, don't put "Joke: " before the jokes, since that's not how people talk in real life.
4. Test the refined prompt and note the differences in the output.

    Prompt output:

    Hey, hey, hey! Bill Nye the Science Guy here, and today, we’re diving into the wonderfully weird world of quantum physics—where particles misbehave, reality gets confused, and your common sense takes a vacation. Buckle up!

    🚀 Superposition: Particles Can’t Make Up Their Minds

    Imagine you’re at an ice cream shop. You can’t decide between chocolate or vanilla, so you just sort of… exist in both states until you finally place your order. That’s superposition! In the quantum realm, particles can be in two or more states at once—spinning clockwise and counterclockwise, or being in two places simultaneously.

    It’s like when you were a kid playing hide-and-seek and you thought, "If I close my eyes, I’m both hiding and not hiding!" Except in quantum physics, that actually works. Until you measure the particle, it exists in all possible states. But the moment you observe it—poof!—it picks one. Reality plays favorites.

    🔗 Quantum Entanglement: When Particles Become Soulmates

    Now, let’s say you and your best friend each grab a fortune cookie. The moment you crack yours open, you instantly know what’s inside your friend’s, no matter how far away they are—even if they’re on the other side of the galaxy. That’s quantum entanglement.

    When two particles become entangled, their states are mysteriously linked. Change one, and the other changes instantly—even if they’re light-years apart. Einstein called it "spooky action at a distance." I call it "the universe’s version of a long-distance relationship."

    🎩 Heisenberg Uncertainty Principle: You Can’t Have It All

    Ah yes, Heisenberg! The guy who basically said, "You can either know where a particle is or how fast it’s moving—but not both at the same time." It’s like when you’re late for work: you can either know your exact location (in bed, still snoozing) or your rate of acceleration (frantically running to the car), but never both accurately.

    In quantum mechanics, the more precisely you measure a particle’s position, the fuzzier its momentum becomes—and vice versa. It’s nature’s way of saying, "Hey! Stop being so nosy!"

    So, in summary:

    Superposition: Particles can’t commit.

    Entanglement: Particles have long-distance drama.

    Uncertainty Principle: The universe values its privacy.

    Isn’t quantum physics fun? Now, if you’ll excuse me, I’m off to entangle my socks in the dryer. Bill Nye—out! 🔥

    Analysis: The more detailed prompt definitely changed the output to be more naturally funny, structured, and engaging. It was overall more enjoyable to read.

# Part 3: Evaluating Prompt Effectiveness
Task: Use evaluation metrics to assess the quality of AI responses and refine prompts based on feedback.

1. Create a prompt for a specific task:
    - Example: "Write an email inviting colleagues to a team-building event."
        
    Output: Subject: Invitation: Team-Building Event – Join Us for Fun and Collaboration!

    Hi Team,

    I’m excited to invite you to an upcoming team-building event designed to strengthen our collaboration, have some fun, and take a well-deserved break from our daily routines.

    📅 Date: [Insert Date]

    ⏰ Time: [Insert Time]

    📍 Location: [Insert Location]

    🎯 Activities: [Briefly mention key activities, e.g., interactive games, group challenges, and a chance to win fun prizes]

    This will be a great opportunity to connect with colleagues in a relaxed setting, boost team spirit, and enjoy some lighthearted competition. Food and refreshments will be provided.

    Please RSVP by [Insert Deadline] so we can finalize the arrangements.

    Looking forward to seeing you there!

    [Your Name]

    [Your Job Title]

    [Contact Info, if applicable]

2. Generate the AI's response and evaluate it using the following metrics:
    - Relevance: Does the output match the task? Yes, the output writes an email for you that you only need to fill with your missing info.
    - Completeness: Does it cover all requested elements? Yes, because the user didn't ask for much. 4.
    - Clarity: Is it easy to understand? Yes, it's clearly an iinvitation addressed to coworkers. 5.
    - Accuracy: Are details correct? The details were blank so no. 1.
    - Creativity (if applicable): Is it engaging or unique? No, it's a basic email. 1.
    - Efficiency: Is it concise and to the point? It's very concise, it's a very no-frills email. 4.
3. Score the response for each metric (e.g., 1-5 scale) and calculate the total score. Seee above
4. Refine the prompt based on the evaluation and generate a new response. Compare the results.

    A: New prompt: Generate a short email inviting my coworkers to a weekend team-building event. The event details are:
    - Place: The Grotto climbing center
    - Time: Saturday, March 22 at 11:00am
    - Activity: team climbing obstacle course
    Some info about my company:
    - Name: Technitalent
    - Type: Technical consulting firm

    Please keep the email to less than 200 words and have a professional and friendly tone.

    New response: Subject: Join Us for a Team-Building Climbing Adventure!

    Hi Team,

    Let's take teamwork to new heights-literally! You're invited to a fun and challenging team-building event at The Grotto Climbing Center on Saturday, March 22, at 11:00 AM.

    We'll be tackling a team climbing obstacle course, designed to test our collaboration, problem-solving, and a little bit of courage-all in a supportive and exciting environment. No prior climbing experience is needed; just bring your enthusiasm!

    This is a great chance to connect outside the office, build trust, and enjoy a weekend adventure together. Please RSVP by Wednesday, March 20, so we can finalize the details.

    Looking forward to seeing you there!

    Best,

    [Your Name]

    Technitalent

    The new prompt generated a better scoring response in every metric except conciseness, since the email was longer. But the email was more creative, had all details filled in, and was engaging.

# Part 4: Creative Application
Task: Apply everything you've learned to solve a real-world problem.

1. Choose a creative task:
    - Examples:
        - Generate a catchy slogan for a new product.
        - **Write a step-by-step guide for a complex topic.**
        - Create a fictional story based on a given theme.
2. Optimize, debug, and evaluate your prompts to achieve the best possible results.
3. Experiment with advanced techniques like few-shot prompting or role-based guidance to enhance the output.

A. The following is an engineered prompt to write a step-by-step guide for a complex topic that uses few-shot prompting and role-based guidance.

You are a technical trainer for the software Amira-Avizo. You are asked to provide your new clients a presentation on how to use the software's Filament editor to skeletonize 3D models of neuron dendrites. Make it step by step. Please use the following guide to fine-tuning a large language model as example guidance for the structure of your presentation: 
1. Prepare your environment: 
2. Load and preprocess the dataset:
3. Fine-tune the model:
4. Evaluate the model:


