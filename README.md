Hello everybody, Welcome to part 02 of the HBnB Evolution project.

Hopefully you still remember what happened in Part 01, because we're going to continue working on the code from that project and adding a new feature: Database Storage!

Same as before, the code you have before you is meant to serve as a foundation from which you will see how the models and classes in a system can be coded in a way that they are flexible enough to accomodate different data sources.

The code you are seeing is something I have written using my own style. You may develop your own style over time and if it differs from mine, it is ok. What is most important is that the code is well organised and easily understandable.

1. For now, ignore all the stuff in the project description about running separate Docker containers for the database. You should already have MySQL installed in your work environment. Let's just use that for now.
2. Once again, the code is not perfect. In fact, I've left a few things inside that could be optimised.
3. Look at the endpoints in app.py and see how they've all changed compared to Part 01. I've moved them all into the /api/v1 folder and there's no more clutter inside app.py!
4. Look at the __init__.py in the data folder to see what changes I've made so that we can integrate DB Storage.
5. The model classes have been modified extensively to make them work well with either File Storage or DB Storage. BUT! A lot of the methods contain unoptimised code! Is there something we can do about it?
6. You may all see a lot of lines in the model files that I have commented out. What are all these relationship things? There are a few working examples in app.py that shows how to use relationships to extract data when using DB Storage.
7. As before, let's play a game of 'Fill in the Blanks'. Challenge yourself to optimise what you see as well as complete the incomplete code to add back what's missing.
 - Review API endpoints are not defined.
 - Several model classes are missing their methods.
 - There is A LOT of unoptimised code within some of the model class methods that needs to be rewritten.
 - Relationships have been disabled in a lot of places. If you turned them back on, how would you make use of them? Note that they can only be used by DB Storage.
 - There is one specific thing regarding database connections that was not implemented. Can you all figure out what it is?