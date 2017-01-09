**GENERAL**

Feel free to partition a personal section of scratchpad.md to write your own notes. This can be anything you want, feature ideas, bugs, design notes/suggestions etc.

We are currently trying to make the build process easier. Hopefully, if you are on a Linux machine you can just type: make install and all the dependencies will be installed with the program. Let us know if that doesn't work out. You also need git to clone the development branch.

If you need a virtual machine with the dependencies installed, email: mfeneley@vt.edu

Getting Ready For Development:
    1. Sign up for a GitHub account 
    2. Fork the project
    3. Clone the fork
    4. Checkout the dev branch: git checkout dev
    DO WORK
    5. Add upstream project: git add remote upstream https://github.com/mikefeneley/chaos-monitor.git
    6. Fetch from upsteam: git fetch upstream
    7. Merge changes: git merge upstream/dev
    8. Push request: git push



**BEGINNER**

## Testing

Testing is the best way for beginers to contribute. First, it is a great way to learn how the program works. Second, testing is the most helpful contribution in general. It helps strengthens the code base, speeds up development clarifies interface details, and forces exact defintions of function behavior. 

We try to make sure that there are tests to implement at any time. Look in the tests folder and open up one of the files ending in .py. If there is a function with a detailed description of what is being tested but no code to test it, then this is functionality that needs to be verified. We aim to come up with a tag that indicates when a test has been implemented or not.

EXAMPLE: --- Function with no code below docstring. Needs to be implemented.

def test_that_some_function_performs_correctly()
"""
This is the first line that describes what is being tested.

This is the second line that defines how the function should behave.

What To Test: -- This section indicates exactly how the test should be implemetned.
    1. Create a variable.
    2. Assign the variable the value 3
    3. Assert that the variable value is 3
    5. Assign the variable the value 4
    6. Asser that the variable value is 4
""" 

pass -- Test Code Needs to Go Here. Replace pass with test implementation.

END EXAMPLE

## Formating

Clean up the code. Make sure it follows pep8 style guide. Note: We generally ignore the 80 character line limit so if you use autopep8, make sure to set the line limit to >200 to make sure it doesn't improperly format long lines.

Check for spelling and grammar errors. Look for mismatched vocabulary. For example, when the project started, we were calling the data stored in the checksum database checksum pairs, but now we are storing three fields to so we are switching to calling them checksum tuples instead. There are many instances where the comments refer to them as checksum pairs 

## Documentation/Tutorials

If you are just getting started working on the code, you have a useful perspective. It is easier for a beginer to undstand which parts of the code and documentation are confusing. If you see something that is unclear, it is helpful if you make a note and think of a way that it could be explained better.

<INTERMEDIATE>

Look into unimplemented skeleton functions in the codebase. If you understand the comment description, go ahead and start working. We are putting together a system to stop overlapping work. For now, just tell someone what you are doing so someone else doesn't work on the same part.

Help design tests. We don't want people to design tests for their own function, but we are ok with them implementing tests designed by someone else.

<ADVANCED>

Help with high level design/architecture. Write function stubs and definitions for new features and functionality.
