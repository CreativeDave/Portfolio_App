# Blog Portfolio App
> A dynamic blog, portfolio, and resume application enabling a user to customize nearly every detail of content through an intuitively designed backend interface. 

!['image'](./media/about.gif)
## About This Project

The intention behind this application was to enable anyone, regardless of coding experience, to choose a template and be able to create an engaing and unique website about their life and work. 

In choosing a programming framework, I wanted to challenge myself to use django in a real world example, and decided to use the Wagtail CMS because of its Page model's functionality. 

I treated this as if I were building a product for a client, taking myself through all the phases of the Project Management Life Cycle. All the way from initiation and planning on trello, to execution and testing, and finally deployment of a production build on Python-Anywhere. 

Overall, this was an incredible learning experience, and I had to challenge myself to learn much more than just django in the end. Depoying a production version of a website, even a medium-small sized one, can be fraught with unexpected challenges so I started a blog about some of my experiences and the pitfalls I had.

---

## Project Overview

There are 5 main django apps for this project.
  1. Portfolio - the project's namesake and default app. Only functionally contains:
     - settings files
     - static folder 
     - base.html & error templates
     - main urls routes
     - wsgi.py
  2. Home - the intial Wagtail migration. Functionally contains templates and models for 3 key pages:
     - Home / landing page
     - About Me page
     - Contact page 
  3. Blog - the blog application of the website. Contains templates and models for:
     - Blog Index page
     - Blog Post page
     - Blog Tag Index page
  4. Project - the projects/portfolio application of the website. Contains templates and models for:
     - Project Index page
     - Project pages
  5. ResumeCV - the resume application of the website. Contains the model and template for:
     - Resume page
    
 
     
