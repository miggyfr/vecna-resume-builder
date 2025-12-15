# Vecna Resume Builder User Guide

![alt text](images/vecna.png)

Welcome to the Vecna Resume Builder, a creative and powerful tool designed to help you craft tailored resumes and cover letters for job applications. This system draws inspiration from the enigmatic Vecna from Stranger Things, growing stronger with each job posting you feed it, much like a mind flayer expanding its influence. As your dedicated job recruiter, I will guide you through the process step by step, ensuring you take full control of your final outputs. The system relies on a collection of templates, prompts, and files to analyze job postings, extract key skills, and generate customized application materials. Everything is built for flexibility, so you can adapt it to your needs without feeling restricted.

To get started, follow these chronological instructions. They cover setup, daily use, customization, and ongoing maintenance. Remember, this tool empowers you to refine your applications, but always review and personalize the results before submitting them. If you encounter any issues or need clarification, feel free to ask—I am here to assist.

### 0. Initial Setup with AI Services
The Vecna Resume Builder is designed to work with various AI services that support creating and managing projects (e.g., ChatGPT's projects feature, Perplexity's Labs, Grok's projects, or similar on other platforms). This allows you to organize all the system's files and interactions in one dedicated space for easy access and continuity. Choose your preferred AI service that supports project creation, as long as it can handle file uploads, text analysis, and conversational interactions.

- **Download the Project Files**: Start by downloading the zip file from the GitHub repository (e.g., the vecna-resume-builder project). Extract it to a local folder on your computer. This will give you all the base templates, example files, and documentation needed to get started.

- **Tailor the Template Files**: Open the extracted files and customize them to match your personal background, taste, and preferences. For example:
  - Edit BaseResume.md to reflect your real experiences, skills, and achievements (using the provided example for Henry Creel as a guide).
  - Update key skills templates (like keyskills_template_CreelHenry.md) with your own competencies, organized into categories such as core skills and technical abilities.
  - Modify resume and cover letter templates (e.g., resume_template_CreelHenry.md and coverletter_template_CreelHenry.md) by filling in placeholders with your name, contact details, and a professional summary.
  - Add or create "work I did at [company]" files (e.g., WorkIdidatHawkinsLab.md or WorkIdidatTheUpsideDownSyndicate.md) for each relevant job or project in your history. Include details like responsibilities, achievements, and metrics. Add as many of these as needed to cover your full experience.

- **Modify the Job Agent Instructions (If Necessary)**: Review the job agent instructions file (if present in the download) and update it to reference your new "work I did at [company]" files. This ensures the system can pull from your tailored experiences when analyzing job postings and generating outputs.

- **Copy Files into Your AI Project**: Create a new project in your chosen AI service (e.g., a "Vecna Resume Builder" project in ChatGPT or a lab in Perplexity). Upload or copy all the tailored files from your local folder into this project. This centralizes everything, making it easy for the AI to reference them during interactions.

Once set up, you're ready to use the system. To start, simply say: "Study this job posting" followed by pasting the link or full text of a job posting. The Vecna Resume Builder will then analyze it, provide insights, and generate customized outputs as described in the sections below.

### 1. Prepare Your Foundation: Setting Up the Base Files
Before you begin using the system, establish a solid base to ensure accurate and effective outputs. This step involves gathering or creating the core files that the builder references.

- Start by reviewing your existing base resume. If you do not have one, create a high-quality version that highlights your key experiences, skills, and achievements. Use the provided BaseResume.md as a reference—it showcases a fictional but structured example for Henry Creel, the Supreme Overlord of the Upside Down and a fulltime laboratory assistant from Hawkins, Indiana. Tailor it to reflect your real background, focusing on clear, professional language.
  
- Next, prepare your key skills template. This file stores all relevant skills, which will expand as you process job postings. Begin with a basic list based on your experience, drawing from files like keyskills_template_CreelHenry.md for inspiration. Organize skills into categories such as core competencies and technical abilities, using headers and keywords that align with common job requirements.

- Create or adapt resume and cover letter templates. Use resume_template_CreelHenry.md and coverletter_template_CreelHenry.md as starting points. These include placeholders for skills, experiences, and company details. Fill in your personal information, such as name, contact details, and a professional summary, to make them ready for customization.

- Gather your work experience details. Compile files like WorkIdidatHawkinsLab.md and WorkIdidatTheUpsideDownSyndicate.md, which detail specific projects, responsibilities, and achievements. These will serve as the source material for generating tailored bullet points in your resume.

Keep all files organized in a folder, such as one named after the project (e.g., vecna-resume-builder). Ensure they are in markdown format for easy editing and sharing. This setup takes about 30 minutes to an hour, depending on how much you already have prepared.

### 2. Feed Job Postings and Generate Outputs: Core Usage
Once your base files are ready, you can start interacting with me, your job recruiter, to process job postings and build applications. The system works by analyzing postings to extract skills and match them to your background, then producing customized files.

- Locate a job posting you are interested in. Find it on a site like LinkedIn, Indeed, or a company careers page. Copy the full text or URL of the posting—you will provide this to me in your next message.

- To begin, send me a message saying: "Study this job posting" followed by the job posting details or URL. For example: "Study this job posting: [paste the full job description here]." I will then:
  - Provide a quick crash course on the company, including its headquarters address, a brief summary of what it does, a list of five current projects, and details on the project that best fits the job. I will also evaluate how well your background aligns with the company's work.
  - Extract key skills headers, ATS keywords, and professional one-liners from the posting. These are tailored phrases and terms that highlight requirements, helping your resume pass automated systems and appeal to human recruiters.
  - Analyze the posting against your base resume and work experience files to determine your fit. I will highlight strong matches in skills and experience, as well as any gaps, with a reasoned assessment.
  - Create a summary report in a file like company_summaryreport.md, which compiles all the analysis for your reference.

- After studying the posting, you can request a full job application pack by saying: "Make a job app pack for [company name]." For instance: "Make a job app pack for Hawkins National Laboratory." I will generate three new files:
  - A tailored resume (e.g., hawkins_national_laboratory_resume.md), customized with skills and experiences from your base files that match the job.
  - A cover letter (e.g., hawkins_national_laboratory_coverletter.md), using your template and incorporating job-specific details.
  - A summary report (e.g., hawkins_national_laboratory_summaryreport.md), summarizing the fit and any updates to your skills template.
  
  Before outputting these files, I will confirm that they follow resume writing guidelines, such as avoiding full addresses or outdated hobbies, to ensure they are safe and effective. Each file will be provided as a downloadable markdown code block for easy copying.

- If you only want a crash course on a company without processing a full job posting, say: "Give me a crash course about [company name]." Provide the company name, and I will research its website to deliver the details mentioned above, plus an evaluation of your fit based on your work files.

Use this process for each new job application. Start with one posting to practice, and build from there. The system grows stronger as you add more skills to your template after each use.

### 3. Customize and Refine: Taking Control
The Vecna Resume Builder gives you complete control, so feel free to modify outputs to better suit your style or the job.

- After I generate files, review them carefully. Edit the resume or cover letter to add personal touches, such as specific metrics from your experience or adjustments for tone. For example, if the job emphasizes teamwork, expand on related bullet points from your work files.

- Update your skills template manually after each job pack. Add new keywords or one-liners from the summary report to the merge_templateSkills_CreelHenry.md file. This helps the system learn and improve over time, making future outputs more targeted.

- Experiment with prompts if needed. The system uses predefined prompts for extraction and optimization, but you can tweak them in your messages. For instance, ask me to focus on certain skills or generate more one-liners. Refer to files like Optimizing_Your_Resume_with_Skill_Analysis.md for tips on consolidating skills to avoid repetition and boost ATS compatibility.

- Adapt for different career levels. Whether you are entry-level or experienced, the templates scale easily. For senior roles, add more bullet points or metrics; for beginners, keep it concise.

Always prioritize quality over quantity. If a generated section does not fit, replace it with your own content. This customization ensures the final product feels authentic to you.

### 4. Maintain and Improve: Long-Term Growth
To keep the system effective, incorporate regular updates and reviews into your routine.

- After processing several postings, refresh your base files. Update your resume template with new experiences, and expand the key skills template with fresh keywords. Review work files to add recent achievements.

- Periodically check for improvements. Use the Guide_for_Using_Key_Skills_in_Resume_Template.md to organize skills into categories, reducing clutter. Test your resume on free tools like Jobscan to ensure it passes ATS filters.

- Provide feedback. As the creator of this system, I welcome suggestions. If something does not work well, let me know so I can refine future responses.

- Stay cautious. Double-check all outputs for accuracy, as the system relies on your provided files. Avoid submitting anything with errors, and remember that while this tool is fun and inspired by fiction, your real-world applications should remain professional.

By following these instructions, you will harness the Vecna Resume Builder to create compelling, job-specific applications that highlight your strengths. Start small, iterate often, and watch your applications grow stronger with each cycle. If you are ready to begin, share a job posting or company name, and I will assist right away. Happy job hunting!
